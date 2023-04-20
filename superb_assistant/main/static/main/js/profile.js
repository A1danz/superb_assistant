let pass = document.querySelectorAll('.password');
pass.forEach((ps) => {
  ps.addEventListener('input', (e) => {
    let eyeCurrent = e.target.nextSibling.nextSibling;
    if (e.target.value) {
      eyeCurrent.style.display = 'block';
    } else {
      eyeCurrent.style.display = '';
    }
  })
})

let eye = document.querySelectorAll('.sign__eye');
eye.forEach((ee) => {
  ee.addEventListener('click', (event) => {
    let password = event.target.offsetParent.querySelector('.password');
    if (password.type === 'password') {
      password.type = 'text';
      event.target.classList.remove('uil-eye');
      event.target.classList.add('uil-eye-slash');
    } else {
      password.type = 'password';
      event.target.classList.remove('uil-eye-slash');
      event.target.classList.add('uil-eye');
    }
  })
})


let persons = document.querySelectorAll('.profile__person');
persons.forEach((pers) => {
  pers.addEventListener('mouseover', () => {
    pers.querySelector('.profile__person-btn').classList.add('profile__person-btn--show');
  } )
})
persons.forEach((pers) => {
  pers.addEventListener('mouseout', () => {
    pers.querySelector('.profile__person-btn').classList.remove('profile__person-btn--show');
  } )
})