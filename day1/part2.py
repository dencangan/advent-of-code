import re
from utils.parser import parse_input

input_list = parse_input('day1')

number_to_int = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
ans_list = []
regex = re.compile(r'\d|' + r"|".join(number_to_int))
regex_reverse = re.compile(r'\d|' + r"|".join(n[::-1] for n in number_to_int))
for line in input_list:
    start_digit = regex.search(line)
    start_digit = start_digit[0]
    end_digit = regex_reverse.search(line[::-1])[0]
    end_digit = end_digit[::-1]
    if start_digit.isalpha():
        start = str(number_to_int[start_digit])
    else:
        start = start_digit
    if end_digit.isalpha():
        end = str(number_to_int[end_digit])
    else:
        end = end_digit
    ans = start + end
    ans_list.append(int(ans))

print(sum(ans_list))



