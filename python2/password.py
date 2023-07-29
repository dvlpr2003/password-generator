import random 
# import suffler

class Password :
    def __init__(self,Capitals,Smaller,Symbols):
        self.Capitals =Capitals
        self.Smaller = Smaller
        self.Symbols = Symbols
        self.pas = []
    def generate(self):
        char = int(input("How many Uppercase you want ? : "))
        s_char = int(input("How many Lowercase you want ? : "))
        special_char = int(input("How many special character want ?: "))
        for _ in range(0,char):
            self.pas.append(random.choice(self.Capitals))
        for _ in range(0,s_char):
            self.pas.append(random.choice(self.Smaller))
        for _ in range(0,special_char):
          self.pas.append(random.choice(self.Symbols))
        



