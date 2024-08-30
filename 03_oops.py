def greet(fx):
    #  *arg . **kwargs is for arguments functions
    def mfx(*args , **kwargs):
        print("Good Moarning")
        fx(*args , **kwargs)
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("hello")

# hello()

@greet
def add(a, b):
  print(a + b)



add(2, 1)
