const bloggit_container = document.getElementById("bloggit-container");
bloggit_container.className = "container mt-4"
post = data["post"][0]

bloggit_container.innerHTML+=`<h1> ${post.title}</h1>`
if(post.image){
    bloggit_container.innerHTML += `<img src="http://127.0.0.1:8000${post.image }" class="img-fluid" alt="Image for the post">`
}
bloggit_container.innerHTML += `
    <p>${convert_datetime(post.time)}</p>
    <div class="mt-4">
    ${post.body}
    </div>
`