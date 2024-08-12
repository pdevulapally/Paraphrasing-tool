from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load a pre-trained paraphrasing model from Hugging Face
paraphrase_pipeline = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

@app.route('/paraphrase', methods=['POST'])
def paraphrase():
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({"error": "No text provided"}), 400

    # Generate paraphrase
    paraphrased_text = paraphrase_pipeline(text, max_length=100, num_return_sequences=1)[0]['generated_text']

    return jsonify({"paraphrased_text": paraphrased_text})

# Route to serve the front-end HTML file
@app.route('/')
def serve_index():
    return send_from_directory('', 'index.html')

# Route to serve the CSS file
@app.route('/style.css')
def serve_css():
    return send_from_directory('', 'style.css')

# Route to serve the JavaScript file
@app.route('/script.js')
def serve_js():
    return send_from_directory('', 'script.js')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
