import re

def is_sri_lankan_phone_number(phone: str) -> bool:
    """
    Determine whether the string is a valid sri lankan phone number or not
    >>> is_sri_lankan_phone_number("+94475682163")
    True
    >>> is_sri_lankan_phone_number("+94773283048")
    True
    >>> is_sri_lankan_phone_number("0718382399")
    True
    >>> is_sri_lankan_phone_number("0094112343221")
    True
    >>> is_sri_lankan_phone_number("+94-3283048")
    False
    >>> is_sri_lankan_phone_number("07779209245")
    False
    >>> is_sri_lankan_phone_number("0957651234")
    False
    """

    pattern = re.compile(r'^(?:0|94|\+94|0{2}94)?(?:(1{2}|21|23|24|25|26|27|31|32|3{2}|34|35|36|37|38|41|45|47|51|52|54|5{2}|57|63|65|6{2}|67|81|91)(0|2|3|4|5|7|9)|7(0|1|2|4|5|6|7|8)\d)\d{6}$')    
    
    return bool(re.search(pattern, phone))

if __name__ == '__main__':
    phone = "+94475682163"

    print(is_sri_lankan_phone_number(phone))    
