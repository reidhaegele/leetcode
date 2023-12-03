def is_palindrome(x: int) -> bool:
    if x < 0: return False
    if x < 10: return True
    tens = 10
    new_num = x
    temp = 0
    while new_num >= 10:
        temp = temp * 10
        temp += new_num % tens
        new_num = new_num // tens
    temp = temp * 10
    temp += new_num
    return x == temp

if __name__ == '__main__':
    num = 123121
    print(is_palindrome(num))