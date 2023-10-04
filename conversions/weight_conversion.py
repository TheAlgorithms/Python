"""
Conversion of weight units.

__author__ = "Anubhav Solanki"
__license__ = "MIT"
__version__ = "1.1.0"
__maintainer__ = "Anubhav Solanki"
__email__ = "anubhavsolanki0@gmail.com"

USAGE :
-> Import this file into their respective project.
-> Use the function weight_conversion() for conversion of weight units.
-> Parameters :
    -> from_type : From which type you want to convert
    -> to_type : To which type you want to convert
    -> value : the value which you want to convert

REFERENCES :

-> Wikipedia reference: https://en.wikipedia.org/wiki/Kilogram
-> Wikipedia reference: https://en.wikipedia.org/wiki/Gram
-> Wikipedia reference: https://en.wikipedia.org/wiki/Millimetre
-> Wikipedia reference: https://en.wikipedia.org/wiki/Tonne
-> Wikipedia reference: https://en.wikipedia.org/wiki/Long_ton
-> Wikipedia reference: https://en.wikipedia.org/wiki/Short_ton
-> Wikipedia reference: https://en.wikipedia.org/wiki/Pound
-> Wikipedia reference: https://en.wikipedia.org/wiki/Ounce
-> Wikipedia reference: https://en.wikipedia.org/wiki/Fineness#Karat
-> Wikipedia reference: https://en.wikipedia.org/wiki/Dalton_(unit)
-> Wikipedia reference: https://en.wikipedia.org/wiki/Stone_(unit)
"""

KILOGRAM_CHART: dict[str, float] = {
    "kilogram": 1,
    "gram": pow(10, 3),
    "milligram": pow(10, 6),
    "metric-ton": pow(10, -3),
    "long-ton": 0.0009842073,
    "short-ton": 0.0011023122,
    "pound": 2.2046244202,
    "stone": 0.1574731728,
    "ounce": 35.273990723,
    "carrat": 5000,
    "atomic-mass-unit": 6.022136652e26,
}

WEIGHT_TYPE_CHART: dict[str, float] = {
    "kilogram": 1,
    "gram": pow(10, -3),
    "milligram": pow(10, -6),
    "metric-ton": pow(10, 3),
    "long-ton": 1016.04608,
    "short-ton": 907.184,
    "pound": 0.453592,
    "stone": 6.35029,
    "ounce": 0.0283495,
    "carrat": 0.0002,
    "atomic-mass-unit": 1.660540199e-27,
}


def weight_conversion(from_type: str, to_type: str, value: float) -> float:
    """
    Conversion of weight unit with the help of KILOGRAM_CHART

    "kilogram" : 1,
    "gram" : pow(10, 3),
    "milligram" : pow(10, 6),
    "metric-ton" : pow(10, -3),
    "long-ton" : 0.0009842073,
    "short-ton" : 0.0011023122,
    "pound" : 2.2046244202,
    "stone": 0.1574731728,
    "ounce" : 35.273990723,
    "carrat" : 5000,
    "atomic-mass-unit" : 6.022136652E+26

    >>> weight_conversion("kilogram","kilogram",4)
    4
    >>> weight_conversion("kilogram","gram",1)
    1000
    >>> weight_conversion("kilogram","milligram",4)
    4000000
    >>> weight_conversion("kilogram","metric-ton",4)
    0.004
    >>> weight_conversion("kilogram","long-ton",3)
    0.0029526219
    >>> weight_conversion("kilogram","short-ton",1)
    0.0011023122
    >>> weight_conversion("kilogram","pound",4)
    8.8184976808
    >>> weight_conversion("kilogram","stone",5)
    0.7873658640000001
    >>> weight_conversion("kilogram","ounce",4)
    141.095962892
    >>> weight_conversion("kilogram","carrat",3)
    15000
    >>> weight_conversion("kilogram","atomic-mass-unit",1)
    6.022136652e+26
    >>> weight_conversion("gram","kilogram",1)
    0.001
    >>> weight_conversion("gram","gram",3)
    3.0
    >>> weight_conversion("gram","milligram",2)
    2000.0
    >>> weight_conversion("gram","metric-ton",4)
    4e-06
    >>> weight_conversion("gram","long-ton",3)
    2.9526219e-06
    >>> weight_conversion("gram","short-ton",3)
    3.3069366000000003e-06
    >>> weight_conversion("gram","pound",3)
    0.0066138732606
    >>> weight_conversion("gram","stone",4)
    0.0006298926912000001
    >>> weight_conversion("gram","ounce",1)
    0.035273990723
    >>> weight_conversion("gram","carrat",2)
    10.0
    >>> weight_conversion("gram","atomic-mass-unit",1)
    6.022136652e+23
    >>> weight_conversion("milligram","kilogram",1)
    1e-06
    >>> weight_conversion("milligram","gram",2)
    0.002
    >>> weight_conversion("milligram","milligram",3)
    3.0
    >>> weight_conversion("milligram","metric-ton",3)
    3e-09
    >>> weight_conversion("milligram","long-ton",3)
    2.9526219e-09
    >>> weight_conversion("milligram","short-ton",1)
    1.1023122e-09
    >>> weight_conversion("milligram","pound",3)
    6.6138732605999995e-06
    >>> weight_conversion("milligram","ounce",2)
    7.054798144599999e-05
    >>> weight_conversion("milligram","carrat",1)
    0.005
    >>> weight_conversion("milligram","atomic-mass-unit",1)
    6.022136652e+20
    >>> weight_conversion("metric-ton","kilogram",2)
    2000
    >>> weight_conversion("metric-ton","gram",2)
    2000000
    >>> weight_conversion("metric-ton","milligram",3)
    3000000000
    >>> weight_conversion("metric-ton","metric-ton",2)
    2.0
    >>> weight_conversion("metric-ton","long-ton",3)
    2.9526219
    >>> weight_conversion("metric-ton","short-ton",2)
    2.2046244
    >>> weight_conversion("metric-ton","pound",3)
    6613.8732606
    >>> weight_conversion("metric-ton","ounce",4)
    141095.96289199998
    >>> weight_conversion("metric-ton","carrat",4)
    20000000
    >>> weight_conversion("metric-ton","atomic-mass-unit",1)
    6.022136652e+29
    >>> weight_conversion("long-ton","kilogram",4)
    4064.18432
    >>> weight_conversion("long-ton","gram",4)
    4064184.32
    >>> weight_conversion("long-ton","milligram",3)
    3048138240.0
    >>> weight_conversion("long-ton","metric-ton",4)
    4.06418432
    >>> weight_conversion("long-ton","long-ton",3)
    2.999999907217152
    >>> weight_conversion("long-ton","short-ton",1)
    1.119999989746176
    >>> weight_conversion("long-ton","pound",3)
    6720.000000049448
    >>> weight_conversion("long-ton","ounce",1)
    35840.000000060514
    >>> weight_conversion("long-ton","carrat",4)
    20320921.599999998
    >>> weight_conversion("long-ton","atomic-mass-unit",4)
    2.4475073353955697e+30
    >>> weight_conversion("short-ton","kilogram",3)
    2721.5519999999997
    >>> weight_conversion("short-ton","gram",3)
    2721552.0
    >>> weight_conversion("short-ton","milligram",1)
    907184000.0
    >>> weight_conversion("short-ton","metric-ton",4)
    3.628736
    >>> weight_conversion("short-ton","long-ton",3)
    2.6785713457296
    >>> weight_conversion("short-ton","short-ton",3)
    2.9999999725344
    >>> weight_conversion("short-ton","pound",2)
    4000.0000000294335
    >>> weight_conversion("short-ton","ounce",4)
    128000.00000021611
    >>> weight_conversion("short-ton","carrat",4)
    18143680.0
    >>> weight_conversion("short-ton","atomic-mass-unit",1)
    5.463186016507968e+29
    >>> weight_conversion("pound","kilogram",4)
    1.814368
    >>> weight_conversion("pound","gram",2)
    907.184
    >>> weight_conversion("pound","milligram",3)
    1360776.0
    >>> weight_conversion("pound","metric-ton",3)
    0.001360776
    >>> weight_conversion("pound","long-ton",2)
    0.0008928571152432
    >>> weight_conversion("pound","short-ton",1)
    0.0004999999954224
    >>> weight_conversion("pound","pound",3)
    3.0000000000220752
    >>> weight_conversion("pound","ounce",1)
    16.000000000027015
    >>> weight_conversion("pound","carrat",1)
    2267.96
    >>> weight_conversion("pound","atomic-mass-unit",4)
    1.0926372033015936e+27
    >>> weight_conversion("stone","kilogram",5)
    31.751450000000002
    >>> weight_conversion("stone","gram",2)
    12700.58
    >>> weight_conversion("stone","milligram",3)
    19050870.0
    >>> weight_conversion("stone","metric-ton",3)
    0.01905087
    >>> weight_conversion("stone","long-ton",3)
    0.018750005325351003
    >>> weight_conversion("stone","short-ton",3)
    0.021000006421614002
    >>> weight_conversion("stone","pound",2)
    28.00000881870372
    >>> weight_conversion("stone","ounce",1)
    224.00007054835967
    >>> weight_conversion("stone","carrat",2)
    63502.9
    >>> weight_conversion("ounce","kilogram",3)
    0.0850485
    >>> weight_conversion("ounce","gram",3)
    85.0485
    >>> weight_conversion("ounce","milligram",4)
    113398.0
    >>> weight_conversion("ounce","metric-ton",4)
    0.000113398
    >>> weight_conversion("ounce","long-ton",4)
    0.0001116071394054
    >>> weight_conversion("ounce","short-ton",4)
    0.0001249999988556
    >>> weight_conversion("ounce","pound",1)
    0.0625000000004599
    >>> weight_conversion("ounce","ounce",2)
    2.000000000003377
    >>> weight_conversion("ounce","carrat",1)
    141.7475
    >>> weight_conversion("ounce","atomic-mass-unit",1)
    1.70724563015874e+25
    >>> weight_conversion("carrat","kilogram",1)
    0.0002
    >>> weight_conversion("carrat","gram",4)
    0.8
    >>> weight_conversion("carrat","milligram",2)
    400.0
    >>> weight_conversion("carrat","metric-ton",2)
    4.0000000000000003e-07
    >>> weight_conversion("carrat","long-ton",3)
    5.9052438e-07
    >>> weight_conversion("carrat","short-ton",4)
    8.818497600000002e-07
    >>> weight_conversion("carrat","pound",1)
    0.00044092488404000004
    >>> weight_conversion("carrat","ounce",2)
    0.0141095962892
    >>> weight_conversion("carrat","carrat",4)
    4.0
    >>> weight_conversion("carrat","atomic-mass-unit",4)
    4.8177093216e+23
    >>> weight_conversion("atomic-mass-unit","kilogram",4)
    6.642160796e-27
    >>> weight_conversion("atomic-mass-unit","gram",2)
    3.321080398e-24
    >>> weight_conversion("atomic-mass-unit","milligram",2)
    3.3210803980000002e-21
    >>> weight_conversion("atomic-mass-unit","metric-ton",3)
    4.9816205970000004e-30
    >>> weight_conversion("atomic-mass-unit","long-ton",3)
    4.9029473573977584e-30
    >>> weight_conversion("atomic-mass-unit","short-ton",1)
    1.830433719948128e-30
    >>> weight_conversion("atomic-mass-unit","pound",3)
    1.0982602420317504e-26
    >>> weight_conversion("atomic-mass-unit","ounce",2)
    1.1714775914938915e-25
    >>> weight_conversion("atomic-mass-unit","carrat",2)
    1.660540199e-23
    >>> weight_conversion("atomic-mass-unit","atomic-mass-unit",2)
    1.999999998903455
    """
    if to_type not in KILOGRAM_CHART or from_type not in WEIGHT_TYPE_CHART:
        msg = (
            f"Invalid 'from_type' or 'to_type' value: {from_type!r}, {to_type!r}\n"
            f"Supported values are: {', '.join(WEIGHT_TYPE_CHART)}"
        )
        raise ValueError(msg)
    return value * KILOGRAM_CHART[to_type] * WEIGHT_TYPE_CHART[from_type]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
