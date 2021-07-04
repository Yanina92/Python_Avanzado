
class TemaConcreto(Tema):
	def __init__(self):
		self.estado = None
	def set_estado(self, value):
		self.estado = value
		self.notificar()
	def get_estado(self):
		return self.estado
		
class Observador():
	def update(self):
		raise NotImplementedError("Delegacion de actualizacion")
		
class ConcreteObserverA(Observador):
	def __init__(self, objeto):
		self.observado_a = objeto
		self.observador_a.agregar(self)
	def update(self):
		print("Actualizacion dentro de observador concreto A")
		self.estado = self.observador_a.get_estado()
		print("Estado = ", self.estado)
		
class ConcreteObserverB(Observador):
	def __init__(self, objeto):
		self.observado_b = objeto
		self.observador_b.agregar(self)
	def update(self):
		print("Actualizacion dentro de observador concreto B")
		self.estado = self.observador_b.get_estado()
		print("Estado = ", self.estado)
