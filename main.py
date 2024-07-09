from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    audio_file = request.files['file']

    # Save the file temporarily to process it
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
        try:
            # Specify the language as Turkish
            text = recognizer.recognize_google(audio, language="tr-TR")
            return jsonify({'text': text})
        except sr.UnknownValueError:
            return jsonify({'error': 'Speech was unintelligible'})
        except sr.RequestError:
            return jsonify({'error': 'Could not request results from Google Speech Recognition service'})

if __name__ == '__main__':
    app.run(debug=True)
