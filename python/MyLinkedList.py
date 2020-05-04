from functools import reduce

class MyLinkedList(object):
    def __init__(self):
        print('init')
        self.list = []
        self.current=0
        self.prev=0
    def next(self):
        print('next')
        self.list[self.current]
        if self.current == len(self.list)-1:
            self.current=0
        else:
            self.current+=1

    def prev(self):
        print('prev')
        if current > 0:
            self.list[self.current]
            self.current-=1
        elif current == 0:
            self.list[self.current]
            self.current = len(self.list-1)
    def insert(self,data):
        self.list.append(data)
    def remove(self,data):
        del self.list[self.list.index(data)]
    #def hasMore(self):
    #    return self.current>len(self.list)
    def __str__(self):
        return reduce(lambda x,y:str(x)+str(y) ,enumerate(self.list))
ll=MyLinkedList()
ll.insert(5)
ll.insert(10)
ll.insert(15)
print(ll)