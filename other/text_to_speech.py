"""
Created by: Ariel Sperduti

Given a text it converts into an  MP3 audio file.
Under the hood it uses fromtexttospeech.com.

Example:
    text_to_speech(text="¡Hola Mundo!", language="Spanish", voice="Mateo")
"""

import re

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


def get_mp3_filename(html: str) -> str:
    """Returns the  mp3 file name of an HTML response from fromtexttospeech.com"""
    try:
        filename = re.search(r"(\/output\/\d+\/\d+\.mp3)", html).group(0)
    except AttributeError:
        filename = None
    return filename


def request_fromtexttospeech(
    text: str = "Hello world",
    language: str = "British",
    voice: str = "Emma",
) -> requests.Response:
    """Makes POST request to fromtexttospeech and returns a requests.Response."""
    # prepare data
    data = {
        "input_text": text,
        "language": language,
        "voice": VOICES[voice],
        "speed": 0,
        "action": "process_text",
    }

    headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 "
        + "Firefox/66.0",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": "http://www.fromtexttospeech.com/",
        "Connection": "keep-alive",
    }
    # make request to www.fromtexttospeech.com
    # it gives an html with the mp3's url
    return requests.post("http://www.fromtexttospeech.com/", headers=headers, data=data)


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

    r = request_fromtexttospeech(text, language, voice)
    # extract the mp3's url
    mp3_file = get_mp3_filename(r.text)
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
