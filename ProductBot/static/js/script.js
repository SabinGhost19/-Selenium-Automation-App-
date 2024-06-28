document.getElementById('monitor-form').addEventListener('submit', function(e) {
    e.preventDefault();

    let product_name = document.getElementById('product_name').value;
    let target_price = document.getElementById('target_price').value;

    fetch('/monitor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `product_name=${product_name}&target_price=${target_price}`
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('response').innerText = data;
    })
    .catch(error => console.error('Error:', error));
});
