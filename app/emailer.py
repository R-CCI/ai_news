# emailer.py
import os
from dotenv import load_dotenv
from redmail import gmail
import logging

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger(__name__)

# Fetch credentials from environment variables
username = "ymejia@cci.com.do"
password = "dlpf vvwd smff rsij"

if not username or not password:
    logger.error("❌ Credentials missing. Please check your .env file.")

# Configure Redmail
gmail.username = username
gmail.password = password

# Gmail SSL Configuration (Port 465)
gmail.smtp_host = "smtp.gmail.com"
gmail.smtp_port = 587
gmail.smtp_use_ssl = False  # Apagar SSL implícito
gmail.smtp_use_tls = True   # Encender STARTTLS


def send_email(to: list[str], subject: str, html: str):
    """
    Sends email using Gmail and Redmail via SSL.
    """
    try:
        logger.info(f"Attempting to send email to {to}")

        gmail.send(
            subject=subject,
            receivers=to,
            html=html,
            sender=f"AI Market Newsletter <{gmail.username}>"
        )
        logger.info("✅ Email sent successfully")
    except Exception as e:
        logger.error(f"❌ Error sending email: {e}")
        raise e
