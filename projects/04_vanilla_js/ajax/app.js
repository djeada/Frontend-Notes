document.getElementById('fetchBtn').addEventListener('click', function() {
    fetch('https://jsonplaceholder.typicode.com/posts/1')
        .then(response => response.json())
        .then(data => {
            const dataContainer = document.getElementById('dataContainer');
            dataContainer.innerHTML = `<p><strong>Title:</strong> ${data.title}</p>
                                       <p>${data.body}</p>`;
        })
        .catch(error => {
            console.error('Error fetching data:', error);
        });
});
