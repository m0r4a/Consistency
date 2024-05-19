import sys


def palindrome(s):
    return s == s[::-1]


def test_palindrome():
    return palindrome(sys.argv[1])


if __name__ == '__main__':
    if test_palindrome():
        print('Is a palindrome!')
    else:
        print('Is not a palindrome!')
