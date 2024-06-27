document.getElementById('search-button').addEventListener('click', function() {
    const query = document.getElementById('search-input').value;
    fetch(`/search_photos?query=${query}`)
        .then(response => response.json())
        .then(data => {
            const results = document.getElementById('results');
            results.innerHTML = '';
            data.image_urls.forEach(url => {
                const img = document.createElement('img');
                img.src = url;
                results.appendChild(img);
            });
        })
        .catch(error => console.error('Error fetching images:', error));
});

document.getElementById('scrape-button').addEventListener('click', function() {
    fetch(`/scrape`)
        .then(response => response.json())
        .then(data => {
            const scrapeResults = document.getElementById('scrape-results');
            scrapeResults.innerHTML = '';

            data.results.forEach(result => {
                const div = document.createElement('div');
                div.classList.add('card');
                div.innerHTML = `
                    <h3>${result.title}</h3>
                    <p>${result.paragraph}</p>
                `;
                scrapeResults.appendChild(div);
            });

            data.properties_details.forEach(property => {
                const div = document.createElement('div');
                div.classList.add('card');
                div.innerHTML = `
                    <h3>${property.denumire}</h3>
                    <p><span>Rating:</span> ${property.rating}</p>
                    <p><span>Price:</span> ${property.pret}</p>
                    <p><span>Guest liked:</span> ${property.guest_liked}</p>
                    <p><span>Description:</span> ${property.descriere}</p>
                    <p><span>Location:</span> ${property.locatie}</p>
                    <p><span>Additional details:</span> ${property.detalii_aditionale.join(', ')}</p>
                `;
                scrapeResults.appendChild(div);
            });
        })
        .catch(error => console.error('Error scraping data:', error));
});
