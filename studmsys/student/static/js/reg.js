// Add beautiful styling to all form inputs
    window.onload = function() {
        const inputs = document.querySelectorAll('input');
        inputs.forEach(input => {
            if (input.type !== 'hidden') {
                input.className += " form-input w-full px-5 py-4 border border-gray-300 rounded-2xl focus:outline-none text-gray-800";
            }
        });

        // Special handling for password fields
        const passwordFields = document.querySelectorAll('input[type="password"]');
        passwordFields.forEach((field, index) => {
            const wrapper = document.createElement('div');
            wrapper.className = "relative";
            field.parentNode.insertBefore(wrapper, field);
            wrapper.appendChild(field);

            if (index === 0 || index === 1) {
                const toggleBtn = document.createElement('button');
                toggleBtn.type = "button";
                toggleBtn.innerHTML = '<i class="fas fa-eye"></i>';
                toggleBtn.className = "absolute right-5 top-1/2 -translate-y-1/2 text-gray-400 hover:text-gray-600";
                toggleBtn.onclick = () => togglePassword(field, toggleBtn);
                wrapper.appendChild(toggleBtn);
            }
        });
    };

    function togglePassword(field, btn) {
        const icon = btn.querySelector('i');
        if (field.type === "password") {
            field.type = "text";
            icon.classList.replace('fa-eye', 'fa-eye-slash');
        } else {
            field.type = "password";
            icon.classList.replace('fa-eye-slash', 'fa-eye');
        }
    }