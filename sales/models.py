from django.db import models

class sale(models.Model):
    data = models.DateField()
    produto = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f'{self.produto} - {self.data}'
