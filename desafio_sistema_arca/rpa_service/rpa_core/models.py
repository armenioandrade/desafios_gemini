from django.db import models

class Cliente(models.Model):
    inscricao_estadual = models.CharField(max_length=200, null=False, blank=False, unique=True)
    cnpj = models.CharField(max_length=14, null=False, blank=False, unique=True)
    razao_social = models.CharField(max_length=200, null=False, blank=False)
    codigo_apelido = models.CharField(max_length=200, null=False, blank=False, unique=True)
    chave_api_dominio = models.CharField(max_length=200, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "Cliente para Consulta"
        verbose_name_plural = "Clientes para Consulta"

    def __str__(self):
        return f'CLIENTE{self.razao_social} cadastrado com sucesso!'