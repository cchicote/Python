#! python2.7.13
# mapit.py - Launches a map in the browser using an address from the command line or clipboard.

from __future__ import print_function
import logging, webbrowser, sys, pyperclip
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
logging.disable(logging.CRITICAL)
logging.debug('Start of program')

# Get the address
if (len(sys.argv) > 1):
    logging.debug('Getting the address from the command line')
    address=' '.join(sys.argv[1:])
else:
    logging.debug('Getting the address from paperclip')
    address = pyperclip.paste()

# Open the map with the given address
logging.debug('Opening the web browser with the given address')
webbrowser.open('https://www.google.fr/maps/place/' + address)

logging.debug('End of program')
