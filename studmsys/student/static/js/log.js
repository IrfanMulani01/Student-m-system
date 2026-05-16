function togglePassword() {
        const passwordField = document.querySelector('input[type="password"]') || 
                             document.querySelector('input[name="password"]');
        const eyeIcon = document.getElementById('eye-icon');
        
        if (passwordField.type === "password") {
            passwordField.type = "text";
            eyeIcon.classList.replace('fa-eye', 'fa-eye-slash');
        } else {
            passwordField.type = "password";
            eyeIcon.classList.replace('fa-eye-slash', 'fa-eye');
        }
    }

    // Auto focus on username field
    window.onload = () => {
        const usernameField = document.querySelector('input[name="username"]') || 
                             document.querySelector('input[type="text"]');
        if (usernameField) usernameField.focus();
    }