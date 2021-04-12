function initNavbar() {
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);
  if ($navbarBurgers.length > 0) {
      $navbarBurgers.forEach( el => {
      el.addEventListener('click', () => {
        const target = el.dataset.target;
        const $target = document.getElementById(target);
        el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }
}

function initModal() {
  const $modals = Array.prototype.slice.call(document.querySelectorAll('.modal'), 0);
  if ($modals.length > 0) {
    $modals.forEach(el => {
      el.querySelector('.modal-background').addEventListener('click', () => {
        el.classList.toggle('is-active');
      });

      el.querySelector('.modal-close').addEventListener('click', () => {
        el.classList.toggle('is-active');
      });
    });
  }
}

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initModal();
});