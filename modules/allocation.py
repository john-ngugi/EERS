import random

class Allocation:
    def __init__(self,emergency,resource,index):
        self.emergency = emergency
        self.resource = resource 
        self.index = index 

    def allocator(self):
        
        def randInt(a,b):
            val = random.randint(a,b)
            return val


        def resourceDispatcher():
            if self.index < 3:
                self.resource-= randInt(0,3)

            elif self.index < 6:
                self.resource -= randInt(3,9)
                print(self.resource)
            else:
                self.resource -= randInt(9,28)   
            
            return self.resource
        
        if self.emergency == 'Fire':
           resourceDispatcher()

        if self.emergency == 'Crime':
            resourceDispatcher()

        if self.emergency == 'Medical':
           resourceDispatcher()

        return self.resource    

                

                

  