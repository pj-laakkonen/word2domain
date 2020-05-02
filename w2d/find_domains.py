
def find_domains(data, domain_ext):
    min_domain_length = 3
    # max_domain_length = 63
    # domain_ext = 'io' # Testing

    domain_ext_length = len(domain_ext)
    selected_domains = []

    for word in data:
        chars = word['word']
        chars_length = len(chars)
        last_chars = chars[-domain_ext_length:]

        if domain_ext == last_chars:
            if chars_length >= (min_domain_length + domain_ext_length):
                domain = chars[:(chars_length-domain_ext_length)]
                domain_name = domain + '.' + last_chars
                selected_domains.append(domain_name)
    return selected_domains








