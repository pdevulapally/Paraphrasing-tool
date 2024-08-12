document.getElementById('paraphrase-button').addEventListener('click', function() {
    const inputText = document.getElementById('input-text').value;

    fetch('http://localhost:5000/paraphrase', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('output-text').value = data.paraphrased_text;
    })
    .catch(error => console.error('Error:', error));
});
