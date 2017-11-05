import itertools
from web_spider_go import download

max_error = 5
num_error = 0
for page in itertools.count(1):
    url = 'http://example.webscraping.com/places/default/view/-%d' % page
    html = download(url)
    if html is None:
        num_error += 1
        if num_error == max_error:
            break
    else:
        num_error = 0
