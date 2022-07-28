const navbarToggle = document.getElementById('navbarToggle');
const navbarLinks = document.getElementById("navbar-links");

navbarToggle.addEventListener('click', function() {
    /*When the user presses the button, toggle between 
    showing and hiding the navigation menu links. */
    navbarLinks.stlye.display = 'block' == navbarLinks.style.display ? 'none' : 'block';
});