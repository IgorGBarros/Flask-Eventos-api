from evento import Evento

class EventoOnline(Evento):
    def __init__(self, nome, local=""):
        local = f"https://tamarcado.com/eventos?id = {EventoOnline.id}"
        super().__init__(nome,local)

    def imprime_informacoes(self):
        print(f"ID do evento:", {self.id})
        print(f"Nome evento:", {self.nome})
        print(f"Link para acessar o evento:", {self.local})
        print("---------------")

