#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(input_string):
    # Place code here - refer to function specifics in section below
    return input_string[0:5]


def last_seven(input_string):
    # Place code here - refer to function specifics in section below
    return input_string[-7:]

def middle_number(number):
    # Place code here - refer to function specifics in section below
    number = str(number)
    return number[1:3]

def first_three_last_three(str1, str2):
    # Place code here - refer to function specifics in section below
    str1 = str1[0:3]
    str2 = str2[-3:]
    substring = str1[0:3] + str2[-3:]
    return substring


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))

    