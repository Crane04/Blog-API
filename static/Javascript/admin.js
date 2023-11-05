function toggleSection(sectionId) {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
}
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

function editPost(id){
location
}

function getCookie(name) {
const value = `; ${document.cookie}`;
const parts = value.split(`; ${name}=`);
if (parts.length === 2) return parts.pop().split(';').shift();
}

document.getElementById("make-post").addEventListener("click", function(e){

// Function to check if Summernote is empty
function isSummernoteEmpty() {
var content = $('#content').summernote('code').trim();
return content === '' || content === '<p><br></p>';
}

if (isSummernoteEmpty()) {
    e.preventDefault()
    document.querySelector('.status_post').innerText = "Content field can't be empty!"
    document.querySelector('.status_post').style.display = "block"

    setTimeout(() => {
        
    document.querySelector('.status_post').style.display = "none"
    }, 3000);
} 
})