# stack data structure for regular people
class Paper:
    def __init__(self, next=None, value=None):
        self.next = next
        self.value = value
        

class Stack:
    def __init__(self):
        self.TOP = -1
    
    # inserts a Paper at the top of the stack
    def insert(self, value):
        self.TOP = Paper(next=self.TOP, value=value)

    # shifts the current top Paper to be the next (the one below)
    def pop(self):
        # stack is empty
        if self.TOP == -1:
            return -1
        
        else:
            popped_value = self.TOP.value
            self.TOP = self.TOP.next
            return popped_value
        
    # function that allows to check what the top element in the stack is
    def peek(self):
        return self.TOP.value
    
    # function for checking if the stack is empty
    def is_empty(self):
        return self.TOP == -1

       

# stack data structure for the extra cultured people
class Dolla_Dolla_Bill:
    def __init__(self, next_dolla=None, amount=None, dollas=None):
        self.TOP = next_dolla
        self.amount = amount
        self.dollas = dollas


class Stacks:
    def __init__(self):
        self.TOP = -1
    
    def stack_dolla(self, amount):
        # stacks the first dolla
        if self.TOP == -1:
            self.TOP = Dolla_Dolla_Bill(next_dolla=self.TOP, amount=amount, dollas=1)

        # stacks every other dolla
        else:
            if self.TOP.dollas % 2 == 0:
                print("dollar, dollar bill, Y'all")
            self.TOP = Dolla_Dolla_Bill(next_dolla=self.TOP, amount=amount, dollas=self.TOP.dollas + 1)
            
    def take(self):
        if self.TOP == -1:
            print('No dolla left')
            return -1

    def look(self):
        return self.TOP.amount
    
    def no_dollas(self):
        return self.TOP == -1
