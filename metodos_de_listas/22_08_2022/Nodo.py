class Nodo:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

    def __str__(self) -> str:
        return f'(data: {self.data}, next: {self.next})'
    
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data
    
    def set_next(self, next):
        self.next = next