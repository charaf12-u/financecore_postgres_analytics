import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import logging
from data_processing.data_cleaning import clean_data
from data_processing.etl_pipeline import split_tables
from data_processing.load_data import load_table
from config.db_config import get_engine
from sqlalchemy import text


os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/etl.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_sql_scripts():
    # --> run SQL (tables, indexes, views)
    logging.info("Initializing SQL Database Schema...")
    engine = get_engine()
    sql_files = [
        "sql/02_create_tables.sql",
        "sql/03_indexes.sql",
        "sql/04_views.sql"
    ]
    # --> execute SQL scripts
    with engine.begin() as conn:
        for sql_file in sql_files:
            file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', sql_file))
            if os.path.exists(file_path):
                logging.info(f"Executing {sql_file}...")
                with open(file_path, "r", encoding="utf-8") as f:
                    sql_query = f.read()
                try:
                    conn.execute(text(sql_query))
                except Exception as e:
                    logging.error(str(e))
            else:
                logging.error(f"File not found: {file_path}")

def main():

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'financecore_clean.csv'))

    run_sql_scripts()

    logging.info("Starting ETL Pipeline...")

    # --> read and clean data
    df = clean_data(file_path)
    logging.info("Data cleaned")

    # --> split tables
    tables = split_tables(df)
    logging.info("Data split into tables")

    # --> load tables
    load_order = [
        "segment_client",
        "agence",
        "categorie_produit",
        "produit",
        "devise",
        "type_operation",
        "statut_transaction",
        "client",
        "transaction",
        "anomalie"
    ]
    for table_name in load_order: 
        if table_name in tables:
            logging.info(f"Loading {table_name} ...")
            load_table(tables[table_name], table_name)

    
    logging.info("ETL Finished Successfully")

if __name__ == "__main__":
    main()