const blogit = document.getElementById("blogit-container")
fetch(`http://127.0.0.1:8000/posts/api/${api_key}?url=${window.location.href}`)
.then((response) => {
    if (response.status === 200) { // Replace with the expected status code
        return response.json(); // If expecting JSON response
    } else {
        throw new Error(`Couldn't fetch your data: ${response.status}`);
    }
})
.then((data) => {
    console.log('Your posts have been loaded');
    console.log('Response data:', data);


    data["posts"].forEach(function(parameter){
        let title = parameter.title
        let body = parameter.body
        let image = parameter.image
        let time = String(parameter.time)
        let post_id = parameter.custom_id

        
        const dateComponents = time.match(/(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/);


        const year = parseInt(dateComponents[1]);
        const month = parseInt(dateComponents[2]) - 1;
        const day = parseInt(dateComponents[3]);

        // Create a JavaScript Date object without considering the timezone
        const date = new Date(year, month, day);

        // Format the date as "Month Day, Year"
        const formattedDate = date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
        

        let post_container = document.createElement('section')


        post_container.className = "post"
        
        if(image){
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
        }

        blogit.appendChild(post_container)
    })

    
})
.catch((error) => {
    console.error(error);
});
