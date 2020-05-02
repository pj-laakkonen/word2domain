# Testing
import requests

r = requests.get('http://127.0.0.1:8000/words/en', auth=('laakkonen.pj@gmail.com', 'Hani5640'), timeout=None)

data = r.json()

min_domain_length = 3
# max_domain_length = 63

# Testing -->

domain_ext = 'com'
domain_ext_length = len(domain_ext)

selected_domains = []

# Minimum Domain Name Length Is 3 Characters and Maximum is 63.

for word in data:
    chars = word["word"]
    chars_length = len(chars)
    last_chars = chars[-domain_ext_length:]

    if domain_ext == last_chars: #Smaller subset of words
        if chars_length >= (min_domain_length + domain_ext_length):
            domain = chars[:(chars_length-domain_ext_length)]
            domain_name = domain + '.' + last_chars
            selected_domains.append(domain_name)








