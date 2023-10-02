def intToRoman(num: int) -> str:
    roman_values = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M'
      }

    roman_str = ''
    # cria uma lista com as keys para conseguir percorrer ela de baixo pra cima
    lista_indices = list(roman_values.keys())
    for value in lista_indices[::-1]:
      while num >= value:
          roman_str += roman_values[value]
          num -= value
    return roman_str