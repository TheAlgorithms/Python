import requests


# Bir IP adresi için coğrafi konum verilerini almak için fonksiyon
def get_ip_geolocation(ip_address: str) -> str:
    try:
        # IP coğrafi konum API'si için URL'yi oluştur
        url = f"https://ipinfo.io/{ip_address}/json"

        # API'ye GET isteği gönder
        response = requests.get(url, timeout=10)

        # HTTP isteğinin başarılı olup olmadığını kontrol et
        response.raise_for_status()

        # Yanıtı JSON olarak ayrıştır
        data = response.json()

        # Şehir, bölge ve ülke bilgisi mevcut mu kontrol et
        if "city" in data and "region" in data and "country" in data:
            location = f"Konum: {data['city']}, {data['region']}, {data['country']}"
        else:
            location = "Konum verisi bulunamadı."

        return location
    except requests.exceptions.RequestException as e:
        # Ağ ile ilgili istisnaları ele al
        return f"İstek hatası: {e}"
    except ValueError as e:
        # JSON ayrıştırma hatalarını ele al
        return f"JSON ayrıştırma hatası: {e}"


if __name__ == "__main__":
    # Kullanıcıdan bir IP adresi girmesini iste
    ip_address = input("Bir IP adresi girin: ")

    # Coğrafi konum verilerini al ve yazdır
    location = get_ip_geolocation(ip_address)
    print(location)
