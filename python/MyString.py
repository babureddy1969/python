#String manipulation
#helilo
class MyString:
    def __init__(self,s):
        self.mystring = s
        self.history = [s]
        self.currentPosition = 0
    def insert(self,pos,s):        
        self.mystring = self.mystring[:pos]+s+self.mystring[pos:]
        self.history+=[self.mystring]
        self.currentPostion += 1
    def delete(self,pos,n):
        #helilo
        self.mystring = self.mystring[:pos]+self.mystring[pos+n:]
        self.history+=[self.mystring]
        self.currentPostion += 1
    
    def undo(self):
        if self.currentPostion > 0:
            self.currentPosition -= 1
        self.mystring = self.history[self.currentPosition]
    def redo(self):
        if self.currentPosition +1 < len(history) - 1:
            self.currentPosition += 1
        self.mystring = self.history[self.currentPosition]
