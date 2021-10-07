# Plagiarism checker - Checks Bing results for plagiarism checking.
# Author: Anuran Roy (https://github.com/anuran-roy)

import string
import time
from typing import Any, Dict, List, Set

import nltk
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download("stopwords")

stopwords = stopwords.words("english")


def clean_string(text: str) -> str:
    """
    This function cleans the supplied string.
    It strips off punctuations and emojis from the text that you are entering.
    """

    text = text.lower()
    text = "".join([word for word in text if word not in string.punctuation])
    text = "".join([word for word in text.split() if word not in stopwords])

    return text


def getResults(text: str) -> str:
    """
    This function fetches the search results from Bing,
    processes them into a query string,
    fetches the search results, and returns them.
    """

    text = text.replace(" ", "+")
    # print(text)  # For debugging
    url: str = (
        f"https://www.bing.com/search?q={text}&qs=n&form=QBRE&sp=-1&pq={text.lower()}"
    )

    # Crafting the proper request
    header: Dict = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
    }

    page: Any = requests.get(url, headers=header, allow_redirects=True)

    content: str = BeautifulSoup(page.content, "html.parser")
    # print(content)  # For debugging
    return content


def process(content: Any) -> Dict:
    """
    This function processes the content of the search results
    and returns them as a dictionary, each entry containing the details
    of the card of each result.
    """

    res: Dict = {}
    res["headlines"]: List = []
    res["result-stats"]: List = []
    res["cards"]: List = []

    for i in content.find_all("h2"):
        entry: str = i.find("a")
        lnk: str = ""
        if len(str(entry)) >= 28:
            lnk = str(entry)[28 : str(entry).index('" target')]
        res["headlines"].append((i.get_text(), lnk))

    for i in content.find_all("p"):
        res["cards"].append(
            i.get_text()
            .replace("/strong&gt;", "")
            .replace("&lt;", "")
            .replace("strong&gt;", "")
        )

    res["result-stats"] = [
        i.get_text() for i in content.find_all("span", attrs={"class": "sb_count"})
    ][0]

    return res


def web_search(sentence_list: List) -> Dict:
    """
    Searches each sentence in sentence list and
    returns the final results as a dictionary.
    """

    search_results: Dict = {}

    for i in range(len(sentence_list)):
        cnt: str = getResults(sentence_list[i])
        search_results[sentence_list[i]] = process(cnt)
        time.sleep(2)

        print(f"Completion percent: {i/len(sentence_list)*100}%")

    return search_results


def similarity(s1: str, s2: str) -> float:
    """
    This function checks the similarity between two strings, and returns
    the similarity score ranging from 0 (no plagiarism) to 1(identical copy).
    """

    l1: List = word_tokenize(s1)
    l2: List = word_tokenize(s2)

    v1: List = []
    v2: List = []

    set1: Set = {w for w in l1 if w not in stopwords}
    set2: Set = {w for w in l2 if w not in stopwords}

    rvect: Set = set1.union(set2)

    for w in rvect:
        if w in set1:
            v1.append(1)
        else:
            v1.append(0)

        if w in set2:
            v2.append(1)
        else:
            v2.append(0)

    score: float = 0

    for i in range(len(rvect)):
        score += v1[i] * v2[i]
    div = float((sum(v1) * sum(v2)) ** 0.5)

    if div > 0:
        score /= div
    else:
        score = 0
    return score


def scorer(sentence_list: List, sentence_list_web: List) -> float:
    """
    Returns a score of the total input lists,
    and matches the strings in the two lists
    (one from the paragraph, and one after parsing the web results)
    with each other.
    """

    len1: int = len(sentence_list)
    len2: int = 0
    for i in sentence_list_web:
        len2 += len(i)
    f: float = 0

    for i in range(len1):
        if sentence_list_web[i] == []:
            f += 1
        else:
            for j in range(len(sentence_list_web[i])):
                f += similarity(sentence_list[i], sentence_list_web[i][j])

    f /= len2

    return f


def extractor(resdict: Dict) -> List:
    """
    This method parses the web results and segregates them into cards.
    """

    slweb: List = []
    for i in resdict.keys():
        itm = resdict[i]["cards"]
        # print(itm)
        slweb.append(itm)

    return slweb


def driver(txt: str) -> None:  # Driver code
    """
    This method controls the total flow of execution of the functions.
    """

    txt = """{}""".format(txt)

    sen: List = []

    sen0: List = sent_tokenize(txt)
    for i in sen0:
        sen.append(i)  # (clean_string(i))

    # print(sen)

    results: List = extractor(web_search(sen))

    scorer_results = scorer(sen, results)

    print("Completion percent: 100%")
    print(f"Plagiarism = {scorer_results*100}%")


txt: str = input("Enter text:")
driver(txt)
