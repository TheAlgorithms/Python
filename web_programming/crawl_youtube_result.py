import html
import json
import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from PyInquirer import (Token, ValidationError, Validator, prompt,
                        style_from_dict)


class EmptyValidator(Validator):
    def validate(self, value):
        if len(value.text):
            return True
        else:
            raise ValidationError(
                message="You can't leave this blank", cursor_position=len(value.text)
            )


class MaxResultValidator(Validator):
    def validate(self, value):
        if value.text in "0123456789":
            return True
        else:
            raise ValidationError(
                message="Only enter number in this field",
                cursor_position=len(value.text),
            )


style = style_from_dict(
    {
        Token.QuestionMark: "#E91E63 bold",
        Token.Selected: "#673AB7 bold",
        Token.Instruction: "",
        Token.Answer: "#2196f3 bold",
        Token.Question: "",
    }
)


class HandlerS:
    def scriptResponseHandler(self):
        self.links = []
        self.ids = []
        self.titles = []
        self.channels = []
        self.channelIds = []
        self.publishTime = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        indexValue = 0

        self.pageSource = self.page.split('":"')

        for index in range(0, len(self.pageSource) - 1, 1):

            # Setting Video Durations And View Counts.

            if (
                self.pageSource[index][-14:] == '}},"simpleText'
                and self.pageSource[index + 1][-28:] == '"viewCountText":{"simpleText'
            ):
                durationBuffer = ""
                viewCountBuffer = 0
                for character in self.pageSource[index + 1]:
                    if character != '"':
                        durationBuffer += character
                    else:
                        break
                for character in self.pageSource[index + 2]:
                    if character.isnumeric():
                        viewCountBuffer = viewCountBuffer * 10 + int(character)
                    elif character == '"':
                        break
                self.durations[-1] = durationBuffer
                self.views[-1] = viewCountBuffer

            # Setting Video Links, IDs And Thumbnails.

            if self.pageSource[index][0:9] == "/watch?v=":
                id = self.pageSource[index][9:20]
                modes = [
                    "default",
                    "hqdefault",
                    "mqdefault",
                    "sddefault",
                    "maxresdefault",
                ]
                self.ids += [id]
                self.links += ["https://www.youtube.com/watch?v=" + id]
                thumbnailbuffer = []
                for mode in modes:
                    thumbnailbuffer += [
                        "https://img.youtube.com/vi/" + id + "/" + mode + ".jpg"
                    ]
                self.thumbnails += [thumbnailbuffer]

            # Setting Video Titles.

            if (
                self.pageSource[index][-23:] == '"title":{"runs":[{"text'
                and self.pageSource[index + 1][-44:]
                == '"accessibility":{"accessibilityData":{"label'
            ):
                titleBuffer = ""
                for subIndex in range(len(self.pageSource[index + 1])):
                    if self.pageSource[index + 1][subIndex : subIndex + 2] != "}]":
                        """ For getting rid of " written as \" in JSON """
                        if (
                            self.pageSource[index + 1][subIndex] == '"'
                            and self.pageSource[index + 1][subIndex + 1 : subIndex + 3]
                            != "}]"
                        ):
                            titleBuffer = titleBuffer[:-1]
                        titleBuffer += self.pageSource[index + 1][subIndex]
                    else:
                        titleBuffer = titleBuffer[:-1]
                        break
                self.titles += [titleBuffer.replace("\\u0026", "&")]

                self.views += ["LIVE"]
                self.durations += ["LIVE"]
                self.publishTime += ["LIVE"]
                self.channels += [""]
                self.channelIds += [""]

            # Setting Video Channels.

            if (
                self.pageSource[index][-32:] == '"longBylineText":{"runs":[{"text'
                and self.pageSource[index + 1][-42:]
                == '"navigationEndpoint":{"clickTrackingParams'
            ):
                channelBuffer = ""
                for character in self.pageSource[index + 1]:
                    if character != '"':
                        channelBuffer += character
                    else:
                        break
                try:
                    self.channels[-1] = channelBuffer.replace("\\u0026", "&")
                    self.channelIds[-1] = self.pageSource[index + 5].split('"')[0]
                except:
                    pass

            # Setting Video Published Time Text.

            if self.pageSource[index][-31:] == 'publishedTimeText":{"simpleText':
                self.publishTime[-1] = self.pageSource[index + 1].split('"},"')[0]

            if (
                min(
                    len(self.links),
                    len(self.ids),
                    len(self.titles),
                    len(self.channels),
                    len(self.channelIds),
                    len(self.publishTime),
                    len(self.views),
                    len(self.durations),
                    len(self.thumbnails),
                )
                + 1
                > self.max_results
            ):
                break


class HandlerP:
    def pageResponseHandler(self):
        self.links = []
        self.ids = []
        self.titles = []
        self.channels = []
        self.channelIds = []
        self.views = []
        self.durations = []
        self.thumbnails = []

        self.pageSource = self.page.split()

        for index in range(0, len(self.pageSource) - 1, 1):

            element = self.pageSource[index]
            elementNext = self.pageSource[index + 1]
            elementPrev = self.pageSource[index - 1]

            # Setting Video View Counts.

            if element == "views</li></ul></div><div":
                viewCount = 0
                for character in elementPrev:
                    if character.isnumeric():
                        viewCount = viewCount * 10 + int(character)
                self.views += [viewCount]
                # Unimplemented as this response is not recieved now
                self.channelIds += [""]

            # Setting Video Links, IDs And Thumbnails.

            if (
                element[0:15] == 'href="/watch?v='
                and len("www.youtube.com" + element[6 : len(element) - 1]) == 35
            ):
                thumbnailbuffer = []
                modes = [
                    "default",
                    "hqdefault",
                    "mqdefault",
                    "sddefault",
                    "maxresdefault",
                ]
                if element[15 : len(element) - 1] not in self.ids:
                    self.links += [
                        "https://www.youtube.com" + element[6 : len(element) - 1]
                    ]
                    self.ids += [element[15 : len(element) - 1]]
                    for mode in modes:
                        thumbnailbuffer += [
                            "https://img.youtube.com/vi/"
                            + element[15 : len(element) - 1]
                            + "/"
                            + mode
                            + ".jpg"
                        ]
                    self.thumbnails += [thumbnailbuffer]

            # Setting Video Channels.

            if (
                element[-15:] == "</a>&nbsp;<span"
                and self.pageSource[index + 1] == 'title="Verified"'
            ) or (
                element[-14:] == "</a></div><div"
                and self.pageSource[index + 1] == 'class="yt-lockup-meta'
            ):
                channelBuffer = ""
                channelText = ""
                for channelIndex in range(0, 10):
                    if self.pageSource[index - channelIndex][0] == ">":
                        channelText = (
                            self.pageSource[index - channelIndex] + " " + channelText
                        )
                        break
                    else:
                        channelText = (
                            self.pageSource[index - channelIndex] + " " + channelText
                        )
                channelText = channelText[1:]
                for index in range(0, len(channelText)):
                    if channelText[index] == "<":
                        break
                    else:
                        channelBuffer += channelText[index]
                self.channels += [channelBuffer]

            # Setting Video Durations.

            if element[0:19] == 'aria-hidden="true">' and element[19].isnumeric():
                buffer = ""
                bufferBool = False
                for character in element:
                    if character == ">":
                        bufferBool = True
                    if bufferBool and character != "<":
                        buffer += character
                    if character == "<":
                        break
                self.durations += [buffer[1::]]

            # Setting Video Titles.

            if (element[0:23] == 'data-sessionlink="itct=') and (
                elementNext[0:7] == 'title="'
            ):
                buffer = ""
                init = self.pageSource[index + 1]
                buffer += init
                subIndex = index + 2
                end = index + 22
                while subIndex < end:
                    this_element = self.pageSource[subIndex]
                    next_element = self.pageSource[subIndex + 1]
                    if (this_element[len(this_element) - 1]) == '"':
                        if next_element == 'rel="spf-prefetch"':
                            buffer += " " + this_element
                            self.titles += [html.unescape(buffer[7:-1])]
                            break
                    else:
                        buffer += " " + this_element
                    subIndex += 1

            if len(self.titles) + 1 > self.max_results:
                break


class HandlerR:
    def request(self):
        try:
            query = urlencode(
                {
                    "search_query": self.keyword,
                    "page": self.offset,
                    "sp": self.searchPreferences,
                    "persist_gl": 1,
                    "gl": self.region,
                }
            )
            request = Request(
                "https://www.youtube.com/results" + "?" + query,
                headers={"Accept-Language": f"{self.language},en;q=0.9"},
            )
            response = urlopen(request).read()
            self.page = response.decode("utf_8")

            if self.page[0:29] == '  <!DOCTYPE html><html lang="':
                self.validResponse = True

        except:
            self.networkError = True


class SearchVideos(HandlerR, HandlerP, HandlerS):
    networkError = False
    validResponse = False

    def __init__(
        self,
        keyword,
        offset=1,
        mode="json",
        max_results=20,
        language="en-US",
        region="US",
    ):
        self.offset = offset
        self.mode = mode
        self.keyword = keyword
        self.max_results = max_results
        self.searchPreferences = "EgIQAQ%3D%3D"
        self.language = language
        self.region = region
        self.main()

    def main(self):
        self.request()
        if self.networkError:
            self.networkError = True
        else:

            if not self.validResponse:
                self.scriptResponseHandler()

            if self.validResponse:
                self.pageResponseHandler()

    def result(self):
        if self.networkError:
            return None

        else:

            result = []

            if self.mode in ["json", "dict"]:

                for index in range(len(self.ids)):
                    result_index = {
                        "index": index,
                        "id": self.ids[index],
                        "link": self.links[index],
                        "title": self.titles[index],
                        "channel": self.channels[index],
                        "duration": self.durations[index],
                        "views": self.views[index],
                        "thumbnails": self.thumbnails[index],
                        "channelId": self.channelIds[index],
                        "publishTime": self.publishTime[index],
                    }
                    result += [result_index]

                if self.mode == "json":
                    return json.dumps({"search_result": result}, indent=4)
                else:
                    return {"search_result": result}

            elif self.mode == "list":

                for index in range(len(self.ids)):
                    list_index = [
                        index,
                        self.ids[index],
                        self.links[index],
                        self.titles[index],
                        self.channels[index],
                        self.durations[index],
                        self.views[index],
                        self.thumbnails[index],
                        self.channelIds[index],
                        self.publishTime[index],
                    ]
                    result += [list_index]

                return result


if __name__ == "__main__":
    key = [
        {
            "type": "input",
            "name": "key",
            "message": "Enter search keyword:",
            "validate": EmptyValidator,
        },
        {
            "type": "list",
            "name": "mode",
            "message": "Choose mode:",
            "choices": [
                "Json",
                "Dictionary",
                "List",
            ],
        },
        {
            "type": "input",
            "name": "max",
            "message": "Enter max results(Defualt: 20):",
            "validate": MaxResultValidator,
        },
    ]
    answer = prompt(key, style=style)
    if answer["mode"] == "Dictionary":
        answer["mode"] = "dict"
    if answer["max"] == "":
        answer["max"] = 20
    search = SearchVideos(
        keyword=answer["key"],
        offset=1,
        mode=answer["mode"].lower(),
        max_results=int(answer["max"]),
    )
    print(search.result())
    """
    Parameters
    ----------
    keyword : str 
        Used as a query to search for videos in YouTube.
    offset : int, optional
        Offset for result pages on YouTube. Defaults to 1.
    mode : str
        Search result mode. Can be 'json', 'dict' or 'list'.
    max_results : int, optional
        Maximum number of playlist results. Defaults to 20.
    language: str, optional
        Can be used to get results in particular language. Defaults to 'en-US'
    region: str, optional
        Can be used to get results according to particular region. Defaults to 'US'.
    
    Returns None, if network error occurs.
    """
