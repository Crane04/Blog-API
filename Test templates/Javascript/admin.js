function toggleSection(sectionId) {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
}



// Handle form submission (you'd send the data to the server)
const postForm = document.getElementById('post-form');
postForm.addEventListener('submit', (e) => {
    e.preventDefault();
    // Process and send data to the server here
});

// Function to edit a post (you would implement this functionality)
function editPost(postId) {
    // Implement the edit functionality here
}

// Function to delete a post (you would implement this functionality)
function deletePost(postId) {
    // Implement the delete functionality here
    const requestOptions = {
        method: 'DELETE',
        headers:{
            "Authorization": "Token " + api_key
        }
    };
    fetch("http://127.0.0.1:8000/posts/" + postId, requestOptions)
}