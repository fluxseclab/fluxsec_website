const toggleBtn = document.getElementById('theme-toggle');
const root = document.documentElement;

function setTheme(theme) {
    if(theme === 'dark') {
        root.setAttribute('data-theme', 'dark');
        toggleBtn.textContent = '☀️';
    } else {
        root.setAttribute('data-theme', 'light');
        toggleBtn.textContent = '🌙';
    }
    localStorage.setItem('theme', theme);
}

const savedTheme = localStorage.getItem('theme');
if(savedTheme) {
    setTheme(savedTheme);
} else {
    setTheme('dark');
}

toggleBtn.addEventListener('click', () => {
    const currentTheme = root.getAttribute('data-theme');
    setTheme(currentTheme === 'dark' ? 'light' : 'dark');
});
