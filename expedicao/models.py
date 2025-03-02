from django.db import models


class Carregamento(models.Model):
    TIPO_CHOICES = [
        ('carregamento', 'Carregamento'),
        ('descarregamento', 'Descarregamento'),
    ]

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='carregamento')
    data_carregamento = models.DateField()
    hora_carregamento = models.TimeField(default='00:00:00')  # Valor padrão corrigido
    numero_carregamento = models.CharField(max_length=100, unique=True)
    peso = models.FloatField()
    inicio_separacao_data = models.DateField(null=True, blank=True)
    inicio_separacao_hora = models.TimeField(null=True, blank=True)
    termino_separacao_data = models.DateField(null=True, blank=True)
    termino_separacao_hora = models.TimeField(null=True, blank=True)
    inicio_carregamento_data = models.DateField(null=True, blank=True)
    inicio_carregamento_hora = models.TimeField(null=True, blank=True)
    termino_carregamento_data = models.DateField(null=True, blank=True)
    termino_carregamento_hora = models.TimeField(null=True, blank=True)
    motorista = models.CharField(max_length=100, blank=True, null=True)
    conferente = models.CharField(max_length=100, blank=True, null=True)
    separador = models.CharField(max_length=100, blank=True, null=True)
    observacao = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.numero_carregamento