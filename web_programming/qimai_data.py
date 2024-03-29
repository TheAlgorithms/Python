"""
Qimai Data (qimai.cn) is a mobile product business analysis platform in China.

Get a dict of the app information for a given typename (free, paid, grossing) from https://www.qimai.cn

p.s. Current version of DrissionPage : 4.0.4.17
https://github.com/g1879/DrissionPage
"""

from DrissionPage import ChromiumPage


def login(page: ChromiumPage, username: str, password: str) -> bool:
    page.get("https://www.qimai.cn/account/signin/r/%2F")
    if page.url != "https://www.qimai.cn/":
        try:
            page.ele("@name=username").input(username)
            page.ele("@name=password").input(password)
            page.ele(".submit").click()
            print("Login successfully")
            return True
        except KeyError:
            print("Login failed")
            page.close()
            return False
    else:
        print("Already login")
        return True


def get_app_info(
    page: ChromiumPage, username: str, password: str, typename: str
) -> dict:
    # Clear the cache to avoid the login failure
    page.clear_cache(cookies=True)
    if login(page, username, password):
        # Get the data of default page
        page.listen.start(f"brand={typename}&device=iphone&country=cn&genre=5000")
        page.get(
            f"https://www.qimai.cn/rank/index/brand/{typename}/device/iphone/country/cn/genre/5000"
        )

        # Get the response data
        res = page.listen.wait().response.body

        dic = {}
        for i in range(len(res["rankInfo"])):
            font = res["rankInfo"][i]["appInfo"]
            dic[font["appId"]] = {
                "appId": font["appId"],
                "appName": font["appName"],
                "country": font["country"],
                "file_size": font["file_size"],
                "icon_path": font["icon"],
                "price": font["price"],
                "publisher": font["publisher"],
                "subtitle": font["subtitle"],
            }

        # Get the data of other pages
        if res["maxPage"] > 1:
            for page_num in range(1, res["maxPage"]):
                # Target the page number
                page.listen.start(f"page={page_num + 1}")
                print(f"Getting page {page_num + 1}")
                # Chrome will scroll to the bottom of the page to load more data
                page.scroll.to_bottom()
                page.wait.load_start()

                res = page.listen.wait().response.body
                for i in range(len(res["rankInfo"])):
                    font = res["rankInfo"][i]["appInfo"]
                    dic[font["appId"]] = {
                        "appId": font["appId"],
                        "appName": font["appName"],
                        "country": font["country"],
                        "file_size": font["file_size"],
                        "icon_path": font["icon"],
                        "price": font["price"],
                        "publisher": font["publisher"],
                        "subtitle": font["subtitle"],
                    }

    else:
        return {"error": "Login failed"}

    return dic


if __name__ == "__main__":
    page = ChromiumPage()
    print(get_app_info(page, "YOUR USERNAME", "YOUR PASSWORD", "free"))
    page.close()
