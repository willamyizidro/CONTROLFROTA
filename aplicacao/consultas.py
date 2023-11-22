from .models import *

def verifica_nome_usuario(nome):
    try:
        user = Usuario.objects.get(usuario = nome)
        return True
    except Usuario.DoesNotExist:
        return False
    

def verifica_email_usuario(email):
    try:
        user = Usuario.objects.get(email = email)
        return True
    except Usuario.DoesNotExist:
        return False