CREATE TABLE IF NOT EXISTS sessions (
    cookie TEXT PRIMARY KEY,
    staff_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id)
);

