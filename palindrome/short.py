if __name__ == '__main__':
    s = input("String: ")
    if s == s[::-1]:
        print('Is a palindrome!')
    else:
        print('Is not a palindrome!')