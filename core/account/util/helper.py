import re
from rest_framework.serializers import ValidationError

numbers_dict = {
    '۰': '0',
    '۱': '1',
    '۲': '2',
    '۳': '3',
    '۴': '4',
    '۵': '5',
    '۶': '6',
    '۷': '7',
    '۸': '8',
    '۹': '9'
}

def to_english(text):
    for i, j in numbers_dict.items():
        text = text.replace(i, j)
    return text


def validate_national_id(value, raise_exception=True, accept_11_digit_id=False):
    value = str(value)
    if re.search(r'^[0-9]{11}$', value) and accept_11_digit_id:
        return to_english(value)
    if re.search(r'^[0-9]{10}$', value):
        check = int(value[9])
        s = sum([int(value[x]) * (10 - x) for x in range(9)]) % 11
        if (s < 2 and check == s) or (s >= 2 and check + s == 11):
            return to_english(value)
    if raise_exception:
        raise ValidationError("کد ملی معتبر نیست.")
    return False