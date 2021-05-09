function initAddModal() {
    document.querySelector('.js-add-course').addEventListener('click', () => {
        document.querySelector('.js-add-modal').classList.toggle('is-active');
    });
}

function initAddModalTabs() {
    const importTab = document.querySelector('.js-import-tab');
    const createTab = document.querySelector('.js-create-tab');
    const importField = document.querySelector('#id_import_text').closest('.field');
    importField.classList.add('is-hidden');
    
    importTab.addEventListener('click', () => {
        importTab.classList.add('is-active');
        createTab.classList.remove('is-active');
        importField.classList.remove('is-hidden');
    });
    createTab.addEventListener('click', () => {
        createTab.classList.add('is-active');
        importTab.classList.remove('is-active');
        importField.classList.add('is-hidden');
    });
}

document.addEventListener('DOMContentLoaded', () => {
    initAddModal();
    initAddModalTabs();
});