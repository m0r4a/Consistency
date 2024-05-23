import ipaddress
import sys


def ip_address_checker(ip_address_string):

    if ipaddress.ip_address(ip_address_string):
        print("It\'s indeed an IP address!")
        exit(0)
    else:
        print("It\'s not an IP address!")
        exit(1)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        inp = input("Enter an IP address: ")
        ip_address_checker(inp)

    else:
        ip_address_checker(sys.argv[1])
