const bloggit = document.getElementById("bloggit-container")
bloggit.className = "blog-container-1"


// function processResponseData(data){
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
                <div class="read-more">
                    <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
                </div>
            </div>
            <div class="post-image">
                <img src="https://bloggit.pythonanywhere.com${image}" alt="${title}">
            </div>
            <span>${comments}</span>
            `
            bloggit.appendChild(post_container)
        }else{
            post_container.innerHTML += `
            <div class="post-content">
                <h2>${title}</h2>
                <p>${strip_tags(body)}</p>
                <date>${convert_datetime(parameter.time)}</date>
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
