from app.bigquery import unsubscribe_email

def unsubscribe_user(email: str):
    unsubscribe_email(email)
    return {
        "status": "unsubscribed",
        "email": email
    }
