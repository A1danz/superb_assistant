function notify(string) {
  let notification = document.querySelector('.notification');
  notification.textContent = string;
  notification.style.transform = 'translateX(0)'
  setTimeout(() => {
    notification.style.transform = ''
  }, 2000)
}


let $btn = document.querySelector('.btn-modal');
let modal = document.querySelector('.modal');
$btn.addEventListener('click', openModal);

function openModal() {
  document.querySelector('.modal__title').textContent = 'НОВЫЙ КОНТАКТ';
  document.querySelector('.modal__btn').value = "ДОБАВИТЬ";
  document.querySelector('.modal__form').action = "/add_post";
  document.querySelector('.modal__input-name').value = '';
  document.querySelector('.modal__lesson').value = '';
  document.querySelector('.modal__contact').value = '';

  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';
  document.querySelector('.modal__btn').addEventListener('click', createCell);

  function createCell(e) {
    let name = document.querySelector('.modal__input-name').value;
    let lesson = document.querySelector('.modal__lesson').value;
    let contact = document.querySelector('.modal__contact').value;
    if (name && lesson && contact) {
      notify('новый контакт добавлен');
      let cell = document.createElement('div');
      cell.classList.add("contact__cell");

      cell.innerHTML = `
                <div class="contact__title">${name}</div>
              <div class="contact__info">
                <div class="contact__text">${lesson}</div>
                <div class="contact__text contact__randomname">${contact}
                </div>
              </div>
              <div class="contact__btns">
                <button class="mini-btn btn-change">ИЗМЕНИТЬ</button>
                <button class="mini-btn btn-cancel">УДАЛИТЬ</button>
              </div>
      `
      let information = cell.querySelectorAll('.contact__text')[1]
      cell.querySelector('.btn-change').addEventListener('click', openModalChange);
      cell.querySelector('.btn-cancel').addEventListener('click', deleteCell);
      document.querySelector('.contact__container').append(cell);
    } else {
      notify('нельзя создать пустой контакт')
    }

    close();
    document.querySelector('.modal__btn').removeEventListener('click', createCell);
  }
}

document.querySelector('.modal__overlay').addEventListener('click', closeModal);

function closeModal(e) {
  if (e.target.classList.contains('modal__icon')) {
    close();
  }
}

let btnChange = document.querySelectorAll('.btn-change')
btnChange.forEach((btn) => {
  btn.addEventListener('click', openModalChange);
})

function openModalChange(e) {
  let parent = e.target.closest('.contact__cell');
  document.querySelector('.modal__title').textContent = 'ИЗМЕНИТЬ КОНТАКТ';
  document.querySelector('.modal__btn').value = "ИЗМЕНИТЬ";
  document.querySelector('.modal__form').action = "/edit_post";
  document.querySelector('.modal__input-name').value = parent.querySelector('.contact__title').textContent.trim();
  document.querySelector('.modal__lesson').value = parent.querySelector('.contact__text').textContent.trim();
  document.querySelector('.modal__contact').value = parent.querySelector('.contact__randomname').textContent.trim();

  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';

  document.querySelector('.modal__btn').addEventListener('click', changeCell);

  function changeCell(e) {
    let name = document.querySelector('.modal__input-name').value;
    let lesson = document.querySelector('.modal__lesson').value;
    let contact = document.querySelector('.modal__contact').value;
    if (name === '' || lesson === '' || contact === '') {
      notify('контакт удален');
      parent.remove();
    } else {
      notify('контакт изменен');
      parent.querySelector('.contact__title').textContent = name;
      parent.querySelector('.contact__text').textContent = lesson;
      let information = parent.querySelectorAll('.contact__text')[1];
      information.innerHTML = `${contact}`

    }
    close();
    document.querySelector('.modal__btn').removeEventListener('click', changeCell);
  }
}

let btnCancel = document.querySelectorAll('.btn-cancel')
btnCancel.forEach((btn) => {
  btn.addEventListener('click', deleteCell);
})

function deleteCell(e) {
  notify('контакт удален');
  let parent = e.target.closest('.contact__cell');
  parent.remove();
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