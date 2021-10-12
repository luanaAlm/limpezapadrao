from django.db import models


class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    mensagem = models.TextField()

    def __str__(self):
        template = '{0.nome} {0.email} {0.telefone} {0.mensagem}'
        return template.format(self)


class Limpeza(models.Model):
    ID_Limpeza = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    foto = models.URLField(max_length=200)


class Sofa(Limpeza):
    ID_Sofa = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Cama(Limpeza):
    ID_Cama = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Tapete(Limpeza):
    ID_Tapete = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Automovel(Limpeza):
    ID_Automovel = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Depoimento(models.Model):
    ID_Depoimento = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    foto = models.URLField(max_length=200)

    def __str__(self):
        return self.title


class Parceiro(models.Model):
    ID_Parceiro = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    foto = models.URLField(max_length=200)

    def __str__(self):
        return self.title
