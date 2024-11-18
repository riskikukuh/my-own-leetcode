import math

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reversed = 0
    number = x
    # Do reverse with math
    while number > 0:
        reversed = (reversed * 10) + (number % 10)
        number = math.floor(number / 10)
    return reversed == x

def isPalindromeWithString(x: int) -> bool:
    if x < 0:
        return False
    temp = str(x)
    reverse = temp[::-1]    
    return reverse == str(x)

if __name__ == "__main__":
    input = 123321
    res = isPalindromeWithString(input)
    print(res)