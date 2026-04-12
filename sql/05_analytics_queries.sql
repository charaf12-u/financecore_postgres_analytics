--> Agrégations (GROUP BY, HAVING)

--> par agence
SELECT
    a.agence_nom,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.montant) AS total_montant,
    AVG(t.montant) AS moyenne_montant
FROM transaction t
JOIN agence a ON t.agence_id = a.agence_id
GROUP BY a.agence_nom
ORDER BY total_montant DESC;

--> par produit
SELECT
    p.produit_nom,
    COUNT(*) AS nb_transactions,
    SUM(t.montant) AS total_montant,
    AVG(t.montant) AS avg_montant
FROM transaction t
JOIN produit p ON t.produit_id = p.produit_id
GROUP BY p.produit_nom
HAVING COUNT(*) > 5;

--> par mois
SELECT
    EXTRACT(MONTH FROM date_transaction) AS mois,
    COUNT(*) AS total_transactions,
    SUM(montant) AS total_montant,
    AVG(montant) AS moyenne_montant
FROM transaction
GROUP BY EXTRACT(MONTH FROM date_transaction)
ORDER BY mois;




SELECT *
FROM client
WHERE score_credit < (
    SELECT AVG(score_credit)
    FROM client
);

SELECT
    sc.segment_nom,

    COUNT(t.transaction_id) AS total_transactions,

    SUM(CASE WHEN a.is_anomaly = TRUE THEN 1 ELSE 0 END) AS nb_defauts,

    ROUND(
        100.0 * SUM(CASE WHEN a.is_anomaly = TRUE THEN 1 ELSE 0 END)
        / COUNT(t.transaction_id),
        2
    ) AS taux_defaut

FROM transaction t
JOIN client c ON t.client_id = c.client_id
JOIN segment_client sc ON c.segment_id = sc.segment_id
LEFT JOIN anomalie a ON t.transaction_id = a.transaction_id

GROUP BY sc.segment_nom;



SELECT
    t.transaction_id,
    c.client_id,
    sc.segment_nom,
    p.produit_nom,
    a.agence_nom,
    d.code_devise,
    t.montant,
    t.date_transaction
FROM transaction t
JOIN client c ON t.client_id = c.client_id
JOIN segment_client sc ON c.segment_id = sc.segment_id
JOIN produit p ON t.produit_id = p.produit_id
JOIN agence a ON t.agence_id = a.agence_id
JOIN devise d ON t.devise_id = d.devise_id;


