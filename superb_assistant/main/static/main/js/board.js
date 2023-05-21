let $btn = document.querySelector('.btn-modal');
let modal = document.querySelector('.modal');
$btn.addEventListener('click', openModal);

function openModal() {
  document.querySelector('.modal__title').textContent = 'НОВОЕ ОБЪЯВЛЕНИЕ';
  document.querySelector('.modal__btn').value = "ДОБАВИТЬ";
  document.querySelector('.modal__form').action = "/add_data";
  document.querySelector('.input__hidden').value = "";
  document.querySelector('.modal__input-name').value = '';
  document.querySelector('.modal__textarea').value = '';
  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';
  document.querySelector('.modal__btn').addEventListener('click', createCell);

  function createCell(e) {
    let name = document.querySelector('.modal__input-name').value;
    let text = document.querySelector('.modal__textarea').value;
    if (name && text) {
      notify('объявление создано')
      let cell = document.createElement('div');
      cell.classList.add("board__cell");
      let curDate = new Date();
      cell.innerHTML = `
              <div class="board__box">
                <h4 class="board__title">
                  ${name}
                </h4>
                <p class="board__date">
                ${curDate.getDay()}.${curDate.getMonth()}.${curDate.getFullYear()} ${curDate.getHours()}:${curDate.getMinutes()}
                </p>
              </div>
              <p class="board__text">
                ${text}
              </p>
              <div class="board__btns">
                <button class="mini-btn btn-change">ИЗМЕНИТЬ</button>
                <button class="mini-btn btn-cancel">
                  УДАЛИТЬ
                </button>
              </div>
      `
      cell.querySelector('.btn-change').addEventListener('click', openModalChange);
      cell.querySelector('.btn-cancel').addEventListener('click', deleteCell);
      document.querySelector('.board__container').append(cell);
    } else {
      notify('невозможно создать пустое объявление')
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
  let parent = e.target.closest('.board__cell');
  document.querySelector('.modal__title').textContent = 'ИЗМЕНИТЬ МАТЕРИАЛ';
  document.querySelector('.modal__btn').value = "ИЗМЕНИТЬ";
  document.querySelector('.modal__form').action = "contacts/edit_data";
  document.querySelector('.input__hidden').value = e.target.dataset.id;
  document.querySelector('.modal__input-name').value = parent.querySelector('.board__title').textContent.trim();
  document.querySelector('.modal__textarea').value = parent.querySelector('.board__text').textContent.trim();
  modal.style.display = 'block';
  document.querySelector('body').style.overflowY = 'hidden';


  document.querySelector('.modal__btn').addEventListener('click', changeCell);

  function changeCell(e) {
    let name = document.querySelector('.modal__input-name').value;
    let text = document.querySelector('.modal__textarea').value;
    if (name === '' || text === '') {
      notify('объявление удалено');
      parent.remove();
    } else {
      notify('объявление изменено');
      parent.querySelector('.board__title').textContent = name;
      parent.querySelector('.board__text').textContent = text;
    }
    close();
    document.querySelector('.modal__btn').removeEventListener('click', changeCell);
  }
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