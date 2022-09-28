class Printer:
    def __init__(self, ppm):
        #Al instanciar la clase lo que necesitamos pasar son las paginas por minuto
        self.page_rate = ppm 
		# páginas que la impresora imprime por minuto
        self.current_task = None
        #Tarea que se encuentra imprimiendo 
        self.time_remaining = 0
        #Tiempo restante para terminar la tarea

    def tick(self):
        if self.current_task is not None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60/self.page_rate