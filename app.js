// JavaScript (app.js)
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/products')
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById('productTableBody');
            data.forEach(product => {
                const row = document.createElement('tr');
                const idCell = document.createElement('td');
                idCell.textContent = product.id;
                const nameCell = document.createElement('td');
                nameCell.textContent = product.name;
                const priceCell = document.createElement('td');
                priceCell.textContent = product.price;
                row.appendChild(idCell);
                row.appendChild(nameCell);
                row.appendChild(priceCell);
                tableBody.appendChild(row);
            });
        })
        .catch(error => {
            console.error('Lỗi:', error);
        });
});
