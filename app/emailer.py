# emailer.py (Versión SendGrid - Funciona en Cloud Run)
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import logging

logger = logging.getLogger(__name__)

# Configura tu API KEY (Obtenida de SendGrid)
# NO pongas la clave directamente aquí, usa variables de entorno en Cloud Run
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
SENDER_EMAIL = "ymejia@cci.com.do"  # Tu correo corporativo verificado

def send_email(to: list[str], subject: str, html: str):
    """
    Envía email usando la API de SendGrid (Estándar para Cloud Run).
    """
    if not SENDGRID_API_KEY:
        logger.error("❌ Falta la SENDGRID_API_KEY. Configura la variable de entorno.")
        raise Exception("SendGrid API Key missing")

    message = Mail(
        from_email=SENDER_EMAIL,
        to_emails=to,
        subject=subject,
        html_content=html
    )

    try:
        logger.info(f"Intentando enviar email a {to} vía SendGrid...")
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        
        # SendGrid devuelve 202 (Accepted) cuando todo está bien
        if response.status_code in [200, 201, 202]:
            logger.info(f"✅ Email enviado correctamente. Status: {response.status_code}")
        else:
            logger.error(f"⚠️ SendGrid respondió con error: {response.status_code}")
            
    except Exception as e:
        logger.error(f"❌ Error enviando email con SendGrid: {e}")
        raise e
