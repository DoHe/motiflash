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

function initNotifications() {
  const $notifications = Array.prototype.slice.call(document.querySelectorAll('.notification'), 0);
  $notifications.forEach(notification => {
    notification.querySelector('.js-delete').addEventListener('click', () => {
      notification.parentNode.removeChild(notification);
    })
  });
}

function checkNotifications() {
  fetch('/notifications')
}

function showNotification(text) {
  const template = document.createElement('template');
  template.innerHTML = `<div class="notification is-primary is-light">
    <button class="delete js-delete"></button>
    ${text}
  </div>`
  const notification = template.content.firstChild;
  notification.querySelector('.js-delete').addEventListener('click', () => {
    notification.parentNode.removeChild(notification);
  })
  const notificationArea = document.querySelector('.js-achievement');
  if (notificationArea) {
    notificationArea.appendChild(notification);
  }
}

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initModal();
    initNotifications();
    window.showNotification = showNotification;
});