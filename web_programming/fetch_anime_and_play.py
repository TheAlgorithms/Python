import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from fake_useragent import UserAgent

BASE_URL = "https://ww1.gogoanime2.org"


def search_scraper(anime_name: str) -> list:
    """[summary]

    Bir URL al ve
    siteyi kazıdıktan sonra anime listesini döndür.

    >>> type(search_scraper("demon_slayer"))
    <class 'list'>

    Args:
        anime_name (str): [Anime adı]

    Raises:
        e: [Başarısızlık durumunda istisna fırlatır]

    Returns:
        [list]: [Anime listesi]
    """

    # Arama URL'sini oluşturmak için adı birleştir.
    search_url = f"{BASE_URL}/search/{anime_name}"

    response = requests.get(
        search_url, headers={"User-Agent": UserAgent().chrome}, timeout=10
    )  # URL'yi iste.

    # Yanıt iyi mi?
    response.raise_for_status()

    # Soup ile ayrıştır.
    soup = BeautifulSoup(response.text, "html.parser")

    # Anime listesini al
    anime_ul = soup.find("ul", {"class": "items"})
    if anime_ul is None or isinstance(anime_ul, NavigableString):
        msg = f"{anime_name} adında bir anime bulunamadı"
        raise ValueError(msg)
    anime_li = anime_ul.children

    # Her anime için listeye ekle. Adı ve URL'si.
    anime_list = []
    for anime in anime_li:
        if isinstance(anime, Tag):
            anime_url = anime.find("a")
            if anime_url is None or isinstance(anime_url, NavigableString):
                continue
            anime_title = anime.find("a")
            if anime_title is None or isinstance(anime_title, NavigableString):
                continue

            anime_list.append({"title": anime_title["title"], "url": anime_url["href"]})

    return anime_list


def search_anime_episode_list(episode_endpoint: str) -> list:
    """[summary]

    Bir URL al ve
    siteyi kazıdıktan sonra bölüm listesini döndür.

    >>> type(search_anime_episode_list("/anime/kimetsu-no-yaiba"))
    <class 'list'>

    Args:
        episode_endpoint (str): [Bölümün son noktası]

    Raises:
        e: [Açıklama]

    Returns:
        [list]: [Bölüm listesi]
    """

    request_url = f"{BASE_URL}{episode_endpoint}"

    response = requests.get(
        url=request_url, headers={"User-Agent": UserAgent().chrome}, timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Bu kimlikle bölüm listesini al.
    episode_page_ul = soup.find("ul", {"id": "episode_related"})
    if episode_page_ul is None or isinstance(episode_page_ul, NavigableString):
        msg = f"{episode_endpoint} adında bir anime bölümü bulunamadı"
        raise ValueError(msg)
    episode_page_li = episode_page_ul.children

    episode_list = []
    for episode in episode_page_li:
        if isinstance(episode, Tag):
            url = episode.find("a")
            if url is None or isinstance(url, NavigableString):
                continue
            title = episode.find("div", {"class": "name"})
            if title is None or isinstance(title, NavigableString):
                continue

            episode_list.append(
                {"title": title.text.replace(" ", ""), "url": url["href"]}
            )

    return episode_list


def get_anime_episode(episode_endpoint: str) -> list:
    """[summary]

    Bölüm URL'sinden tıklama URL'si ve indirme URL'si al

    >>> type(get_anime_episode("/watch/kimetsu-no-yaiba/1"))
    <class 'list'>

    Args:
        episode_endpoint (str): [Bölümün son noktası]

    Raises:
        e: [Açıklama]

    Returns:
        [list]: [İndirme ve izleme URL'si listesi]
    """

    episode_page_url = f"{BASE_URL}{episode_endpoint}"

    response = requests.get(
        url=episode_page_url, headers={"User-Agent": UserAgent().chrome}, timeout=10
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    url = soup.find("iframe", {"id": "playerframe"})
    if url is None or isinstance(url, NavigableString):
        msg = f"{episode_endpoint} adresinden URL ve indirme URL'si bulunamadı"
        raise RuntimeError(msg)

    episode_url = url["src"]
    if not isinstance(episode_url, str):
        msg = f"{episode_endpoint} adresinden URL ve indirme URL'si bulunamadı"
        raise RuntimeError(msg)
    download_url = episode_url.replace("/embed/", "/playlist/") + ".m3u8"

    return [f"{BASE_URL}{episode_url}", f"{BASE_URL}{download_url}"]


if __name__ == "__main__":
    anime_name = input("Anime adını girin: ").strip()
    anime_list = search_scraper(anime_name)
    print("\n")

    if len(anime_list) == 0:
        print("Bu adla bir anime bulunamadı")
    else:
        print(f"{len(anime_list)} sonuç bulundu: ")
        for i, anime in enumerate(anime_list):
            anime_title = anime["title"]
            print(f"{i+1}. {anime_title}")

        anime_choice = int(input("\nLütfen aşağıdaki listeden birini seçin: ").strip())
        chosen_anime = anime_list[anime_choice - 1]
        print(f"{chosen_anime['title']} seçtiniz. Bölümler aranıyor...")

        episode_list = search_anime_episode_list(chosen_anime["url"])
        if len(episode_list) == 0:
            print("Bu anime için bölüm bulunamadı")
        else:
            print(f"{len(episode_list)} sonuç bulundu: ")
            for i, episode in enumerate(episode_list):
                print(f"{i+1}. {episode['title']}")

            episode_choice = int(input("\nBir bölüm seçin: ").strip())
            chosen_episode = episode_list[episode_choice - 1]
            print(f"{chosen_episode['title']} seçtiniz. Aranıyor...")

            episode_url, download_url = get_anime_episode(chosen_episode["url"])
            print(f"\nİzlemek için, {episode_url} adresine ctrl+click yapın.")
            print(f"İndirmek için, {download_url} adresine ctrl+click yapın.")
