function notify(string) {
  let notification = document.querySelector('.notification');
  notification.textContent = string;
  notification.style.transform = 'translateX(0)'
  setTimeout(() => {
    notification.style.transform = ''
  }, 2000)
}

function close() {
  document.querySelector('.modal__overlay').classList.remove('animate__fadeIn');
  document.querySelector('.modal__content').classList.remove('animate__backInDown');
  document.querySelector('.modal__overlay').classList.add('animate__fadeOut');
  document.querySelector('.modal__content').classList.add('animate__backOutUp');
  setTimeout(() => {
    modal.style.display = '';
    document.querySelector('body').style.overflowY = 'auto';
    document.querySelector('.modal__overlay').classList.remove('animate__fadeOut');
    document.querySelector('.modal__content').classList.remove('animate__backOutUp');
    document.querySelector('.modal__overlay').classList.add('animate__fadeIn');
    document.querySelector('.modal__content').classList.add('animate__backInDown');
  }, 500);
}

let $btn = document.querySelector('.btn-modal');
let modal = document.querySelector('.modal');
$btn.addEventListener('click', openModal);

function openModal() {
  document.querySelector('.modal__input-name').value = '';
  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';
  document.querySelector('.modal__btn').addEventListener('click', createLesson);

  function createLesson(e) {
    e.preventDefault();
    let name = document.querySelector('.modal__input-name').value;
    if (name) {
      notify('материал создан')
      let lesson = document.createElement('a');
      lesson.classList.add("log__link");
      lesson.href = '';
      lesson.innerHTML = name;
      document.querySelector('.log__links').append(lesson);
    } else {
      notify('невозможно создать пустой урок')
    }

    close();
    document.querySelector('.modal__btn').removeEventListener('click', createLesson);
  }
}

document.querySelector('.modal__overlay').addEventListener('click', closeModal);

function closeModal(e) {
  if (e.target.classList.contains('modal__icon')) {
    close();
  }
}