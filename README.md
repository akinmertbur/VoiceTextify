# VoiceTextify

This project implements a speech-to-text application with speaker recognition using a Flask web application. The system identifies whether the speaker is a target speaker and converts their speech to text if recognized.

## Features

- **Speaker Recognition**: Uses a Support Vector Machine (SVM) model to recognize the target speaker.
- **Speech-to-Text Conversion**: Converts recognized speech to text using the Google Web Speech API.
- **Feature Extraction**: Extracts MFCCs, delta, and delta-delta coefficients from audio files for speaker recognition.
- **Flask Web Application**: Provides a web interface for uploading audio files and displaying recognized text.

## Project Structure

```bash
VoiceTextify/
│
├── app.py
├── requirements.txt
├── model_training/
│ ├── train_model.py
│ ├── speaker_recognition_model.pkl
│ └── voice_samples/
│ ├── target_speaker/
│ │ ├── sample1.wav
│ │ ├── sample2.wav
│ │ └── ...
│ └── other_speakers/
│ ├── sample1.wav
│ ├── sample2.wav
│ └── ...
├── templates/
│ └── index.html
├── static/
│ └── css/
│ └── styles.css
└── utils/
├── feature_extraction.py
└── init.py
```

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/akinmertbur/VoiceTextify.git
    cd VoiceTextify
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use .venv\Scripts\activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Training the Model

1. **Place voice samples**:
    - Add target speaker samples to `model_training/voice_samples/target_speaker/`.
    - Add other speaker samples to `model_training/voice_samples/other_speakers/`.

2. **Run the training script**:
    ```bash
    python model_training/train_model.py
    ```

## Running the Flask Application

1. **Ensure the model is trained and `speaker_recognition_model.pkl` is present**.
2. **Start the Flask application**:
    ```bash
    python app.py
    ```

3. **Open your browser and navigate to** `http://127.0.0.1:5000/`.

## Usage

1. **Upload an audio file** using the provided interface.
2. **The system will check if the speaker is the target speaker**:
    - If recognized, it will convert the speech to text and display it.
    - If not recognized, it will return an error message.

## File Descriptions

- **app.py**: The main Flask application file.
- **requirements.txt**: A file listing the dependencies required for the project.
- **model_training/**: Contains scripts and data for training the speaker recognition model.
  - **train_model.py**: Script to train the speaker recognition model.
  - **speaker_recognition_model.pkl**: The trained speaker recognition model.
  - **voice_samples/**: Directory containing voice samples for training.
- **templates/**: Contains HTML templates for the Flask application.
  - **index.html**: The main HTML template for the speech-to-text interface.
- **static/**: Directory for static files like CSS.
  - **css/**: Directory for CSS files.
    - **styles.css**: Stylesheet for the application.
- **utils/**: Contains utility scripts.
  - **feature_extraction.py**: Script for extracting features from audio files.

## Dependencies

- Flask
- SpeechRecognition
- librosa
- numpy
- scikit-learn
- joblib
- gtts

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
