import threading
from guiBot import *
from botHiLink import *

threading.Thread(target=gui).start()
threading.Thread(target=runBot).start()
