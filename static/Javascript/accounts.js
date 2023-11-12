if(document.querySelector("#signup")){
    document.querySelector("#signup").addEventListener("click", function(e){
        const password = document.getElementById('password').value;
        const password2 = document.getElementById('password2').value;
        if(password === password2){
            if (password.length < 6 || !/[A-Z]/.test(password) || !/[a-z]/.test(password) || !/[^A-Za-z0-9]/.test(password)){
            e.preventDefault()
            document.querySelector('.status_post').innerText = "Password must contain atleast 6 characters, 1 upper, lowercase and a special character"
            document.querySelector('.status_post').style.display = "block"
    
            setTimeout(() => {
                
            document.querySelector('.status_post').style.display = "none"
            }, 4000);
            
            }
        }else{
            e.preventDefault()
            document.querySelector('.status_post').innerText = "Passwords don't match!"
            document.querySelector('.status_post').style.display = "block"
    
            setTimeout(() => {
                
            document.querySelector('.status_post').style.display = "none"
            }, 3000);
            }
    })
    function isStrongPassword(password) {
        // Check for a minimum length of 6 characters
        if (password.length < 6) {
            return false;
        }
    
        // Check for at least one uppercase letter
        if (!/[A-Z]/.test(password)) {
            return false;
        }
    
        // Check for at least one lowercase letter
        if (!/[a-z]/.test(password)) {
            return false;
        }
    
        // Check for at least one special character (not alphanumeric)
        if (!/[^A-Za-z0-9]/.test(password)) {
            return false;
        }
    
        // If all checks pass, the password is strong
        return true;
    }
    
}
function togglePassword(){
    var password_inputs = document.getElementsByClassName("password-input");
    for(let i =0; i<password_inputs.length; i++){
        if (password_inputs[i].type === "password") {
            password_inputs[i].type = "text";
            document.querySelector(".eye-icon").className = "fas fa-eye-slash eye-icon"
        } else {
            password_inputs[i].type = "password";
            document.querySelector(".eye-icon").className = "fas fa-eye eye-icon"
        }
    }

}
