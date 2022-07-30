const body = document.body;
const darkModeToggle = document.getElementById("darkModeToggle");

darkModeToggle.addEventListener('click', function() {
    body.classList.toggle("dark-mode");
});