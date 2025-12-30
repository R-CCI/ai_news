from fastapi import FastAPI, Query, HTTPException
from typing import Optional
import os
import logging

# =====================================================
# App config
# =====================================================
app = FastAPI(
    title="AI Market Newsletter",
    version="1.0.0",
    description="AI-powered weekly stock market newsletter"
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# =====================================================
# Health check (Cloud Run NEEDS this)
# =====================================================
@app.get("/")
def health_check():
    return {"status": "ok"}

# =====================================================
# Generate newsletter
# =====================================================
@app.post("/generate")
def generate_newsletter(test_email: Optional[str] = Query(default=None)):
    """
    Generates the weekly newsletter.
    If test_email is provided, sends ONLY to that email.
    """

    try:
        # --- PLACEHOLDER: fetch news ---
        news = [
            "Stocks rallied after the Fed signaled potential rate cuts in 2025.",
            "Tech stocks outperformed as AI-related earnings surprised to the upside.",
            "Oil prices fell amid concerns about global demand."
        ]

        # --- PLACEHOLDER: AI generation ---
        content = f"""
        <h2>Newsletter semanal – Mercados financieros</h2>
        <p>Este es un contenido de prueba generado por la API.</p>
        <ul>
            {''.join(f'<li>{n}</li>' for n in news)}
        </ul>
        """

        if test_email:
            # --- PLACEHOLDER: email sending ---
            logger.info(f"Sending TEST newsletter to {test_email}")

            # Aquí luego integras SendGrid / Gmail API
            return {
                "status": "sent_test",
                "email": test_email,
                "preview": content[:300]
            }

        # --- Producción (más adelante) ---
        logger.info("Generating newsletter for all subscribers")

        return {
            "status": "generated",
            "message": "Newsletter generated (production mode not enabled yet)"
        }

    except Exception as e:
        logger.exception("Error generating newsletter")
        raise HTTPException(status_code=500, detail=str(e))

# =====================================================
# Unsubscribe endpoint
# =====================================================
@app.get("/unsubscribe")
def unsubscribe(email: str = Query(...)):
    """
    Unsubscribe a user from the newsletter.
    """
    try:
        logger.info(f"Unsubscribing {email}")

        # Aquí luego conectas BigQuery
        return {
            "status": "unsubscribed",
            "email": email
        }

    except Exception as e:
        logger.exception("Error unsubscribing user")
        raise HTTPException(status_code=500, detail=str(e))
