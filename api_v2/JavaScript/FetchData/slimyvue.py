def slimy_vue(token):

    slimy_vue_txt = """
            fetch(`http://127.0.0.1:8000/v2/main?location=${current_url}&id=${post_id}`,
        {
        "headers": {
        """
    slimy_vue_txt += f"""
        "Authorization": "Token {token}"
        """
    
    slimy_vue_txt+="""
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
    if(data["type"] === "all" && data["detail"] === "okay"){
        data["posts"].forEach(function(parameter){

                let title = parameter.title
                let body = parameter.body
                let image = parameter.image
                let post_id = parameter.custom_id
                let comments = parameter.comment_count

                let post_container = document.createElement('section')
                post_container.className = "post"

                if(image){

                    post_container.innerHTML = `
                    
                    <div class="post-image">
                        <img src="http://127.0.0.1:8000${image}" alt="${title}">
                    </div>
                    <div class="post-content">
                        <h2>${title}</h2>
                        <p>${strip_tags(body)}</p>
                        <date>${convert_datetime(parameter.time)}</date>
                        <span>${comments} Comments</span>
                        <div class="read-more">
                            <a href="${data["ind"]}?id=${post_id}">Read More</a>
                        </div>
                    </div>
                    `
                    bloggit.appendChild(post_container)
                }else{
                    post_container.innerHTML = `
                
                        <div class="post-image">
                        </div>
                        <div class="post-content">
                            <h2>${title}</h2>
                            <p>${strip_tags(body)}</p>
                            <span>${comments} Comments</span>
                            <div class="read-more">
                                <a href="${data["ind"]}?id=${post_id}" >Read More</a>
                            </div>
                        </div>
                    `
                    bloggit.appendChild(post_container)
                }
            }
        )}else if(data["type"] == "one"){
            bloggit.className = "container mt-4"
            post = data["post"]

            bloggit.innerHTML+=`<h1> ${post.title}</h1>`
            if(post.image){
                bloggit.innerHTML += `<img src="http://127.0.0.1:8000${post.image }" class="img-fluid" alt="Image for the post">`
            }
            bloggit.innerHTML += `
                <p>${convert_datetime(post.time)}</p>
                <div class="mt-4">
                ${post.body}
                </div>`
        }
        try{
            bloggit_preloader.style.display = "none"
        }catch(error){
        
        }
    })

    .catch((error) =>{
        console.log(error)
    })

        """
    
    return slimy_vue_txt