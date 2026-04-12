--> create tables
DROP TABLE IF EXISTS anomalie, transaction, statut_transaction, type_operation, devise, produit, categorie_produit, agence, client, segment_client CASCADE;

-- SEGMENT CLIENT
CREATE TABLE segment_client (
    segment_id SERIAL PRIMARY KEY,
    segment_nom VARCHAR(50) UNIQUE NOT NULL
);

-- CLIENT
CREATE TABLE client (
    client_id VARCHAR(50) PRIMARY KEY,
    score_credit INT CHECK (score_credit >= 0),
    segment_id INT,
    taux_interet NUMERIC(5,2),
    categorie_risque VARCHAR(20),
    FOREIGN KEY (segment_id) REFERENCES segment_client(segment_id)
);

-- AGENCE
CREATE TABLE agence (
    agence_id SERIAL PRIMARY KEY,
    agence_nom VARCHAR(100) NOT NULL
);

-- CATEGORIE PRODUIT
CREATE TABLE categorie_produit (
    categorie_id SERIAL PRIMARY KEY,
    categorie_nom VARCHAR(50) UNIQUE NOT NULL
);

-- PRODUIT
CREATE TABLE produit (
    produit_id SERIAL PRIMARY KEY,
    produit_nom VARCHAR(100) NOT NULL,
    categorie_id INT,
    FOREIGN KEY (categorie_id) REFERENCES categorie_produit(categorie_id)
);

-- DEVISE
CREATE TABLE devise (
    devise_id SERIAL PRIMARY KEY,
    code_devise VARCHAR(10) UNIQUE NOT NULL,
    taux_change_eur NUMERIC(10,4) NOT NULL
);

-- TYPE OPERATION
CREATE TABLE type_operation (
    type_operation_id SERIAL PRIMARY KEY,
    type_operation_nom VARCHAR(50) UNIQUE NOT NULL
);

-- STATUT TRANSACTION
CREATE TABLE statut_transaction (
    statut_id SERIAL PRIMARY KEY,
    statut_nom VARCHAR(50) UNIQUE NOT NULL
);

-- TRANSACTION
CREATE TABLE transaction (
    transaction_id VARCHAR(50) PRIMARY KEY,
    client_id VARCHAR(50) NOT NULL,
    produit_id INT NOT NULL,
    devise_id INT NOT NULL,
    agence_id INT NOT NULL,
    type_operation_id INT NOT NULL,
    statut_id INT NOT NULL,
    date_transaction DATE NOT NULL,
    montant NUMERIC(12,2),
    montant_eur NUMERIC(12,2),

    FOREIGN KEY (client_id) REFERENCES client(client_id),
    FOREIGN KEY (produit_id) REFERENCES produit(produit_id),
    FOREIGN KEY (devise_id) REFERENCES devise(devise_id),
    FOREIGN KEY (agence_id) REFERENCES agence(agence_id),
    FOREIGN KEY (type_operation_id) REFERENCES type_operation(type_operation_id),
    FOREIGN KEY (statut_id) REFERENCES statut_transaction(statut_id)
);

-- ANOMALIE
CREATE TABLE anomalie (
    anomalie_id SERIAL PRIMARY KEY,
    transaction_id VARCHAR(50) UNIQUE,
    is_anomaly BOOLEAN,
    is_anomaly_amount BOOLEAN,
    is_anomaly_score BOOLEAN,
    montant_eur_diff NUMERIC(12,2),
    montant_eur_flag BOOLEAN,

    FOREIGN KEY (transaction_id) REFERENCES transaction(transaction_id)
);