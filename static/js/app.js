// Check page theme
if (localStorage.getItem('theme') === 'dark') {
    document.body.classList.add('dark');
}

// Theme toggle
const themeToggle = document.getElementById('themeToggle');
if (themeToggle) {
    themeToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark');

        if (document.body.classList.contains('dark')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
    });
}

// Burger menu
const sidebar = document.getElementById('sidebar');
const menuToggle = document.getElementById('menuToggle');
if (menuToggle) {
    menuToggle.addEventListener('click', () => {
        sidebar.classList.toggle('open');
    });
}