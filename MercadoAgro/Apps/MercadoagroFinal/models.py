from django.db import models

# Create your models here.
class usuario(models.Model):
	id_usuario = models.CharField(max_length = 35, unique = True)
	nombre = models.CharField(max_length = 35)
	apellido= models.CharField(max_length = 35)
	zona_rural= models.CharField(max_length = 35)
	telefono= models.CharField(max_length = 35)
	correo= models.EmailField(max_length = 254)
	contraseña= models.CharField(max_length = 35)
	tipo_usuario= models.CharField(max_length = 35)

	def informacion(self):
		cadena = "{0} {1}"
		return cadena.format(self.id_usuario, self.nombre)

	def __str__(self):
		return self.informacion()

class producto(models.Model):
	id_usuario = models.ForeignKey(usuario, null = False, blank = False, on_delete=models.CASCADE)
	id_producto = models.CharField(max_length = 35, unique = True)
	nombre_producto = models.CharField(max_length = 35)
	precio = models.CharField(max_length = 35)

	def inf_producto(self):
		cadena = "{1} {2} {3}"
		return cadena.format(self.id_usuario,self.id_producto,self.nombre_producto, self.precio)

	def __str__(self):
		return self.inf_producto()

class compra(models.Model):
	id_usuario = models.ForeignKey(usuario, null = False, blank = False, on_delete=models.CASCADE)
	id_producto = models.ForeignKey(producto, null = False, blank = False, on_delete=models.CASCADE)
	id_compra = models.CharField(max_length = 35, unique = True)
	valor = models.CharField(max_length = 35)

	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.id_usuario,self.id_producto)
		