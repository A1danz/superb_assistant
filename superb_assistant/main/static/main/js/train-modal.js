let $btn = document.querySelector('.btn-modal');
let modal = document.querySelector('.modal');
$btn.addEventListener('click', openModal);

function openModal() {
  document.querySelector('.modal__title').textContent = 'НОВЫЙ МАТЕРИАЛ';
  document.querySelector('.modal__btn').value = "ДОБАВИТЬ";
  document.querySelector('.modal__input-name').value = '';
  document.querySelector('.modal__input-link').value = '';
  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';
  document.querySelector('.modal__btn').addEventListener('click', createCell);

  function createCell(e) {
    e.preventDefault();
    let link = document.querySelector('.modal__input-link').value;
    let name = document.querySelector('.modal__input-name').value;
    if (link && name) {
      notify('материал создан')
      let cell = document.createElement('div');
      cell.classList.add("train-material__cell");

      cell.innerHTML = `
                <h4 class="train-material__title">
                  ${name}
                </h4>
                <a class="train-material__link" href="https://${link}">${link}</a>
                <div class="train-material__btns">
                  <button class="mini-btn btn-change">ИЗМЕНИТЬ</button>
                  <button class="mini-btn btn-cancel">
                    УДАЛИТЬ
                  </button>
                </div>
      `
      cell.querySelector('.btn-change').addEventListener('click', openModalChange);
      cell.querySelector('.btn-cancel').addEventListener('click', deleteCell);
      document.querySelector('.train-material__container').append(cell);
    } else {
      notify('невозможно создать пустой материал')
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
  let parent = e.target.closest('.train-material__cell');
  document.querySelector('.modal__title').textContent = 'ИЗМЕНИТЬ МАТЕРИАЛ';
  document.querySelector('.modal__btn').value = "ИЗМЕНИТЬ";
  document.querySelector('.modal__input-name').value = parent.querySelector('.train-material__title').textContent.trim();
  document.querySelector('.modal__input-link').value = parent.querySelector('.train-material__link').textContent.trim();
  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';

  document.querySelector('.modal__btn').addEventListener('click', changeCell);

  function changeCell(e) {
    e.preventDefault();
    let name = document.querySelector('.modal__input-name').value;
    let link = document.querySelector('.modal__input-link').value;
    if (name === '' || link === '') {
      notify('материал удален');
      parent.remove();
    } else {
      notify('материал изменен');
      parent.querySelector('.train-material__title').textContent = name;
      parent.querySelector('.train-material__link').textContent = link;
      parent.querySelector('.train-material__link').href = 'https://' + link;
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
  let parent = e.target.closest('.train-material__cell');
  notify('материал удален');
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


function notify(string) {
  let notification = document.querySelector('.notification');
  notification.textContent = string;
  notification.style.transform = 'translateX(0)'
  setTimeout(() => {
    notification.style.transform = ''
  }, 2000)
}