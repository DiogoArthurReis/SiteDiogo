from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Usuario"

        def __str__(self):
            return f'{self.nome} {self.email} {self.telefone} {self.senha}'
        
class Vivencia(models.Model):
    titulo = models.CharField(max_length=100) 
    img = models.ImageField() 
    descricao = models.CharField(max_length=100) 

    class Meta:
        verbose_name_plural = "Vivencia"

        def __str__(self):
            return f'{self.titulo} {self.img} {self.descricao}'
        
class Comentario(models.Model):
    mensagem = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Comentario"

        def __str__(self):
            return f'{self.mensagem}'
        
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categoria"

        def __str__(self):
            return f'{self.nome}'
        
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    img = models.ImageField()

    class Meta:
        verbose_name_plural = "Produto"

        def __str__(self):
            return f'{self.nome} {self.categoria} {self.descricao} {self.img}'
        
class Receita(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    img = models.ImageField()

    class Meta:
        verbose_name_plural = "Receita"

        def __str__(self):
            return f'{self.nome} {self.categoria} {self.descricao} {self.img}'
        
class Pagina_Home(models.Model):
    nome_alergia = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Pagina_Home"

        def __str__(self):
            return f'{self.nome_alergia}'

class Pagina_Inicial(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.CharField(max_length=1000)

    class Meta:
        verbose_name_plural = "Pagina_Inicial"

        def __str__(self):
            return f'{self.titulo} {self.descricao}'