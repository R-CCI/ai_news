import os
from redmail import gmail
import logging

# Configura el logger para ver qué pasa en la consola de Cloud Run
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- CONFIGURACIÓN CRÍTICA ---
# 1. Usa os.environ.get para leer las variables de Cloud Run
# 2. Si pruebas local, asegúrate de tener estas variables o descomentar las líneas de abajo para probar
username = os.environ.get("GMAIL_USERNAME") # Poner aquí tu @gmail.com PERSONAL
password = os.environ.get("GMAIL_PASSWORD") # Tu App Password

# Configuración de Redmail para Gmail estándar
gmail.username = username
gmail.password = password
gmail.smtp_host = "smtp.gmail.com"
gmail.smtp_port = 587           # Puerto estándar TLS
gmail.smtp_use_tls = True       # Encender TLS
gmail.smtp_use_ssl = False      # Apagar SSL (Importante para el puerto 587)

def send_email(to: list[str], subject: str, html: str):
    try:
        if not username or not password:
            logger.error("❌ Faltan las credenciales (GMAIL_USERNAME o GMAIL_PASSWORD)")
            return

        logger.info(f"📨 Conectando a Gmail como {username} para enviar a {to}...")
        
        # Enviando el correo
        gmail.send(
            subject=subject,
            receivers=to,
            html=html,
            sender=f"AI Newsletter <{username}>" # El remitente DEBE coincidir con el usuario
        )
        logger.info("✅ Correo entregado al servidor SMTP de Gmail")
        
    except Exception as e:
        logger.error(f"❌ Error fatal enviando correo: {e}")
        # Importante: No relanzamos el error para que la app no se caiga, 
        # pero queda registrado en los logs.
