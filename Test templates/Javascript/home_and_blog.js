let bloggit_data = null;
var SendComment = null;

    // Define Variables
    const preloader_view = document.querySelector("#bloggit-preloader");
    let current_url = window.location.href
    let api_key = bloggit_conf.api_key
    let cont_rend = bloggit_conf.cont_rend
    if(bloggit_conf.header){
        var header_type = bloggit_conf.header.type
    }
    if(bloggit_conf.comment){
        var comment_rf = bloggit_conf.comment.render_form
        var comment_rc = bloggit_conf.comment.render_comments
        var comment_data = true
        var bloggit_comment_data = null;
    }else{
        var comment_rf = false, comment_rc = false
        var comment_data = false
    }
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
            z-index:1000;
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
    const originalDate = new Date(param);
    const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    
    const options = {
      timeZone: userTimeZone,
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: 'numeric',
      minute: 'numeric',
      second: 'numeric',
      hour12: false
    };
    
    const convertedDate = new Intl.DateTimeFormat('en-US', options).format(originalDate);
    return convertedDate
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

fetch(`http://127.0.0.1:8000/posts/api/${api_key}?url=${current_url}&cont_rend=${cont_rend}&header_type=${header_type}&category=${category}&comment=${comment_data}&comment_rf=${comment_rf}&comment_rc=${comment_rc}`)

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
                document.getElementById("bloggit-container").innerHTML = `    
                <div class="container">
                    <div class="row justify-content-center">
                        <div class="col-md-6 text-center mt-5">
                            <h1 class="display-4">404 - Not Found</h1>
                            <p class="lead">This Blog Post does not exist!.</p>
                            <a href="${data["home_page"]}" class="btn btn-primary">Go to Homepage</a>
                        </div>
                    </div>
                </div>`
            }else{
                console.log("Error 404, This post doesn't exist!");
            }
        }

        // Set the attributes of the link element
        bloggit_data = (data["posts"] !== undefined) ? data["posts"] : data["post"];


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
            document.body.appendChild(css_render)
        }

        if(data["css_header"]){
            let css_header = document.createElement("style")

            css_header.textContent = data["css_header"].join("\n")

        }
        if(data["comments"]){
            bloggit_comment_data = data["comments"]

            let send_comment_link = document.createElement("script")
            send_comment_link.src = "http://127.0.0.1:8000/static/Javascript/sendcomment.js"
            document.head.appendChild(send_comment_link)
        }
        if (data["comment_rc"]){
            const render__comments = data["comment_rc"].join("\n")

            eval(render__comments)
        }

        if(data["comment_rf"]){
            const render__form = data["comment_rf"].join("\n")

            eval(render__form)

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