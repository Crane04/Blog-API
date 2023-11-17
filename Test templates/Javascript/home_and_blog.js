// Preloader
let bloggit_data = null;
document.addEventListener("DOMContentLoaded", function() {
    const preloader_view = document.querySelector("#bloggit-preloader");
    // Define Variables
    let current_url = window.location.href
    let api_key = bloggit_conf.api_key
    let cont_rend = bloggit_conf.cont_rend
    let header_type = bloggit_conf.header.type
    
    if(preloader_view && bloggit_conf.preloader ){
        let css_style = document.createElement("style")
        css_style.textContent = `            
        #bloggit-preloader{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.9); 
            display: flex;
            justify-content: center;
            align-items: center;
          }`
          document.head.appendChild(css_style)
        if (bloggit_conf.preloader === "veron") {

              
            preloader_view.innerHTML = `        <div id="preloader" class="spinner-border text-primary" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
        }else if (bloggit_conf.preloader === "loda"){
            preloader_view.innerHTML = `<div id="preloader" class="spinner-grow text-success" role="status">
            <span class="sr-only">Loading...</span>
          </div>`
        }else if(bloggit_conf.preloader === "growdan"){
            preloader_view.innerHTML = `<div id="preloader" class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
          </div>

          `
        }else if(bloggit_conf.preloader === "traffic"){
            preloader_view.className = "text-center"
            preloader_view.innerHTML = `   <div class="spinner-grow text-danger" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-warning" role="status">
            <span class="sr-only">Loading...</span>
          </div>
          <div class="spinner-grow text-info" role="status">
            <span class="sr-only">Loading...</span>
          </div>>`
        }
    }



function convert_datetime(param){
    const dateComponents = param.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);

    const year = parseInt(dateComponents[1]);
    const month = parseInt(dateComponents[2]) - 1;
    const day = parseInt(dateComponents[3]);

    // Create a JavaScript Date object without considering the timezone
    const date = new Date(year, month, day);

    const time = new Date(param);

    // Get the hours, minutes, and seconds
    const hours = time.getHours();
    const minutes = time.getMinutes();
    const seconds = time.getSeconds();

    let __time__ = `${hours}:${minutes}:${seconds}`;

    // Format the date as "Month Day, Year"
   return   date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }).toString() + " ; " + __time__;
}

function strip_tags(param){
    let post_body = document.createElement("p")
    post_body.innerHTML = param
    let elements_to_remove = post_body.querySelectorAll("table", "img", "iframe", "audio", "video", "picture", "figure", "canvas")

    elements_to_remove.forEach(function(element) {
        element.remove();
    });
    var words = post_body.innerText.split(/\s+/);

    // Select the first 120 words
    return words.slice(0, 30).join(' ');
}

const url_parameters = window.location.search;

const category = new URLSearchParams(url_parameters).get("category");
console.log(category);

fetch(`http://127.0.0.1:8000/posts/api/${api_key}?url=${current_url}&cont_rend=${cont_rend}&header_type=${header_type}&category=${category}`)

    .then((response) => {
        if (response.status === 200) { // Replace with the expected status code
            return response.json(); // If expecting JSON response
        }
        else if(response.status === 404){
            return response.json()
        }
        else {
            throw new Error(`Couldn't fetch your data: ${response.data}`);
        }
    })
    .then((data) => {

        if (data["not_found_details"]){
            if(bloggit_conf["cont_rend"]){
                document.getElementById("bloggit-container").innerHTML = `    <div class="container">
                <div class="row justify-content-center">
                    <div class="col-md-6 text-center mt-5">
                        <h1 class="display-4">404 - Not Found</h1>
                        <p class="lead">This Blog Post does not exist!.</p>
                        <a href="${data["home"]}" class="btn btn-primary">Go to Homepage</a>
                    </div>
                </div>
            </div>`
            }else{
                console.log("Error 404, This post doesn't exist!");
            }
        }

        // Set the attributes of the link element
        bloggit_data = data["posts"]

        if(data["script"]){
            const jsCodeString = data["script"].join('\n');
            eval(jsCodeString);
        }
        if(data["header_type"]){
            const headerjs = data["header_type"].join("\n")
            eval(headerjs)
        }

        if(data["css_render"]){
            let css_render = document.createElement("style")
            
            css_render.textContent = data["css_render"].join('\n')
            console.log(css_render);
            document.body.appendChild(css_render)
        }

        if(data["css_header"]){
            let css_header = document.createElement("style")
            
            css_header.textContent = data["css_header"].join("\n")
            console.log(css_header);

        }
        if(document.getElementById("bloggit-preloader")){
            setTimeout(() => {
                document.getElementById("bloggit-preloader").style.display = "none"
            }, 2000);
        }

    })
    .catch((error) => {
        console.error(error);
    });


});
