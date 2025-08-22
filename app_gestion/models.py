from django.db import models
from django.utils import timezone
# Create your models here.

opciones_consutas = [
    [0, 'Consulta'],   
    [1, 'Sugerencia'],
    [2, 'Reclamo'],
    [3, 'Petición'],
    [4, 'Queja'],
    [5, 'Felicitación'],   
    [6, 'Otro'],
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha = models.DateTimeField(default=timezone.now)
    tipoconsulta = models.IntegerField(choices=opciones_consutas, default=0)
    mensaje = models.TextField()
    avisos = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre
    

class Obituario(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_fallecimiento = models.DateField()
    mensaje = models.TextField()
    imagen = models.ImageField(upload_to='obituarios/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class DetalleObituario(models.Model):
    obituario = models.OneToOneField(Obituario, on_delete=models.CASCADE)
    lugar_exequias = models.CharField(max_length=100, blank=True)
    fecha_exequias = models.DateTimeField(blank=True, null=True)
    lugar_velatorio = models.CharField(max_length=100, blank=True)
    destino_final = models.CharField(max_length=100, blank=True)
    invitaciones = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"Detalle de {self.obituario.nombre}"


class Condolencia(models.Model):
    obituario = models.ForeignKey(Obituario, on_delete=models.CASCADE, related_name='condolencias')
    nombre_remitente = models.CharField(max_length=100)
    email_remitente = models.EmailField()
    telefono_remitente = models.CharField(max_length=15, blank=True, null=True)
    mensaje = models.TextField()
    fecha_envio = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Condolencia de {self.nombre_remitente} para {self.obituario.nombre}"


class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
