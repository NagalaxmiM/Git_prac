def announce(f):
    def wrapper():
        print('About to run the function...')
        print('printing 2nd line')
        f()
        print('Done with the function..')
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
hello()
