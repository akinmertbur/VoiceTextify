from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    data = request.get_json()
    recognized_text = data.get('text', '')

    # Process the recognized text as needed (db operations)
    print("Recognized Text: " + recognized_text)

    return jsonify({'status': 'success', 'text': recognized_text})

if __name__ == '__main__':
    app.run(debug=True)
