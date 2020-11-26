import unittest

from other.text_to_speech import get_mp3_filename, request_fromtexttospeech


class TestTextToSpeech(unittest.TestCase):
    def test_request_fromtexttospeech_status_code(self):
        r = request_fromtexttospeech()
        self.assertEqual(r.status_code, 200)

    def test_get_mp3_file_valid_html(self):
        html = "<p>Listen to the MP3 file  :<BR></p> <!> \
                <object classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' \
                        width='470' height='24' id='single1' name='single1'> \
                <param name='movie' value='player.swf'> \
                <param name='allowfullscreen' value='true'> \
                <param name='allowscriptaccess' value='always'> \
                <param name='wmode' value='transparent'> \
                <param name = 'flashvars' \
                       value='file=/output/0360061001606401513/59405670.mp3'> \
                <embed \
                    id='single2' \
                    name='single2' \
                    src='player.swf' \
                    width='470' \
                    height='24' \
                    bgcolor='#000000' \
                    allowscriptaccess='always' \
                    allowfullscreen='true' \
                    flashvars='file=/output/0360061001606401513/59405670.mp3' \
                /> \
                </object>"
        mp3_file_name = get_mp3_filename(html)
        self.assertEqual("/output/0360061001606401513/59405670.mp3", mp3_file_name)

    def test_get_mp3_file_invalid_html(self):
        html = "<p>Listen to the MP3 file  :<BR></p> <!> \
                <object classid='clsid:D27CDB6E-AE6D-11cf-96B8-444553540000' \
                        width='470' height='24' id='single1' name='single1'> \
                <param name='movie' value='player.swf'> \
                <param name='allowfullscreen' value='true'> \
                <param name='allowscriptaccess' value='always'> \
                <param name='wmode' value='transparent'> \
                </object>"
        mp3_file_name = get_mp3_filename(html)
        self.assertIsNone(mp3_file_name)
