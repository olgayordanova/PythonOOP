import math


def roman_to_int(input):
    input = input.upper(  )
    nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    sum = 0
    for i in range(len(input)):
        try:
            value = nums[input[i]]
            if i+1 < len(input) and nums[input[i+1]] > value:
                sum -= value
            else: sum += value
        except:
            return f"cant convert"
    return sum

# def isInt_re(v):
#     import re
#     if not hasattr(isInt_re, 'intRegex'):
#         isInt_re.intRegex = re.compile(r"^([+-]?'[1-9]\d\'*|0)$")
#     #  r"^([+-]?[1-9]\d*|0)$"
#     return isInt_re.intRegex.match(str(v).strip()) is not None


class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        try:
            new_value = math.floor ( value )
        except:
            return "value is not a float"
        return Integer (new_value)

    @classmethod
    def from_roman(cls, value):
        new_value = roman_to_int(value)
        return Integer (new_value)

    @classmethod
    def from_string(cls, value):
        try:
            if not isinstance(value, str):
                raise ValueError('not string')
            return Integer ( int(value))
        except:
            return "wrong type"

    def add(self, integer):
        if not isinstance(integer, Integer):
            return "number should be an Integer instance"
        result = self.value + integer.value
        return result

    def __str__(self):
        return str(self.value)



first_num = Integer(10)
second_num = Integer.from_roman("IV")
second_integer = 12
print(Integer.from_float("2.6"))
print(Integer.from_string("10"))
print(Integer.from_string(1.5))

print(first_num.add ( second_integer ))

print(first_num.add(second_num))
