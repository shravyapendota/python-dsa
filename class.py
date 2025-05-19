class Emp:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def dsply(self):
        print(self.name)
        print(self.id)


e1=Emp("shrav", 101)
e1.dsply()
e2=Emp("ks", 102)
e2.dsply()
