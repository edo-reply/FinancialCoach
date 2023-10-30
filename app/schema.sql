DROP TABLE IF EXISTS coach;
CREATE TABLE coach (
  id TEXT PRIMARY KEY,
  details TEXT,
  config TEXT
);

DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id TEXT PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  base_coach TEXT,
  FOREIGN KEY(base_coach) REFERENCES coach(id)
);

DROP TABLE IF EXISTS user_transaction;
CREATE TABLE user_transaction (
  id TEXT PRIMARY KEY,
  user_id TEXT,
  title TEXT,
  details TEXT,
  category INTEGER,
  time_span INTEGER,
  deadline NUMBER,
  recurring_event INTEGER,
  FOREIGN KEY(user_id) REFERENCES user(id)
);
