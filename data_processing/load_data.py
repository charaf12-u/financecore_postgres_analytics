from config.db_config import get_engine

engine = get_engine()

def load_table(df, table_name):
    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="append",
        index=False,
        method="multi"
    )