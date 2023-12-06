CREATE TABLE user (
    id TEXT PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    budget NUMBER
);

CREATE TABLE user_transaction (
    id TEXT PRIMARY KEY,
    user_id TEXT,
    details TEXT,
    amount NUMBER,
    category INTEGER,
    recurring_event INTEGER,
    rating INTEGER,
    FOREIGN KEY(user_id) REFERENCES user(id)
);
