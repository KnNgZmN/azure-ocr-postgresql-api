CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    extracted_text TEXT,
    processed_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
