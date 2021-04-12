function init() {
    document.querySelector('.js-add-course').addEventListener('click', () => {
        document.querySelector('.js-add-modal').classList.toggle('is-active');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    init();
});