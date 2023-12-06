document.getElementById('clickBtn').addEventListener('click', function() {
    document.getElementById('output').textContent = 'Button was clicked!';
});

document.getElementById('inputField').addEventListener('keyup', function(event) {
    document.getElementById('output').textContent = `You typed: ${event.target.value}`;
});
