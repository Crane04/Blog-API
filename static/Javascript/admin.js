const delpost = document.querySelectorAll(".delpostnow")
const time_post = document.getElementsByClassName("time-of-post")


function convert_datetime(param){
    const originalDate = new Date(param);
    const userTimeZone = Intl.DateTimeFormat().resolvedOptions().timeZone;
    
    const options = {
      timeZone: userTimeZone,
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: 'numeric',
      minute: 'numeric',
      second: 'numeric',
      hour12: false
    };
    
    const convertedDate = new Intl.DateTimeFormat('en-US', options).format(originalDate);
    return convertedDate
}

if(time_post){
    for(let i = 0; i < time_post.length; i++){
        try {
            const c_dt = convert_datetime(time_post[i].innerText)
            time_post[i].innerText = c_dt
        } catch (error) {
            
        }

    }
}
function toggleSection(sectionId) {
    const sections = document.querySelectorAll('.form-section');
    sections.forEach(section => section.classList.remove('active'));
    document.getElementById(sectionId).classList.add('active');
}
for(let i = 0; i < delpost.length; i++){
    delpost[i].addEventListener("click", function(e){
        if(confirm("Are you sure you want to delete")){
            
        }else{
            e.preventDefault()
        }
    })
}
function numbering_posts(){
    const numbering = document.getElementsByClassName("numbering")

    for(let i=0; i < numbering.length; i++){
        numbering[i].innerText = i + 1
    }

}
numbering_posts()

function getCookie(name) {
const value = `; ${document.cookie}`;
const parts = value.split(`; ${name}=`);
if (parts.length === 2) return parts.pop().split(';').shift();
}

document.getElementById("make-post").addEventListener("click", function(e){
document.querySelector("#current-time").value = new Date()
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