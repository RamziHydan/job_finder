document.addEventListener('DOMContentLoaded', function() {
    const passwordToggle = document.querySelectorAll('.password-toggle');
    passwordToggle.forEach(function(input) {
      const toggleButton = document.createElement('span');
      toggleButton.className = 'password-toggle-button';
      toggleButton.innerHTML = 'Show';
  
      toggleButton.addEventListener('click', function() {
        if (input.type === 'password') {
          input.type = 'text';
          toggleButton.innerHTML = 'Hide';
        } else {
          input.type = 'password';
          toggleButton.innerHTML = 'Show';
        }
      });
  
      input.after(toggleButton);
    });
  });