from Nodo import Nodo


class List:
    def __init__(self) -> None:
        self.head = None

    def __str__(self) -> str:
        return f'{self.head}'

    def add(self, data):
        nodo = Nodo(data)
        nodo.next = self.head
        self.head = nodo
    
    def search(self,item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not found:
            return
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def is_empty(self):
        return self.head is None

    def size(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.get_next()
        return size

    def append(self,item):
        current = self.head
        previous = None
        while current is not None:
            previous = current
            current = current.get_next()
        current = Nodo(item)
        previous.set_next(current)

    def index(self,item):
        current = self.head
        index = 0
        found = False
        while current is not None:
            if current.get_data() == item:
                found = True
            index += 1
            current = current.get_next()
        if current is None and not found:
            return -1
        return index

    def insert(self, item, pos):
        current = self.head
        index = 0
        found = False
        previous = None
        new_nodo = Nodo(item)

        print(pos)
        if pos == 0:
            self.head = Nodo(item)
            self.head.set_next(current)
        else:
            while not found:
                if index == pos:
                    found = True
                else:
                    index += 1
                    previous = current
                    current = current.get_next()
            previous.set_next(new_nodo)
            new_nodo.set_next(current)
        
    def pop(self, pos = None):
        current = self.head
        index = 0
        found = False
        previous = None
        while current is not None and not found:
            if pos == index or (pos is None and index == self.size() - 1):
                found = True
            else:
                index = index + 1
                previous = current
                current = current.get_next()

        if previous is None:  
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return current


        


