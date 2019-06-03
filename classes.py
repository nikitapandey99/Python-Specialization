class partyanimal:
    x=0

    def party(self):
        self.x=self.x+1
        print('So far',self.x)

an=partyanimal()  #creating an object of class partyanimal
an.party()        #invoking a method within the object
an.party()
an.party()
#can also be written as
partyanimal.party(an)
print(type(an))
print(dir(an))
