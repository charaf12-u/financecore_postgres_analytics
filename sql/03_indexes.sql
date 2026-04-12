--> create indexes


CREATE INDEX idx_transaction_client ON transaction(client_id);
CREATE INDEX idx_transaction_agence ON transaction(agence_id);
CREATE INDEX idx_transaction_date ON transaction(date_transaction);

CREATE INDEX idx_client_segment ON client(segment_id);
CREATE INDEX idx_transaction_produit ON transaction(produit_id);
CREATE INDEX idx_transaction_devise ON transaction(devise_id);
CREATE INDEX idx_transaction_type_operation ON transaction(type_operation_id);
CREATE INDEX idx_transaction_statut ON transaction(statut_id);
CREATE INDEX idx_anomalie_transaction ON anomalie(transaction_id);
