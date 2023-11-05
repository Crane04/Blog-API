
        function toggleSection(sectionId) {
            const sections = document.querySelectorAll('.form-section');
            sections.forEach(section => section.classList.remove('active'));
            document.getElementById(sectionId).classList.add('active');
        }

        function numbering_posts(){
            const numbering = document.getElementsByClassName("numbering")

            for(let i=0; i < numbering.length; i++){
                numbering[i].innerText = i + 1
            }

        }
        numbering_posts()


    function deletePost(post_id) {
        if(confirm("Are you sure you want to delete this post?")){
            const apiUrl = 'http://127.0.0.1:8000/posts/api/' + post_id;
            const headers = new Headers();
            headers.append('X-CSRFToken', getCookie('csrftoken')); // Get the CSRF token from cookies

            fetch(apiUrl, {
                method: 'DELETE',
                headers: headers,
            })
                .then(response => {
                    console.log(response.ok)
                    console.log(document.getElementById("dp"+post_id).parentElement.parentElement)
                    document.getElementById("dp"+post_id).parentElement.remove()
                    numbering_posts()
                })
                .then(data => {
                    // Handle the response data

                });
        }
    }

function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}
