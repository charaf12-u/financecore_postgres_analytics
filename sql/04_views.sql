--> Views pour les transactions
CREATE VIEW v_transactions_details AS
SELECT
t.transaction_id,
c.client_id,
p.produit_nom,
a.agence_nom,
d.code_devise,
t.montant,
t.date_transaction,
st.statut_nom
FROM transaction t
JOIN client c ON t.client_id = c.client_id
JOIN produit p ON t.produit_id = p.produit_id
JOIN agence a ON t.agence_id = a.agence_id
JOIN devise d ON t.devise_id = d.devise_id
JOIN statut_transaction st ON t.statut_id = st.statut_id;

--> Transactions avec anomalies
CREATE VIEW v_transactions_anomalies AS
SELECT
t.transaction_id,
t.date_transaction,
t.montant,
a.is_anomaly,
a.montant_eur_diff
FROM transaction t
JOIN anomalie a
ON t.transaction_id = a.transaction_id
WHERE a.is_anomaly = TRUE;


--> KPI global
CREATE OR REPLACE VIEW v_kpi_global AS
SELECT
    COUNT(*) AS total_transactions,
    SUM(montant) AS total_volume,
    AVG(montant) AS avg_transaction
FROM transaction;

--> KPI agence
CREATE OR REPLACE VIEW v_kpi_agence AS
SELECT
    a.agence_nom,
    COUNT(t.transaction_id) AS nb_transactions,
    SUM(t.montant) AS volume_total
FROM transaction t
JOIN agence a ON t.agence_id = a.agence_id
GROUP BY a.agence_nom;

--> KPI risque
CREATE OR REPLACE VIEW v_kpi_risque AS
SELECT
    COUNT(*) AS total_transactions,
    SUM(CASE WHEN a.is_anomaly = TRUE THEN 1 ELSE 0 END) AS nb_anomalies,
    ROUND(
        100.0 * SUM(CASE WHEN a.is_anomaly = TRUE THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS taux_anomalie
FROM transaction t
LEFT JOIN anomalie a ON t.transaction_id = a.transaction_id;