const bloggit_header = document.getElementById("bloggit-header")
const bloggit_preloader = document.getElementById("bloggit-preloader")
const bloggit = document.getElementById("bloggit-container")

let bloggit_data = null

bloggit_header.innerHTML = `
<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Craennie</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="na
vbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
     <div class="collapse navbar-collapse" id="navbarNav">
         <ul class="navbar-nav ml-auto">


                <li class="nav-item">
                    <a class="nav-link" href="/home">Home</a>
                 </li>
        </ul>
    </div>
</nav>`


bloggit_preloader.innerHTML = ` <div id="preloader" class="spinner-border text-primary" role="status">
        <span class="sr-only">Loading...</span>
    </div>`

    function convert_datetime(param){
    // const dateComponents = param.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);

    // const year = parseInt(dateComponents[1]);
    // const month = parseInt(dateComponents[2]) - 1;
    // const day = parseInt(dateComponents[3]);

    // // Create a JavaScript Date object without considering the timezone
    // const date = new Date(year, month, day);

    // const time = new Date(param);

    // // Get the hours, minutes, and seconds
    // const hours = time.getHours();
    // const minutes = time.getMinutes();
    // const seconds = time.getSeconds();

    // let __time__ = `${hours}:${minutes}:${seconds}`;

    // Format the date as "Month Day, Year"
    return param
    return   date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' }).toString() + " ;" + __time__;
    }

    function strip_tags(param){
        let post_body = document.createElement("p")
        post_body.innerHTML = param
        let elements_to_remove = post_body.querySelectorAll("table", "img", "iframe", "audio", "video", "picture",
"figure", "canvas")

        elements_to_remove.forEach(function(element) {
            element.remove();
        });
        var words = post_body.innerText.split(/\s+/);

        // Select the first 120 words
        return words.slice(0, 30).join(' ');
    }

fetch(`http://127.0.0.1:8000/v2/main`,
    {
    "headers": {

    "Authorization": "Token a954b21e51c809b72b5e68d5a12717ef4e2c5d3a"

}
    }
)
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
    console.log(data)
    bloggit_data = data
if(data["type"] === "all" && data["detail"] === "okay"){
data["posts"].forEach(function(parameter){

    let title = parameter.title
    let body = parameter.body
    let image = parameter.image
    let post_id = parameter.custom_id
    let comments = parameter.comment_count

    let post_container = document.createElement('section')
    post_container.className = "blog-post"

    if(image){

        post_container.innerHTML += `
        <div class="post-content">
            <h2>${title}</h2>
            <p>${strip_tags(body)}</p>
            <date>${convert_datetime(parameter.time)}</date>
            <div>${comments} Comments</div>
            <div class="read-more">
                <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
            </div>
        </div>
        <div class="post-image">
            <img src="http://127.0.0.1:8000${image}" alt="${title}">
        </div>
        `
        bloggit.appendChild(post_container)
    }else{
        post_container.innerHTML += `
        <div class="post-content">
            <h2>${title}</h2>
            <p>${strip_tags(body)}</p>
            <date>${convert_datetime(parameter.time)}</date>
            <div>${comments} Comments</div>
            <div class="read-more">
                <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
            </div>
        </div>
            <div class="post-image">

            </div>
        `
        bloggit.appendChild(post_container)
    }

})
}else if(data["type"] == "one"){
    bloggit_container.className = "container mt-4"
    post = data["post"]

    bloggit_container.innerHTML+=`<h1> ${post.title}</h1>`
    if(post.image){
        bloggit_container.innerHTML += `<img src="http://127.0.0.1:8000${post.image }" class="img-fluid" alt="Imag
e for the post">`
    }
    bloggit_container.innerHTML += `
        <p>${convert_datetime(post.time)}</p>
        <div class="mt-4">
        ${post.body}
        </div>`
}
})

.catch((error) =>{
    console.log(error)
})

