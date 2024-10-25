from django.db import models

class Autor(models.Model):
    nome = models.CharField(max_length=255)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    ano_publicacao = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class LivroTag(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
