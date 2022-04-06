# given a string of space separated numbers, return the highest and lowest number.
# not yet refined for -ve numbers
def HighAndLow(string):
    string = string.replace(' ', '')
    numbers = [int(i) for i in string]
    high = numbers[-1]
    low = numbers[0]
    for i in numbers:
        if i < low:
            low = i
        if i > high:
            high = i
    return f"{high} {low}"


string = '7 4 3 5 9'
print(HighAndLow(string))
