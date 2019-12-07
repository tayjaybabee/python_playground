#! python3
import threading
from multiprocessing import Pool, Barrier
from typing import Any, Union
import time

import requests
import os
import bs4
import sys
from tqdm import trange, tqdm


def chunkify(url_nums, chunk_size):
    for item in range(0, len(url_nums), chunk_size):
        yield url_nums[item:item + chunk_size]


chunk_size = 150

# def progress(count, total, status=''):
#     bar_len = 60
#     filled_len = int(round(bar_len * count / float(total)))
#
#     percents = round(100.0 * count / float(total), 1)
#     bar = '=' * filled_len + '-' * (bar_len - filled_len)
#
#     sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
#     sys.stdout.flush()


url = 'http://xkcd.com/'
os.makedirs('xkcd', exist_ok=True)
url_list = []
valid_urls = []
invalid_urls = []


def results_of_chunk(valid, invalid):
    print(valid)
    print(invalid)





def process_chunks(chu):
    global tried
    global valid_urls
    global invalid_urls

    chunk_num = len(chu)
    chunk_num = int(chunk_num)
    for chunk_item in trange(0, chunk_num):
        url_to_test = chu[chunk_item]
        tried += 1
        try:
            req = requests.get(url_to_test)
            if req.status_code == 200:
                valid_urls.append(url_to_test)
            else:
                invalid_urls.append(url_to_test)

        except:

            print('Does not exist!')


res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text)

comicElem = soup.select('#comic img')
if not comicElem:
    print('Could not find comic image.')
else:
    comicUrl: Union[str, Any] = 'http:' + comicElem[0].get('src')
    print('Downloading image %s...' % comicUrl)
    res = requests.get(comicUrl)
    res.raise_for_status()

    # imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    # for chunk in res.iter_content(100000):
    #     imageFile.write(chunk)
    # imageFile.close()

prevLink = soup.select('a[rel="prev"]')[0]
tried = 0
number = prevLink.get('href')
number = number.replace('/', '')
num_int = int(number) + 3
number = str(num_int)
print(number)
for i in range(0, num_int):
    url_item = url + str(i) + '/'
    url_list.append(url_item)

f = open('urls.txt', 'wb')

chunked = list(chunkify(url_list, chunk_size))
progress_bar_overall = tqdm(chunked)
for chunk in progress_bar_overall:
    progress_bar_overall.set_description(f'Checking chunks....')
    threading.Thread(target=process_chunks(chunk))


print(valid_urls)
status = str(len(valid_urls)) + '/' + str(tried)
formatted_stats = status + ' attempted URL connections'


if len(invalid_urls) >= 1:
    print('Here are the invalid url numbers: %s' % invalid_urls)
else:
    print('No URLs failed!')

print(formatted_stats)

#     url = 'http://xkcd.com' + prevLink.get('href')
#
# print('Done.')
