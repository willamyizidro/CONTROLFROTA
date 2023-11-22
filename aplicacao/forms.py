from django import forms
from .models import *



class UsuarioForm(forms.Form):
    nome = forms.CharField(label="nome", max_length=50)
    usuario = forms.CharField(label="usuario", max_length= 30)
    email = forms.EmailField(label="email", max_length=50, widget=forms.EmailInput)
    senha = forms.CharField(label="senha", max_length=30, min_length=8,  widget=forms.PasswordInput)
    conf_senha = forms.CharField(label="senha", max_length=30 , min_length=8,  widget=forms.PasswordInput)


class LoginForm(forms.Form):
    usuario = forms.CharField(label="usuario", max_length= 30)
    senha = forms.CharField(label="senha", max_length=30, min_length=8,  widget=forms.PasswordInput)


class MotoristaForm(forms.Form):
    nome = forms.CharField(label="text", max_length=50)
    endereco = forms.CharField(label='text', max_length=70)
    cnh = forms.CharField(label="text", max_length=5 )


class TipoManutencoesForms(forms.Form):
    produto = forms.CharField(label="text",max_length= 30)
    tempoTroca = forms.IntegerField()
    kmTroca = forms.IntegerField()
    valor = forms.DecimalField()

class ManutencaoFormCustom(TipoManutencoesForms):
    def __init__(self, manutencao, *args, **kwargs):
        super(ManutencaoFormCustom, self).__init__(*args, **kwargs)
        self.fields['produto'].initial = manutencao.produto
        self.fields['tempoTroca'].initial = manutencao.tempoTroca
        self.fields['kmTroca'].initial = manutencao.kmTroca
        self.fields['valor'].initial = manutencao.valor



class VeiculoForms(forms.Form):
    placa = forms.CharField(max_length=7, min_length=7)
    chassi = forms.CharField(max_length=17, min_length=17)
    marca = forms.CharField(max_length= 15)
    modelo = forms.CharField(max_length= 15)
    tara = forms.IntegerField()
    tamanho = forms.IntegerField()


class MotoristaFormCustom(MotoristaForm):
    def __init__(self, motorista, *args, **kwargs):
        super(MotoristaFormCustom, self).__init__(*args, **kwargs)
        self.fields['nome'].initial = motorista.nome
        self.fields['endereco'].initial = motorista.endereco
        self.fields['cnh'].initial = motorista.cnh


class VeiculoFormCustom(VeiculoForms):
    def __init__(self, veiculo, *args, **kwargs):
        super(VeiculoFormCustom, self).__init__(*args, **kwargs)
        self.fields['placa'].initial = veiculo.placa
        self.fields['chassi'].initial = veiculo.chassi
        self.fields['marca'].initial = veiculo.marca
        self.fields['modelo'].initial = veiculo.modelo
        self.fields['tara'].initial = veiculo.tara
        self.fields['tamanho'].initial = veiculo.tamanho



class InformarManutencaoForm(forms.ModelForm):
    dataAtual = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Manutencao
        fields = ['manutencao', 'veiculo', 'dataAtual', 'kmAtual', 'dataProximaMan', 'kmProximaMan']
     

    def __init__(self, *args, **kwargs):
        super(InformarManutencaoForm, self).__init__(*args, **kwargs)
        self.fields['manutencao'].queryset = TipoManutencao.objects.all()
        self.fields['veiculo'].queryset = Veiculo.objects.all()


class InformarManutencaoFormCustom(InformarManutencaoForm):


    def __init__(self, manutencaoext, *args, **kwargs):
        super(InformarManutencaoFormCustom, self).__init__(*args, **kwargs)
        self.initial['manutencao'] = manutencaoext.manutencao
        self.initial['veiculo'] = manutencaoext.veiculo
        self.initial['dataAtual'] = manutencaoext.dataAtual
        self.initial['kmAtual'] = manutencaoext.kmAtual

    
class InformarAbastecimentoForms(forms.ModelForm):
    data = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    litros = forms.DecimalField(max_digits=5, decimal_places=2,min_value=0)
    kmatual = forms.IntegerField(min_value=0)
    
    class Meta:
        model = Abastecimentos
        fields = ['veiculo', 'data', 'litros', 'kmatual']

    def __init__(self, *args, **kwargs):
        super(InformarAbastecimentoForms, self).__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()

class AbastecimentoFormCustom(InformarAbastecimentoForms):
    def __init__(self, abastecimento, *args, **kwargs):
        super(AbastecimentoFormCustom, self).__init__(*args, **kwargs)
        self.initial['veiculo'] = abastecimento.veiculo
        self.initial['data'] = abastecimento.data
        self.initial['litros'] = abastecimento.litros
        self.initial['kmatual'] = abastecimento.kmatual


class RelatorioForms(forms.ModelForm):
    class Meta:
        model = Abastecimentos
        fields = ['veiculo']
    def __init__(self, *args, **kwargs):
        super(RelatorioForms, self).__init__(*args, **kwargs)
        self.fields['veiculo'].queryset = Veiculo.objects.all()








    

        


