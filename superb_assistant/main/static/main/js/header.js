let header = document.querySelector('.header__container');

let buffer = document.querySelector('.header__selected')
header.addEventListener('mouseover', (e) => {
  if (!e.target.classList.contains('header__selected') && !e.target.classList.contains('header__container')) {
    buffer.classList.remove('header__selected');
    e.target.classList.add('header__selected');
  }
})

header.addEventListener('mouseout', () => {
  document.querySelector('.header__selected').classList.remove('header__selected');
  buffer.classList.add('header__selected');
})