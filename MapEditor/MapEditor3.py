import sys
import time
from coreEditor import *

if __name__ == '__main__':
    try:
        mEditor = MapEditor('core.txt')
        mEditor.EditMap()
    except Exception, e:
        print e.message
        time.sleep(2.0)
        sys.exit(-1)
