import random
import string


def helper_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))


def helper_email():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@gmail.com'


def helper_name():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
