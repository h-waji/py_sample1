import time

def hello(name):
    print("Hello! My name is", name)

hello("Koshigaitai")

def get_name():
    return "Mario"

hello(get_name())

def hello_callback(callback):
    print('Hello! My name is', callback(), ": callback")

hello_callback(get_name)

def print_time():
    now = time.asctime()
    print("It is", now)

print_time()
