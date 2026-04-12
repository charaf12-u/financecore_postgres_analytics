import pandas as pd

def clean_data(file_path):

    # Load data
    df = pd.read_csv(file_path)

    # Remove spaces from column names
    df.columns = df.columns.str.strip()

    # Convert date
    df["date_transaction"] = pd.to_datetime(df["date_transaction"], errors="coerce")

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna({
        "montant": 0,
        "montant_eur": 0,
        "taux_change_eur": 0
    })

    # Ensure numeric types
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

    bool_cols = [
        "is_anomaly",
        "is_anomaly_amount",
        "is_anomaly_score",
        "montant_eur_flag"
    ]
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].astype(bool)

    return df