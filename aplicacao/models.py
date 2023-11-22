from django.db import models
from datetime import date, timedelta


class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    usuario = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    senha = models.CharField(max_length=30)

    def __str__(self):
        return self.usuario
    


class Motorista(models.Model):
    nome = models.CharField(unique=True, max_length=30)
    endereco = models.CharField(max_length= 70, default="")
    cnh = models.CharField(max_length=5)
    
 
    def __str__(self):
        return self.nome
    

class Veiculo(models.Model):
    placa = models.CharField(unique=True ,max_length=7)
    chassi = models.CharField(unique=True ,max_length=17)
    marca = models.CharField(max_length= 15)
    modelo = models.CharField(max_length= 15)
    tara = models.IntegerField()
    tamanho = models.IntegerField()
    
    def __str__(self):
        return self.placa



class TipoManutencao(models.Model):
    produto = models.CharField(unique=True, max_length= 30)
    tempoTroca = models.IntegerField()
    kmTroca = models.IntegerField()
    valor = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.produto



class Manutencao(models.Model):
    manutencao = models.ForeignKey(TipoManutencao, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)
    dataAtual = models.DateField()
    kmAtual = models.IntegerField()
    dataProximaMan = models.DateField(null=True, blank=True)
    kmProximaMan = models.IntegerField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.dataProximaMan:
            intervalo_tempo = timedelta(days=self.manutencao.tempoTroca)
            self.dataProximaMan = self.dataAtual + intervalo_tempo
        if not self.kmProximaMan:
            self.kmProximaMan = self.kmAtual + self.manutencao.kmTroca
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Manutenção de {self.manutencao} para {self.veiculo}'

    
class Abastecimentos(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField()
    litros = models.DecimalField(max_digits=10, decimal_places=2)
    kmatual = models.IntegerField()
    km_anterior = models.IntegerField(null=True, blank=True)
    mediaVeiculo = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.km_anterior:
            ultimo_abastecimento = Abastecimentos.objects.filter(veiculo=self.veiculo).order_by('-kmatual','-data').first()
            
            if ultimo_abastecimento:
                self.km_anterior = ultimo_abastecimento.kmatual
            else:
                self.km_anterior = 0

        if self.km_anterior is not None and self.litros > 0:
            quilometros_percorridos = self.kmatual - self.km_anterior
            self.mediaVeiculo = quilometros_percorridos / self.litros
        else:
            self.mediaVeiculo = 0

        super().save(*args, **kwargs)