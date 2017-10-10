#! python2.7.13
# feeling_lucky.py - Opens several Google search results.


from __future__ import print_function
import logging, os, sys, webbrowser, bs4, requests
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

logging.debug("Googling...")
res = requests.get("http://google.com/search?q=" + ' '.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

link_elems = soup.select('.r a')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open('http://google.com' + link_elems[i].get('href'))

logging.debug('End of program')
os.system("pause")
