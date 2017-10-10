#! python2.7.13
# stopwatch.py

import logging, time
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

start = time.time()
try:
    while True:
        #print((str(time.time()) + " PRESS CTRL+C TO STOP THIS").center(50, '-'))
        print((str(round(time.time() - start, 2)) + " PRESS CTRL+C TO STOP THIS").center(50, '-'))
except KeyboardInterrupt:
    end = time.time()
    print("\nYou've let this program run for " + str(round(end - start, 2)) + " seconds.")
    print("Which corresponds to " + str(int(round(end - start, 2) / 60)) + " minutes and " + str(round(end - start, 2) % 60)) + " seconds."

logging.debug('End of program')
