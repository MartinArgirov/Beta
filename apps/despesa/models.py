from django.db import models

# Create your models here.
class Despesa(models.Model):
    valor = models.CharField(max_length=10)
    categoria = models.CharField(max_length=30)
    #idade = models.IntegerField(blank=True, null=True) # assim não tem nenhum valor
    #idade = models.IntegerField(default=0)# coloca idade automaticamente
    mes = models.IntegerField()

    def __str__(self):
        #return self.valor
        #return f'{self.mes}: {self.valor}: {self.categoria}'
        return f'{self.mes}: {self.valor}'