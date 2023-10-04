"""
This is used to convert the currency using the Amdoren Currency API
https://www.amdoren.com
"""

import os

import requests

URL_BASE = "https://www.amdoren.com/api/currency.php"


# Currency and their description
list_of_currencies = """
AED	United Arab Emirates Dirham
AFN	Afghan Afghani
ALL	Albanian Lek
AMD	Armenian Dram
ANG	Netherlands Antillean Guilder
AOA	Angolan Kwanza
ARS	Argentine Peso
AUD	Australian Dollar
AWG	Aruban Florin
AZN	Azerbaijani Manat
BAM	Bosnia & Herzegovina Convertible Mark
BBD	Barbadian Dollar
BDT	Bangladeshi Taka
BGN	Bulgarian Lev
BHD	Bahraini Dinar
BIF	Burundian Franc
BMD	Bermudian Dollar
BND	Brunei Dollar
BOB	Bolivian Boliviano
BRL	Brazilian Real
BSD	Bahamian Dollar
BTN	Bhutanese Ngultrum
BWP	Botswana Pula
BYN	Belarus Ruble
BZD	Belize Dollar
CAD	Canadian Dollar
CDF	Congolese Franc
CHF	Swiss Franc
CLP	Chilean Peso
CNY	Chinese Yuan
COP	Colombian Peso
CRC	Costa Rican Colon
CUC	Cuban Convertible Peso
CVE	Cape Verdean Escudo
CZK	Czech Republic Koruna
DJF	Djiboutian Franc
DKK	Danish Krone
DOP	Dominican Peso
DZD	Algerian Dinar
EGP	Egyptian Pound
ERN	Eritrean Nakfa
ETB	Ethiopian Birr
EUR	Euro
FJD	Fiji Dollar
GBP	British Pound Sterling
GEL	Georgian Lari
GHS	Ghanaian Cedi
GIP	Gibraltar Pound
GMD	Gambian Dalasi
GNF	Guinea Franc
GTQ	Guatemalan Quetzal
GYD	Guyanaese Dollar
HKD	Hong Kong Dollar
HNL	Honduran Lempira
HRK	Croatian Kuna
HTG	Haiti Gourde
HUF	Hungarian Forint
IDR	Indonesian Rupiah
ILS	Israeli Shekel
INR	Indian Rupee
IQD	Iraqi Dinar
IRR	Iranian Rial
ISK	Icelandic Krona
JMD	Jamaican Dollar
JOD	Jordanian Dinar
JPY	Japanese Yen
KES	Kenyan Shilling
KGS	Kyrgystani Som
KHR	Cambodian Riel
KMF	Comorian Franc
KPW	North Korean Won
KRW	South Korean Won
KWD	Kuwaiti Dinar
KYD	Cayman Islands Dollar
KZT	Kazakhstan Tenge
LAK	Laotian Kip
LBP	Lebanese Pound
LKR	Sri Lankan Rupee
LRD	Liberian Dollar
LSL	Lesotho Loti
LYD	Libyan Dinar
MAD	Moroccan Dirham
MDL	Moldovan Leu
MGA	Malagasy Ariary
MKD	Macedonian Denar
MMK	Myanma Kyat
MNT	Mongolian Tugrik
MOP	Macau Pataca
MRO	Mauritanian Ouguiya
MUR	Mauritian Rupee
MVR	Maldivian Rufiyaa
MWK	Malawi Kwacha
MXN	Mexican Peso
MYR	Malaysian Ringgit
MZN	Mozambican Metical
NAD	Namibian Dollar
NGN	Nigerian Naira
NIO	Nicaragua Cordoba
NOK	Norwegian Krone
NPR	Nepalese Rupee
NZD	New Zealand Dollar
OMR	Omani Rial
PAB	Panamanian Balboa
PEN	Peruvian Nuevo Sol
PGK	Papua New Guinean Kina
PHP	Philippine Peso
PKR	Pakistani Rupee
PLN	Polish Zloty
PYG	Paraguayan Guarani
QAR	Qatari Riyal
RON	Romanian Leu
RSD	Serbian Dinar
RUB	Russian Ruble
RWF	Rwanda Franc
SAR	Saudi Riyal
SBD	Solomon Islands Dollar
SCR	Seychellois Rupee
SDG	Sudanese Pound
SEK	Swedish Krona
SGD	Singapore Dollar
SHP	Saint Helena Pound
SLL	Sierra Leonean Leone
SOS	Somali Shilling
SRD	Surinamese Dollar
SSP	South Sudanese Pound
STD	Sao Tome and Principe Dobra
SYP	Syrian Pound
SZL	Swazi Lilangeni
THB	Thai Baht
TJS	Tajikistan Somoni
TMT	Turkmenistani Manat
TND	Tunisian Dinar
TOP	Tonga Paanga
TRY	Turkish Lira
TTD	Trinidad and Tobago Dollar
TWD	New Taiwan Dollar
TZS	Tanzanian Shilling
UAH	Ukrainian Hryvnia
UGX	Ugandan Shilling
USD	United States Dollar
UYU	Uruguayan Peso
UZS	Uzbekistan Som
VEF	Venezuelan Bolivar
VND	Vietnamese Dong
VUV	Vanuatu Vatu
WST	Samoan Tala
XAF	Central African CFA franc
XCD	East Caribbean Dollar
XOF	West African CFA franc
XPF	CFP Franc
YER	Yemeni Rial
ZAR	South African Rand
ZMW	Zambian Kwacha
"""


def convert_currency(
    from_: str = "USD", to: str = "INR", amount: float = 1.0, api_key: str = ""
) -> str:
    """https://www.amdoren.com/currency-api/"""
    # Instead of manually generating parameters
    params = locals()
    # from is a reserved keyword
    params["from"] = params.pop("from_")
    res = requests.get(URL_BASE, params=params).json()
    return str(res["amount"]) if res["error"] == 0 else res["error_message"]


if __name__ == "__main__":
    TESTING = os.getenv("CI", "")
    API_KEY = os.getenv("AMDOREN_API_KEY", "")

    if not API_KEY and not TESTING:
        raise KeyError(
            "API key must be provided in the 'AMDOREN_API_KEY' environment variable."
        )

    print(
        convert_currency(
            input("Enter from currency: ").strip(),
            input("Enter to currency: ").strip(),
            float(input("Enter the amount: ").strip()),
            API_KEY,
        )
    )
