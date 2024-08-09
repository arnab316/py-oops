def greet(fx):
    def mfx():
        print("Good Moarning")
        fx()
        print("Thanks for using this function")
    return mfx


@greet
def hello():
    print("hello")

hello()