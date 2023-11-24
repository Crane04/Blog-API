const comment_container = document.getElementById("bloggit-comment-container")
comment_container.classList += "container mt4"
if (comment_container){
    comment_container.innerHTML = `<h2>Comments</h2>`
    if(data["comments"] != [] || data["comments"]){
        data["comments"].forEach(function(parameter){
            let name = parameter.name
            let comment = parameter.comment
            let time = convert_datetime(parameter.time) 

            comment_container.innerHTML += `
            <!-- Comments Display -->
            <div id="comments" class="mt-4">
                <!-- Comments will be displayed here -->
                <div class="card mb-3">
                    <div class="card-body">
                        <h3 class="card-title">${name}</h3>
                        <time>${time}</time>
                        <article class="card-text">${comment}</article>
                    </div>
                </div>
            </div>

            `
        })
    }
}
