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

async function checkNotifications() {
  const response =  await fetch('/notifications');
  let notifications = [];
  try {
    notifications = await response.json();
  } catch (error) {
    return;
  }
  notifications.forEach(
    n => showNotification(n)
  );
}

function showNotification({ title, text, id }) {
  const template = document.createElement('template');
  template.innerHTML = `<article class="message is-primary">
    <div class="message-header">
      <p>${title}</p>
      <button class="delete js-delete"></button>
    </div>
    <div class="message-body">
      ${text}
    </div>
  </article>`
  const $notification = template.content.firstChild;
  $notification.querySelector('.js-delete').addEventListener('click', () => {
    $notification.parentNode.removeChild($notification);
    await fetch('/notifications'); // TODO: mark read
  })
  const notificationArea = document.querySelector('.js-achievement');
  if (notificationArea) {
    notificationArea.appendChild($notification);
  }
}

document.addEventListener('DOMContentLoaded', () => {
    initNavbar();
    initModal();
    initNotifications();
    window.showNotification = showNotification;
    checkNotifications();
});