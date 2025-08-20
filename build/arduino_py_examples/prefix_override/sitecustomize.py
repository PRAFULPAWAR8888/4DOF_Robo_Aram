import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/praful_pawar/arduinobot_ws/install/arduino_py_examples'
