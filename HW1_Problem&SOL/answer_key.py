import math
digit_1 = 7
digit_2 = 7
digit_3 = 4
digit_4 = 0
digit_5 = 9
digit_6 = 7
digit_7 = 6
digit_8 = 8
digit_9 = 3

def phone_number_function(digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9):
    double_digit_1 = (digit_9 * 2) +1
    double_digit_2 = (digit_7 * 2) +1
    double_digit_3 = (digit_5 * 2) +1
    double_digit_4 = (digit_3 * 2) +1
    double_digit_5 = (digit_1 * 2) +1
    plus_three_digit_1 = digit_8 + 3
    plus_three_digit_2 = digit_6 + 3
    plus_three_digit_3 = digit_4 + 3
    plus_three_digit_4 = digit_2 + 3
    if double_digit_1 > 9:
        double_digit_1 = double_digit_1 - 9
    else:
        double_digit_1
    if double_digit_2 > 9:
        double_digit_2 = double_digit_2 - 9
    else:
        double_digit_2
    if double_digit_3 > 9:
        double_digit_3 = double_digit_3 - 9
    else:
        double_digit_3
    if double_digit_4 > 9:
        double_digit_4 = double_digit_4 - 9
    else:
        double_digit_4
    if double_digit_5 > 9:      
        double_digit_5 = double_digit_5 - 9
    else:
        double_digit_5
    if plus_three_digit_1 > 9:
        plus_three_digit_1 = plus_three_digit_1 - 9
    else:
        plus_three_digit_1
    if plus_three_digit_2 > 9:
        plus_three_digit_2 = plus_three_digit_2 - 9
    else:
        plus_three_digit_2
    if plus_three_digit_3 > 9:
        plus_three_digit_3 = plus_three_digit_3 - 9
    else:
        plus_three_digit_3
    if plus_three_digit_4 > 9:
        plus_three_digit_4 = plus_three_digit_4 - 9
    else:
        plus_three_digit_4
    check_digit = math.fabs((double_digit_1 + plus_three_digit_1 - double_digit_2 + plus_three_digit_2 - double_digit_3 + plus_three_digit_3 - double_digit_4 + plus_three_digit_4 - double_digit_5) % 10)
    #this step is necessary because math.fabs returns a float, and for the phone number we need an integer.
    check_digit_int = int(check_digit)
    return str(digit_1) + str(digit_2) + str(digit_3) + str(digit_4) + str(digit_5) + str(digit_6) + str(digit_7) + str(digit_8) + str(digit_9) + str(check_digit_int)

print(phone_number_function(digit_1, digit_2, digit_3, digit_4, digit_5, digit_6, digit_7, digit_8, digit_9))