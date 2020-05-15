import re

def find_all_titled_links(self_text):
    # url_pattern = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    # matches all occurrences of: [the-supergen-title](the-supergen_mynoise_url)
    text_url_pattern = r"(?i)(?<=\[)[^\]]+\]\(http[s]?://mynoise.net/supergenerator\.php[^\)]+(?=\))"
    matches = re.findall(text_url_pattern, self_text)
    return matches

def find_all_untitled_links(self_text):
    # todo: create pattern to match links without link text
    non_titled_url_pattern = r""
    matches = re.findall(non_titled_url_pattern, self_text)
    return matches
