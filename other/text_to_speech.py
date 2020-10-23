"""
Created by: Ariel Sperduti

Given a text it converts into an  MP3 audio file.
Under the hood it uses fromtexttospeech.com.

Example:
    text_to_speech(text="¡Hola Mundo!", language="Spanish", voice="Mateo")
"""

import re
import subprocess
import urllib.parse

import requests

LANGUAGES_VOICES = {
    "US English": ["Alice", "Daisy", "George", "Jenna", "John"],
    "British": ["Emma", "Harry"],
    "French": ["Gabriel", "Jade"],
    "Spanish": ["Isabella", "Mateo"],
    "German": ["Michael", "Nadine"],
    "Italian": ["Alessandra", "Giovanni"],
    "Portuguese": ["Rodrigo"],
    "Russian": ["Valentina"],
}

VOICES = {
    "Emma": "IVONA Amy22 (UK English)",
    "Harry": "IVONA Brian22 (UK English)",
    "Jade": "IVONA CΘline22 (French)",
    "Gabriel": "IVONA Mathieu22 (French)",
    "Nadine": "IVONA Marlene22 (German)",
    "Michael": "IVONA Hans22 (German)",
    "Valentina": "IVONA Tatyana22 (Russian)",
    "John": "IVONA Eric22",
    "Jenna": "IVONA Jennifer22",
    "George": "IVONA Joey22",
    "Alice": "IVONA Kimberly22",
    "Daisy": "IVONA Salli22",
    "Alessandra": "IVONA Carla22 (Italian)",
    "Giovanni": "IVONA Giorgio22 (Italian)",
    "Isabella": "IVONA Conchita22 (Spanish [Modern])",
    "Mateo": "IVONA Enrique22 (Spanish [Modern])",
    "Rodrigo": "IVONA Cristiano22 (Portuguese)",
}


def text_to_speech(
    text: str = "Hello world",
    language: str = "British",
    voice: str = "Emma",
    audio_path: str = "output.mp3",
) -> bool:

    if language not in LANGUAGES_VOICES:
        raise ValueError(f"Language '{language}' not available")

    if voice not in LANGUAGES_VOICES[language]:
        raise ValueError(f"Voice '{voice}' not available")

    # prepare data
    text_encoded = urllib.parse.quote(text.encode("utf8"))
    data = f"input_text={text_encoded}&language={language}\
            &voice={VOICES[voice]}&speed=0&action=process_text"

    # make request to www.fromtexttospeech.com
    # it gives an html with the mp3's url
    args = [
        "curl",
        "http://www.fromtexttospeech.com/",
        "-H",
        "Accept-Language: en-US,en;q=0.5",
        "-H",
        "Upgrade-Insecure-Requests: 1",
        "-H",
        "User-Agent:  \
            Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "-H",
        "Content-Type: application/x-www-form-urlencoded",
        "-H",
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "-H",
        "Referer: http://www.fromtexttospeech.com/",
        "-H",
        "Connection: keep-alive",
        "--data",
        data,
        "--compressed",
        "--connect-timeout",
        "30",
        "--retry",
        "300",
        "--retry-delay",
        "5",
        "--max-time",
        "120",
    ]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)

    output = process.communicate()[0]

    # extract the mp3's url
    mp3_file = re.search(r"(\/output\/\d+\/\d+\.mp3)", output.decode("utf-8")).group(0)
    audio_url = f"http://www.fromtexttospeech.com{mp3_file}"

    mp3data = requests.get(audio_url)

    # save the data as an mp3 file
    if mp3data.status_code != 404:
        with open(audio_path, "w+b") as f:
            f.write(mp3data.content)
        return True

    return False


if __name__ == "__main__":
    text_to_speech(text="¡Hola Mundo!", language="Spanish", voice="Mateo")
