let signin = document.querySelector('.sign__link-in');
let signup = document.querySelector('.sign__link-up');


let signDecor = document.querySelector('.sign__decor');

signin.addEventListener('mouseover', () => {
  signin.style.color = '#52057B';
  signup.style.color = '#BC6FF1';
  signDecor.style.transform = 'translateX(0)';
});

signin.addEventListener('mouseout', () => {
  signin.style.color = '';
  signup.style.color = '';
  signDecor.style.transform = '';
});


signup.addEventListener('mouseover', () => {
  signin.style.color = '#BC6FF1';
  signup.style.color = '#52057B';
  signDecor.style.transform = 'translateX(100%)';
});

signup.addEventListener('mouseout', () => {
  signin.style.color = '';
  signup.style.color = '';
  signDecor.style.transform = '';
});


let password = document.querySelector('.password');
let eye = document.querySelector('.sign__eye');
password.addEventListener('input', (e) => {
  if (password.value) {
    eye.style.display = 'block';
  } else {
    eye.style.display = '';
  }
})

eye.addEventListener('click', () => {
  if (password.type === 'password') {
    password.type = 'text';
    eye.classList.remove('uil-eye');
    eye.classList.add('uil-eye-slash');
  } else {
    password.type = 'password';
    eye.classList.remove('uil-eye-slash');
    eye.classList.add('uil-eye');
  }
})