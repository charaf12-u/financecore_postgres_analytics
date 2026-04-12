import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import text
from config.db_config import get_engine

engine = get_engine()

tables = [
    "segment_client",
    "client",
    "agence",
    "categorie_produit",
    "produit",
    "devise",
    "type_operation",
    "statut_transaction",
    "transaction",
    "anomalie"
]

with engine.connect() as conn:
    for t in tables:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {t}"))
        print(f"{t} ", result.scalar())