document.getElementById('addBtn').addEventListener('click', function() {
    const itemList = document.getElementById('itemList');
    const newItem = document.createElement('li');
    newItem.textContent = `Item ${itemList.children.length + 1}`;
    itemList.appendChild(newItem);
});

document.getElementById('removeBtn').addEventListener('click', function() {
    const itemList = document.getElementById('itemList');
    if (itemList.children.length > 0) {
        itemList.removeChild(itemList.lastChild);
    }
});
