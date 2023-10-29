const blogit = document.getElementById("blogit-container")

// Create a new link element


function processResponseData(data){
    data["posts"].forEach(function(parameter){
        const dateComponents = parameter.time.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);

        const year = parseInt(dateComponents[1]);
        const month = parseInt(dateComponents[2]) - 1;
        const day = parseInt(dateComponents[3]);
    
        // Create a JavaScript Date object without considering the timezone
        const date = new Date(year, month, day);
    
        // Format the date as "Month Day, Year"
        const formattedDate = date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let post_id = parameter.custom_id

        let post_container = document.createElement('section')
        post_container.className = "post"
        // Create a new script element
        if(image){
            console.log(1);
            post_container.innerHTML = `
        
            <div class="post-image">
                <img src="http://127.0.0.1:8000${image}" alt="${title}">
            </div>
            <div class="post-content">
                <h2>${title}</h2>
                <p>${body}</p>
                <div class="read-more">
                    <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
                </div>
            </div>
            `
            blogit.appendChild(post_container)
        }else{
            post_container.innerHTML = `
        
                <div class="post-image">
                </div>
                <div class="post-content">
                    <h2>${title}</h2>
                    <p>${body}</p>
                    <div class="read-more">
                        <a href="${data["individual_page"]}?id=${post_id}">Read More</a>
                    </div>
                </div>
            `
            blogit.appendChild(post_container)
        }
    
        // loadPosts(data)
    })

    
    
    
}
