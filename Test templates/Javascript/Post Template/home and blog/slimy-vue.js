const bloggit = document.getElementById("bloggit-container")

// function processResponseData(data){
    data["posts"].forEach(function(parameter){

        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let post_id = parameter.custom_id

        let post_container = document.createElement('section')
        post_container.className = "post"

        if(image){
            console.log(1);
            post_container.innerHTML = `
            
            <div class="post-image">
                <img src="http://127.0.0.1:8000${image}" alt="${title}">
            </div>
            <div class="post-content">
                <h2>${title}</h2>
                <p>${strip_tags(body)}</p>
                <date>${convert_datetime(parameter.time)}</date>
                <div class="read-more">
                    <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
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
                    <div class="read-more">
                        <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
                    </div>
                </div>
            `
            bloggit.appendChild(post_container)
        }
    
    
    })
