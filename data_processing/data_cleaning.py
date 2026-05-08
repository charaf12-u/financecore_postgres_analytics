import pandas as pd

def clean_data(file_path):

    #--> read data
    df = pd.read_csv(file_path)

    #--> remove l'espace in columns
    df.columns = df.columns.str.strip()

    #--> Convert date
    df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")

    #--> Remove duplicate
    df = df.drop_duplicates()

    #--> null values
    df = df.dropna()

    #--> numeric types
    numeric_cols = [
        "montant",
        "montant_eur",
        "taux_change_eur",
        "score_credit_client",
        "taux_interet"
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    
    #--> boolean types
    bool_cols = [
        "is_anomaly",
        "is_anomaly_amount",
        "is_anomaly_score",
        "montant_eur_flag"
    ]
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(bool)

    #--> string types
    str_cols = [
        "client_id",
        "account_id",
        "product_id",
        "branch_id",
        "categorie_risque",
        "segment_client",
        "statut",
        "type_operation",    
        "agence",
        "produit",            
        "categorie",           
        "devise",
        "transaction_id",
    ]
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()


    return df