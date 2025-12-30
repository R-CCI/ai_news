from app.prompts import NEWSLETTER_PROMPT

def build_newsletter(news: list[str]) -> str:
    """
    Builds the newsletter content.
    (Aquí luego entra LangChain + OpenAI)
    """

    joined_news = "\n".join(f"- {n}" for n in news)

    content = f"""
    <h2>Newsletter semanal – Mercados Financieros</h2>

    <h3>Resumen ejecutivo</h3>
    <p>Este es un contenido de prueba generado por el sistema.</p>

    <h3>Noticias consideradas</h3>
    <pre>{joined_news}</pre>

    <p><i>Este contenido será reemplazado por IA.</i></p>
    """

    return content
