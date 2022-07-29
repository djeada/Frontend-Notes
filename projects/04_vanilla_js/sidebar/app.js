/*find element of class "sidebar"*/
const sidebar = document.querySelector(".sidebar");
const sidebarToggle = document.getElementById("sidebarToggle");
const sidebarLinks = document.getElementById("sidebar-links");
const mainContent = document.getElementById("main");

sidebarToggle.addEventListener('click', function() {
    const minWidth = '60px';
    const normalWidth = '150px';
    if (sidebar.style.width === minWidth) {
        sidebar.style.width = normalWidth;
        mainContent.style.marginLeft = normalWidth;
        sidebarLinks.style.opacity = 1;
        sidebarLinks.style.visibility = 'visible';
    } else {
        sidebar.style.width = minWidth;
        mainContent.style.marginLeft = minWidth;
        sidebarLinks.style.opacity = 0;
        sidebarLinks.style.visibility = 'hidden';
    }
});