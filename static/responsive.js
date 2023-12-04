document.addEventListener('DOMContentLoaded', function () {
    var menuIcon = document.getElementById('menu-icon');
    var menuLateral = document.getElementById('menu-lateral');

    menuIcon.addEventListener('click', function () {
        menuLateral.style.width = menuLateral.style.width === '200px' ? '0' : '200px';
    });
});
