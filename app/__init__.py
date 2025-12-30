"""
AI Market Newsletter
Cloud Run application package
"""

__version__ = "1.0.0"

# Exponer la app si usas FastAPI
from .main import app

__all__ = ["app"]
