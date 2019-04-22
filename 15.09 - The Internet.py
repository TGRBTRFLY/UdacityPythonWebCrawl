def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    excpept:
    return ""
