
// document.getElementById('search-button').addEventListener('click', function() {
//     const query = document.getElementById('search-input').value;
//     fetch(`/search_photos?query=${query}`)
//         .then(response => response.json())
//         .then(data => {
//             const results = document.getElementById('results');
//             results.innerHTML = '';
//             data.image_urls.forEach(url => {
//                 const img = document.createElement('img');
//                 img.src = url;
//                 results.appendChild(img);
//             });
//             showSection('results');
//         })
//         .catch(error => console.error('Error fetching images:', error));
// });

// document.getElementById('scrape-button').addEventListener('click', function() {
//     const location = document.getElementById('search-input').value;
//     fetch(`/scrape?location=${location}`)
//         .then(response => response.json())
//         .then(data => {
//             const attractionsResults = document.getElementById('attractions-results');
//             attractionsResults.innerHTML = '';

//             data.results.forEach(result => {
//                 const div = document.createElement('div');
//                 div.classList.add('card');
//                 div.innerHTML = `
//                     <h3>${result.title}</h3>
//                     <p>${result.paragraph}</p>
//                 `;
//                 attractionsResults.appendChild(div);
//             });

//             const hotelsResults = document.getElementById('hotels-results');
//             hotelsResults.innerHTML = '';

//             data.properties_details.forEach(property => {
//                 const div = document.createElement('div');
//                 div.classList.add('card');
//                 div.innerHTML = `
//                     <h3>${property.denumire}</h3>
//                     <p><span>Rating:</span> ${property.rating}</p>
//                     <p><span>Price:</span> ${property.pret}</p>
//                     <p><span>Guest liked:</span> ${property.guest_liked}</p>
//                     <p><span>Description:</span> ${property.descriere}</p>
//                     <p><span>Location:</span> ${property.locatie}</p>
//                     <p><span>Additional details:</span> ${property.detalii_aditionale.join(', ')}</p>
//                 `;
//                 hotelsResults.appendChild(div);
//             });

//             const historyResults = document.getElementById('history-results');
//             historyResults.innerHTML = '';

//             data.wikipedia_data.forEach(paragraph => {
//                 const p = document.createElement('p');
//                 p.textContent = paragraph;
//                 historyResults.appendChild(p);
//             });

//             showSection('attractions-results'); // Default display after scraping
//         })
//         .catch(error => console.error('Error scraping data:', error));
// });

// document.getElementById('show-images').addEventListener('click', function() {
//     showSection('results');
// });

// document.getElementById('show-attractions').addEventListener('click', function() {
//     showSection('attractions-results');
// });

// document.getElementById('show-hotels').addEventListener('click', function() {
//     showSection('hotels-results');
// });

// document.getElementById('show-history').addEventListener('click', function() {
//     showSection('history-results');
// });

// function showSection(sectionId) {
//     document.getElementById('results').classList.add('hidden');
//     document.getElementById('attractions-results').classList.add('hidden');
//     document.getElementById('hotels-results').classList.add('hidden');
//     document.getElementById('history-results').classList.add('hidden');

//     document.getElementById(sectionId).classList.remove('hidden');
// }



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
            showSection('results');
        })
        .catch(error => console.error('Error fetching images:', error));
});

document.getElementById('scrape-button').addEventListener('click', function() {
    const location = document.getElementById('search-input').value;
    fetch(`/scrape?location=${location}`)
        .then(response => response.json())
        .then(data => {
            const attractionsResults = document.getElementById('attractions-results');
            attractionsResults.innerHTML = '';

            data.results.forEach(result => {
                const div = document.createElement('div');
                div.classList.add('card');
                div.innerHTML = `
                    <h3>${result.title}</h3>
                    <p>${result.paragraph}</p>
                `;
                attractionsResults.appendChild(div);
            });

            const hotelsResults = document.getElementById('hotels-results');
            hotelsResults.innerHTML = '';

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
                    <button class="monitor-price-button" data-url="${property.url}">Monitor Price</button>
                `;
                hotelsResults.appendChild(div);
            });

            document.querySelectorAll('.monitor-price-button').forEach(button => {
                button.addEventListener('click', function() {
                    const hotelUrl = this.getAttribute('data-url');
                    const minPrice = prompt('Introduceți suma minimă dorită pentru monitorizare:');
                    if (minPrice) {
                        fetch('/monitor_price', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                hotel_url: hotelUrl,
                                min_price: parseFloat(minPrice),
                            }),
                        })
                        .then(response => response.json())
                        .then(data => alert(data.status))
                        .catch(error => console.error('Error monitoring price:', error));
                    }
                });
            });

            const historyResults = document.getElementById('history-results');
            historyResults.innerHTML = '';

            data.wikipedia_data.forEach(paragraph => {
                const p = document.createElement('p');
                p.textContent = paragraph;
                historyResults.appendChild(p);
            });

            showSection('attractions-results'); // Default display after scraping
        })
        .catch(error => console.error('Error scraping data:', error));
});

document.getElementById('show-images').addEventListener('click', function() {
    showSection('results');
});

document.getElementById('show-attractions').addEventListener('click', function() {
    showSection('attractions-results');
});

document.getElementById('show-hotels').addEventListener('click', function() {
    showSection('hotels-results');
});

document.getElementById('show-history').addEventListener('click', function() {
    showSection('history-results');
});

function showSection(sectionId) {
    document.getElementById('results').classList.add('hidden');
    document.getElementById('attractions-results').classList.add('hidden');
    document.getElementById('hotels-results').classList.add('hidden');
    document.getElementById('history-results').classList.add('hidden');

    document.getElementById(sectionId).classList.remove('hidden');
}
