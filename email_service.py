import smtplib
import random
import string
from email.mime.text import MIMEText
from config import EMAIL_REMETENTE, EMAIL_SENHA_APP, SMTP_HOST, SMTP_PORT


def gerar_senha_temporaria(tamanho=8):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))


def enviar_email_recuperacao(destinatario, nova_senha):
    assunto = "Recuperação de senha - Sistema Cadastro de Pessoas"
    corpo = f"""Olá,

Sua nova senha temporária é: {nova_senha}

Depois de entrar no sistema, altere sua senha.

Mensagem automática do sistema.
"""

    msg = MIMEText(corpo, "plain", "utf-8")
    msg["Subject"] = assunto
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = destinatario

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as servidor:
            servidor.starttls()
            servidor.login(EMAIL_REMETENTE, EMAIL_SENHA_APP)
            servidor.sendmail(EMAIL_REMETENTE, destinatario, msg.as_string())
    except smtplib.SMTPAuthenticationError:
        raise Exception("Falha de autenticação no Gmail. Verifique o e-mail remetente e a senha de app.")