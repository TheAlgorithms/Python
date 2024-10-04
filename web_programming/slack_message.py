# 12/11/19 tarihinde sarathkaul tarafından oluşturuldu

import requests


def slack_mesaj_gonder(mesaj_govdesi: str, slack_url: str) -> None:
    basliklar = {"Content-Type": "application/json"}
    yanit = requests.post(
        slack_url, json={"text": mesaj_govdesi}, headers=basliklar, timeout=10
    )
    if yanit.status_code != 200:
        mesaj = (
            "Slack'e istek gönderilirken bir hata oluştu "
            f"{yanit.status_code}, yanıt:\n{yanit.text}"
        )
        raise ValueError(mesaj)


if __name__ == "__main__":
    # Web kancası oluşturduğunuzda Slack tarafından sağlanan URL'yi ayarlayın
    # https://my.slack.com/services/new/incoming-webhook/
    slack_mesaj_gonder("<MESAJ GÖVDESİ>", "<SLACK KANAL URL'Sİ>")
