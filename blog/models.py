from django.db import models
from django.utils import timezone

# definicion del modelo (objeto)
class Post(models.Model): 
    # este es un vínculo con otro modelo
    author = models.ForeignKey('auth.User')
    #texto con un número limitado de caracteres
    title = models.CharField(max_length=200)
    #esto es para textos largos sin un límite
    text = models.TextField()
    #esto es fecha y hora
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    #def significa que se trata de una función o método. publish es el nombre del método. 
    #La regla es que usamos minúsculas y guiones bajos en lugar de espacios.
    #Los métodos muy a menudo devuelven algo. Hay un ejemplo de esto en el método __str__. 
    #En este escenario, cuando llamamos a __str__() obtendremos un texto (string) con un título de Post.

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
