from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from datetime import timedelta
import os
import whisper

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    # check if the post request has the file part
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file found.'}), 400

    file = request.files['audio']

    if file.filename == '':
        return jsonify({'error': 'No audio file selected.'}), 400

    if not allowed_file(file.filename):
        return jsonify({'error': 'Only WAV, MP3, and OGG audio files are allowed.'}), 400

    filename = secure_filename(file.filename)
    file.save(filename)

    model = whisper.load_model("small") # Change this to your desired model
    print("Whisper model loaded.")
    transcribe = model.transcribe(audio=filename)
    segments = transcribe['segments']

    srt_file = open('subtitles.vtt', 'w', encoding='utf-8')
    srt_file.write('WEBVTT\n\n')

    for segment in segments:
        startTime = str(0)+str(timedelta(seconds=int(segment['start'])))+'.000'
        endTime = str(0)+str(timedelta(seconds=int(segment['end'])))+'.000'
        text = segment['text']
        segmentId = segment['id']+1
        segment = f"{segmentId}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srt_file.write(segment)

    srt_file.close()
    os.remove(filename)

    return send_file('subtitles.vtt', as_attachment=True, download_name='subtitles.vtt', mimetype='text/vtt')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ['wav', 'mp3', 'ogg']

if __name__ == '__main__':
    app.run()
