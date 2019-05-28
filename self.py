class Lazyproperty:
    def __init__(self,func):
        self.func=func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        setattr(instance,self.func.__name__,self.func(instance))
        return self.func(instance)

class Room:
    def __init__(self,name,width,length):
        self.name=name
        self.width=width
        self.length=length

    # @property  #area=property(area)
    @Lazyproperty
    def area(self):
        return self.width*self.length

r1=Room('bihu',1,2)
print(r1.area)
print(Room.area)