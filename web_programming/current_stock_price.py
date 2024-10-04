import requests
from bs4 import BeautifulSoup

def stock_price(symbol: str = "AAPL") -> str:
    """
    Verilen sembol için Yahoo Finance'ten hisse senedi fiyatını döndürür.
    @parametreler: symbol, hisse senedi sembolü (varsayılan: "AAPL")
    """
    url = f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"
    try:
        yahoo_finance_source = requests.get(
            url, headers={"USER-AGENT": "Mozilla/5.0"}, timeout=10
        )
        yahoo_finance_source.raise_for_status()
    except requests.RequestException as e:
        return f"Veri alınırken hata oluştu: {e}"

    soup = BeautifulSoup(yahoo_finance_source.text, "html.parser")
    specific_fin_streamer_tag = soup.find("fin-streamer", {"data-test": "qsp-price"})

    if specific_fin_streamer_tag:
        text = specific_fin_streamer_tag.get_text()
        return text
    return "Belirtilen data-test özniteliğine sahip <fin-streamer> etiketi bulunamadı."

# Sembolü https://finance.yahoo.com/lookup adresinde arayın
if __name__ == "__main__":
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL".split():
        print(f"Current {symbol:<4} stock price is {stock_price(symbol):>8}")
