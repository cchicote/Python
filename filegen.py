#! python2.7.13
# filegen.py - creates a file with python header (those 2 commentaries on top of the file) at the given path
# usage: fg <absolute path> <filename>
#        fg <shortcut> <filename>
# Avalailable shortcuts: Desktop, Documents
# AMELIORATIONS EN VUE: rendre ce programme portable (ne plus dependre des mon path pour l'executable de l'IDLE)

from __future__ import print_function
import os, sys, subprocess, getpass

def filegen():
    # Displays usage if not enough arguments
    if (len(sys.argv) != 3):
        raise Exception('''usage: fg <absolute path> <filename>
                              fg <shortcut> <filename>
                       avalailable shortcuts: Desktop, Documents''')

    elif (len(sys.argv) == 3):

        path = sys.argv[1]
        # Checking if user typed a shortcut or an absolute path
        if (not path.startswith('C:\\')):
            if (path.lower() == 'desktop'):
               path = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\'
            elif (path.lower() == 'documents'):
                path = 'C:\\Users\\' + getpass.getuser() + '\\Documents\\'
            elif (path.lower() == 'python'):
                path = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\PYTHON\\'
            elif (path.lower() == 'tools'):
                path = 'C:\\Users\\' + getpass.getuser() + '\\Desktop\\PYTHON\\tools\\'
        
        # Checking if the given path exists
        if (os.path.exists(path)):
            
            # Checking if user typed the '.py' extension for the file
            filename = sys.argv[2]
            if (not filename.endswith('.py')):
                filename = filename + '.py'

            # Checking if the file already exists, and changing its name if it does
            if (os.path.exists(os.path.join(path, filename))):
                i = 2
                tmp = filename.split('.')
                name = tmp[0] + str(i)
                while True:
                    if (os.path.exists(os.path.join(path, name + '.py'))):
                        i += 1
                        name = name[:-len(str(i))]
                        name += str(i)
                    else:
                        tmp[0] = name
                        filename = '.'.join(tmp)
                        break
                    
            # Creates the file
            keyfile = open(os.path.join(path, filename), 'w')
            
            # Writing in the file
            keyfile.write('#! python' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) +
                          '.' + str(sys.version_info[2]) + '\n# ' + filename + '\n\nimport logging\n' +
                          "logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')\n" +
                          "#logging.disable(logging.CRITICAL)\n" +
                          "logging.debug('Start of program')\n\n\n\n" +
                          "logging.debug('End of program')")
            keyfile.close()
            
            # Success!
            print(filename + " successfully created in " + path)
            
            # Opening the file
            idle_path = r'C:\Python27\Lib\idlelib\idle.bat'
            subprocess.Popen("%s %s" % (idle_path, os.path.join(path, filename)))

        # Displays an error and exit the program if the given path doesn't exists
        else:
            raise Exception("this path doesn't exist")

try:
    filegen()
except Exception as err:
    print("An exception happened: " + str(err))
    os.system("pause")

    
