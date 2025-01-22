async function fetchSuggestions(query, elementId) {
    if (query.length < 3) {
        document.getElementById(elementId).innerHTML = '';
        return;
    }

    const url = `https://api.tomtom.com/search/2/search/${query}.json?key=${TOMTOM_API_KEY}&typeahead=true&limit=5`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.results) {
            // Filter for cities and countries only
            const suggestions = data.results
                .filter(result => result.entityType === "Municipality" || result.entityType === "Country")
                .map(result => result.address.freeformAddress);

            displaySuggestions(suggestions, elementId);
        }
    } catch (error) {
        console.error("Error fetching suggestions:", error);
    }
}

function displaySuggestions(suggestions, elementId) {
    const suggestionsDiv = document.getElementById(elementId);
    suggestionsDiv.innerHTML = '';

    if (suggestions.length > 0) {
        suggestionsDiv.style.display = 'block'; // Show the dropdown
        suggestions.forEach(suggestion => {
            const div = document.createElement('div');
            div.textContent = suggestion;
            div.addEventListener('click', () => {
                document.getElementById(elementId.replace('-suggestions', '')).value = suggestion;
                suggestionsDiv.style.display = 'none'; // Hide dropdown after selection
            });
            suggestionsDiv.appendChild(div);
        });
    } else {
        suggestionsDiv.style.display = 'none'; // Hide the dropdown if no suggestions
    }
}

// Add event listeners for the origin and destination inputs
document.getElementById('origin').addEventListener('input', () => fetchSuggestions(document.getElementById('origin').value, 'origin-suggestions'));
document.getElementById('destination').addEventListener('input', () => fetchSuggestions(document.getElementById('destination').value, 'destination-suggestions'));


document.addEventListener('DOMContentLoaded', () => {
    const trafficForm = document.getElementById('trafficForm');
    const goButton = document.getElementById('go-button');
    const loadingGif = document.getElementById('loading-gif');

    trafficForm.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent default form submission

        // Show the loading GIF and hide the "Go!" button
        goButton.style.display = 'none';
        loadingGif.style.display = 'block';

        // Submit the form data via fetch
        const formData = new FormData(trafficForm);

        fetch('/', {
            method: 'POST',
            body: formData,
        })
            .then(response => response.text())
            .then(html => {
                // Replace the content with the response
                document.querySelector('.everything').innerHTML = html;

                // Hide the loading GIF after the response is processed
                loadingGif.style.display = 'none';
            })
            .catch(error => {
                console.error('Error submitting the form:', error);
                alert('An error occurred. Please try again.');

                // Reset the button and GIF on error
                goButton.style.display = 'block';
                loadingGif.style.display = 'none';
            });
    });
});
