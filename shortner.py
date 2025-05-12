import string
import random

url_mapping = {}

base62_chars = string.digits + string.ascii_letters

def generate_short_id(length=6):
    return ''.join(random.choice(base62_chars) for _ in range(length))

def shorten_url(long_url):
    short_id =generate_short_id()
    short_url = f"https://short.url/{short_id}"

    while short_url in url_mapping:
        short_id = generate_short_id()
        short_url = f"https://short.url/{short_id}"

    url_mapping[short_url] = long_url

    return short_url

def main():
    long_url = input("Input the long URL to be shortened: ")
    short_url = shorten_url(long_url)

    print(f"Short URL: {short_url}")

main()