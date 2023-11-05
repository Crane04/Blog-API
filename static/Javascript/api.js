$(document).ready(function () {
    const active_link = $(".nav-link")[1]
    active_link.className = "nav-link active"

    $("#copyApiKey").click(function (e) {
        e.preventDefault()
        var copyText = document.getElementById("apiKey");
        
        copyText.select();
        copyText.setSelectionRange(0, 99999); // For mobile devices
        
        // Copy the text inside the text field
        navigator.clipboard.writeText(copyText.value);
        document.querySelector('.status_post').innerText = "Copied!"

        document.querySelector('.status_post').style.display = "block"

        setTimeout(() => {
            
        document.querySelector('.status_post').style.display = "none"
        }, 4000);
    });
});
