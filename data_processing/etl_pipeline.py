def split_tables(df):

    segment_df = df[["segment_client"]].drop_duplicates().reset_index(drop=True)
    segment_df["segment_id"] = segment_df.index + 1
    segment_df = segment_df.rename(columns={"segment_client": "segment_nom"})
    df = df.merge(segment_df, left_on="segment_client", right_on="segment_nom", how="left")

    agence_df = df[["agence"]].drop_duplicates().reset_index(drop=True)
    agence_df["agence_id"] = agence_df.index + 1
    agence_df = agence_df.rename(columns={"agence": "agence_nom"})
    df = df.merge(agence_df, left_on="agence", right_on="agence_nom", how="left")

    categorie_df = df[["categorie"]].drop_duplicates().reset_index(drop=True)
    categorie_df["categorie_id"] = categorie_df.index + 1
    categorie_df = categorie_df.rename(columns={"categorie": "categorie_nom"})
    df = df.merge(categorie_df, left_on="categorie", right_on="categorie_nom", how="left")

    produit_df = df[["produit", "categorie_id"]].drop_duplicates(subset=["produit"]).reset_index(drop=True)
    produit_df["produit_id"] = produit_df.index + 1
    produit_df = produit_df.rename(columns={"produit": "produit_nom"})
    df = df.merge(produit_df, left_on="produit", right_on="produit_nom", how="left")

    devise_df = df[["devise", "taux_change_eur"]].drop_duplicates(subset=["devise"]).reset_index(drop=True)
    devise_df["devise_id"] = devise_df.index + 1
    devise_df = devise_df.rename(columns={"devise": "code_devise"})
    df = df.merge(devise_df, left_on="devise", right_on="code_devise", how="left")

    type_operation_df = df[["type_operation"]].drop_duplicates().reset_index(drop=True)
    type_operation_df["type_operation_id"] = type_operation_df.index + 1
    type_operation_df = type_operation_df.rename(columns={"type_operation": "type_operation_nom"})
    df = df.merge(type_operation_df, left_on="type_operation", right_on="type_operation_nom", how="left")

    statut_df = df[["statut"]].drop_duplicates().reset_index(drop=True)
    statut_df["statut_id"] = statut_df.index + 1
    statut_df = statut_df.rename(columns={"statut": "statut_nom"})
    df = df.merge(statut_df, left_on="statut", right_on="statut_nom", how="left")

    client_df = df[[
        "client_id",
        "score_credit_client",
        "segment_id",
        "taux_interet",
        "categorie_risque"
    ]].drop_duplicates(subset=["client_id"])
    client_df = client_df.rename(columns={"score_credit_client": "score_credit"})

    transaction_df = df[[
        "transaction_id",
        "client_id",
        "produit_id",
        "devise_id",
        "agence_id",
        "type_operation_id",
        "statut_id",
        "date_transaction",
        "montant",
        "montant_eur"
    ]].drop_duplicates(subset=["transaction_id"])

    anomalie_df = df[[
        "transaction_id",
        "is_anomaly",
        "is_anomaly_amount",
        "is_anomaly_score",
        "montant_eur_diff",
        "montant_eur_flag"
    ]].drop_duplicates(subset=["transaction_id"])

    return {
        "segment_client": segment_df[["segment_id", "segment_nom"]],
        "agence": agence_df[["agence_id", "agence_nom"]],
        "categorie_produit": categorie_df[["categorie_id", "categorie_nom"]],
        "produit": produit_df[["produit_id", "produit_nom", "categorie_id"]],
        "devise": devise_df[["devise_id", "code_devise", "taux_change_eur"]],
        "type_operation": type_operation_df[["type_operation_id", "type_operation_nom"]],
        "statut_transaction": statut_df[["statut_id", "statut_nom"]],
        "client": client_df,
        "transaction": transaction_df,
        "anomalie": anomalie_df
    }