// Enhanced JavaScript for Django Blog - Form validation and interactions
document.addEventListener('DOMContentLoaded', function() {
    console.log('Blog page loaded with enhanced functionality');
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize password strength meter
    initializePasswordStrengthMeter();
    
    // Initialize form animations
    initializeFormAnimations();
    
    // Initialize loading states
    initializeLoadingStates();
});

// Form validation functionality
function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], textarea');
        
        inputs.forEach(input => {
            // Real-time validation
            input.addEventListener('blur', function() {
                validateField(this);
            });
            
            input.addEventListener('input', function() {
                clearFieldError(this);
            });
        });
        
        // Form submission validation
        form.addEventListener('submit', function(e) {
            if (!validateForm(this)) {
                e.preventDefault();
                showFormError('Please correct the errors before submitting.');
            }
        });
    });
}

// Validate individual field
function validateField(field) {
    const value = field.value.trim();
    const fieldName = field.name;
    let isValid = true;
    let errorMessage = '';
    
    // Required field validation
    if (field.hasAttribute('required') && !value) {
        isValid = false;
        errorMessage = 'This field is required.';
    }
    
    // Email validation
    if (fieldName === 'email' && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(value)) {
            isValid = false;
            errorMessage = 'Please enter a valid email address.';
        }
    }
    
    // Username validation
    if (fieldName === 'username' && value) {
        if (value.length < 3) {
            isValid = false;
            errorMessage = 'Username must be at least 3 characters long.';
        } else if (!/^[a-zA-Z0-9_]+$/.test(value)) {
            isValid = false;
            errorMessage = 'Username can only contain letters, numbers, and underscores.';
        }
    }
    
    // Password validation
    if (fieldName === 'password' && value) {
        if (value.length < 8) {
            isValid = false;
            errorMessage = 'Password must be at least 8 characters long.';
        } else if (!/(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/.test(value)) {
            isValid = false;
            errorMessage = 'Password must contain at least one uppercase letter, one lowercase letter, and one number.';
        }
    }
    
    // Password confirmation validation
    if (fieldName === 'password2' && value) {
        const passwordField = document.querySelector('input[name="password"]');
        if (passwordField && value !== passwordField.value) {
            isValid = false;
            errorMessage = 'Passwords do not match.';
        }
    }
    
    // Bio validation
    if (fieldName === 'bio' && value) {
        if (value.length > 500) {
            isValid = false;
            errorMessage = 'Bio must be 500 characters or less.';
        }
    }
    
    if (!isValid) {
        showFieldError(field, errorMessage);
    } else {
        clearFieldError(field);
    }
    
    return isValid;
}

// Show field error
function showFieldError(field, message) {
    clearFieldError(field);
    
    field.classList.add('error');
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
    
    field.parentNode.appendChild(errorDiv);
}

// Clear field error
function clearFieldError(field) {
    field.classList.remove('error');
    
    const errorDiv = field.parentNode.querySelector('.error-message');
    if (errorDiv) {
        errorDiv.remove();
    }
}

// Validate entire form
function validateForm(form) {
    const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], textarea');
    let isValid = true;
    
    inputs.forEach(input => {
        if (!validateField(input)) {
            isValid = false;
        }
    });
    
    return isValid;
}

// Show form error message
function showFormError(message) {
    const existingError = document.querySelector('.message.error');
    if (existingError) {
        existingError.remove();
    }
    
    const errorDiv = document.createElement('div');
    errorDiv.className = 'message error';
    errorDiv.textContent = message;
    
    const form = document.querySelector('form');
    form.insertBefore(errorDiv, form.firstChild);
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        errorDiv.remove();
    }, 5000);
}

// Password strength meter
function initializePasswordStrengthMeter() {
    const passwordField = document.querySelector('input[name="password"]');
    if (!passwordField) return;
    
    // Create strength meter
    const strengthMeter = document.createElement('div');
    strengthMeter.className = 'password-strength';
    strengthMeter.innerHTML = `
        <div class="strength-bar">
            <div class="strength-fill"></div>
        </div>
        <div class="strength-text"></div>
    `;
    
    passwordField.parentNode.appendChild(strengthMeter);
    
    passwordField.addEventListener('input', function() {
        const strength = calculatePasswordStrength(this.value);
        updateStrengthMeter(strengthMeter, strength);
    });
}

// Calculate password strength
function calculatePasswordStrength(password) {
    let score = 0;
    
    if (password.length >= 8) score += 1;
    if (password.match(/[a-z]/)) score += 1;
    if (password.match(/[A-Z]/)) score += 1;
    if (password.match(/[0-9]/)) score += 1;
    if (password.match(/[^a-zA-Z0-9]/)) score += 1;
    
    return Math.min(score, 5);
}

// Update strength meter display
function updateStrengthMeter(meter, strength) {
    const fill = meter.querySelector('.strength-fill');
    const text = meter.querySelector('.strength-text');
    
    const percentages = [0, 20, 40, 60, 80, 100];
    const colors = ['#e74c3c', '#e67e22', '#f39c12', '#f1c40f', '#2ecc71', '#27ae60'];
    const labels = ['', 'Very Weak', 'Weak', 'Fair', 'Good', 'Strong'];
    
    fill.style.width = percentages[strength] + '%';
    fill.style.backgroundColor = colors[strength];
    text.textContent = labels[strength];
    text.style.color = colors[strength];
}

// Form animations
function initializeFormAnimations() {
    const formContainer = document.querySelector('.form-container');
    if (formContainer) {
        // Add entrance animation
        formContainer.style.opacity = '0';
        formContainer.style.transform = 'translateY(30px)';
        
        setTimeout(() => {
            formContainer.style.transition = 'all 0.5s ease-out';
            formContainer.style.opacity = '1';
            formContainer.style.transform = 'translateY(0)';
        }, 100);
    }
}

// Loading states
function initializeLoadingStates() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="loading"></span> Processing...';
            }
        });
    });
}

// Utility function to show success message
function showSuccessMessage(message) {
    const existingMessage = document.querySelector('.message.success');
    if (existingMessage) {
        existingMessage.remove();
    }
    
    const successDiv = document.createElement('div');
    successDiv.className = 'message success';
    successDiv.textContent = message;
    
    const form = document.querySelector('form');
    if (form) {
        form.insertBefore(successDiv, form.firstChild);
    }
    
    // Auto-remove after 5 seconds
    setTimeout(() => {
        successDiv.remove();
    }, 5000);
}

// Add CSS for password strength meter
const style = document.createElement('style');
style.textContent = `
    .password-strength {
        margin-top: 10px;
    }
    
    .strength-bar {
        width: 100%;
        height: 4px;
        background-color: #e1e5e9;
        border-radius: 2px;
        overflow: hidden;
    }
    
    .strength-fill {
        height: 100%;
        width: 0%;
        transition: all 0.3s ease;
    }
    
    .strength-text {
        font-size: 12px;
        margin-top: 5px;
        font-weight: 500;
    }
`;
document.head.appendChild(style);