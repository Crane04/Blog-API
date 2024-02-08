def classic(token):

    classic_txt = """
            fetch(`http://127.0.0.1:8000/v2/all-posts`,
        {
        "headers": {
        """
    classic_txt += f"""
        "Authorization": "Token {token}"
        """
    
    classic_txt+="""
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
    bloggit_data = data
        
    if(data[type] === "all" && data["detail"] === "okay"){
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
            bloggit_container.innerHTML += `<img src="http://127.0.0.1:8000${post.image }" class="img-fluid" alt="Image for the post">`
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

        """
    
    return classic_txt