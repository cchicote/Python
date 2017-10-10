#! python2.7.13
# archiver.py - generates an archive of the given folder
# usage: archiver <to_archive>
#        archiver <to_archive> <dest_folder>
# IMPORTANT: If you don't give any destination folder, the archive will be created
#            in the same repository than the file to archive
# WARNING: You must give the absolute path of the <to_archive> folder

from __future__ import print_function
import logging, os, sys, zipfile
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def archiver():
    # Checking the arguments
    logging.debug("Checking the arguments")
    if (len(sys.argv) < 2 or len(sys.argv) > 3):
        raise Exception("\n\n\nusage: archiver <to_archive>\n       archiver <to_archive> <dest_folder>\nYou must give the absolute path of the <to_archive> folder\nIf you don't give any destination folder, the archive will be created in the same repository than the file to archive\n\n")
    logging.debug("Arguments OK")

    # Values assignment
    logging.debug("Values assignment")
    path = os.path.abspath(sys.argv[1])
    if (not os.path.exists(path)):
        raise Exception("Can't find the folder %s" % (path))

    dest_path = path
    if (len(sys.argv) == 3):
        if (not os.path.exists(sys.argv[2])):
            raise Exception("Can't find the destination %s" % (sys.argv[2]))
        dest_path = sys.argv[2]
        
    number = 2
    zip_filename = os.path.join(os.path.abspath(dest_path), os.path.basename(path)) + '.zip'
    if (os.path.exists(zip_filename)):
        while True:
            zip_filename = os.path.join(os.path.abspath(dest_path), os.path.basename(path)) + '_' + str(number) + '.zip'
            if (not os.path.exists(zip_filename)):
                break
            number += 1
    zip_filename = os.path.basename(zip_filename)
    logging.debug("Values OK")
    
    os.chdir(os.path.dirname(path))

    logging.debug("Archive's name: %s" % (zip_filename))
    logging.debug("From: %s" % (os.path.dirname(path)))
    logging.debug("To: %s" % (dest_path))

    logging.debug("Creating %s" % (zip_filename))
    zip_file = zipfile.ZipFile(os.path.join(dest_path, zip_filename), 'w')
    for foldername, subfolders, filenames in os.walk(os.path.basename(path)):
        logging.debug("Adding %s to the archive" % (foldername))
        zip_file.write(foldername)
        logging.debug("Success")
        for filename in filenames:
            new_base = os.path.basename(zip_filename) + '_'
            logging.debug("Adding %s to the archive" % (filename))
            zip_file.write(os.path.join(foldername, filename))
            logging.debug("Success")
            
    zip_file.close()
    logging.debug("Done")
    
try:
    archiver()
except Exception as err:
    print("An exception happened: " + str(err))
logging.debug('End of program')
os.system("pause")
