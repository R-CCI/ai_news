import logging

logger = logging.getLogger(__name__)

def send_email(to: list[str], subject: str, html: str):
    """
    Stub de envío de email.
    Aquí luego conectas SendGrid / Gmail API.
    """
    logger.info("Sending email")
    logger.info(f"To: {to}")
    logger.info(f"Subject: {subject}")
    logger.info(f"Body preview: {html[:200]}")
