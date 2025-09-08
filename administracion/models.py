from django.db import models

class  Rol(models.Model):
    nombre  = models.CharField(max_length = 200)
    creado = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.rol

class User(models.Model):
    NOMBRE = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    edad = models.IntegerField()
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,related_name="usuarios")
    sueldo = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.user
                              
    
    

    

    