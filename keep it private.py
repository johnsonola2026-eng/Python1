class myclass:
    __privatevar=27;
    def __privmeth(self):
        print("i'm inside myclass")
    def hello(self):
            print("private variablevalue:",myclass.__privatevar)
foo=myclass()
foo.hello()