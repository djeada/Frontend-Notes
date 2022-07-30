/* find all the buttons of class "tab-link" and add a click event listener to them */
const tabLinks = document.querySelectorAll('.tab-link');
tabLinks.forEach(link => {
    link.addEventListener('click', (e) => {
        e.preventDefault();

        /* hide elements of class "tab-content" */
        const tabContents = document.querySelectorAll('.tab-content');
        tabContents.forEach(content => {
            content.style.display = 'none';
        });

        /* find the tab content that corresponds to the clicked tab link */
        const tabText = e.target.innerText.replace(/\s+/g, '_');
        const tabContent = document.querySelector(`#${tabText}`);
        tabContent.style.display = 'block';
    });
}
);