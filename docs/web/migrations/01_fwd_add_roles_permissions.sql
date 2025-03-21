-- add permission and role tables

DROP TABLE IF EXISTS permission;
CREATE TABLE permission (
  role_name TEXT,
  capability TEXT
);
INSERT INTO permission VALUES
  ('admin', 'add'),
  ('admin', 'delete'),
  ('admin', 'invalidate'),
  ('admin', 'view'),
  ('user', 'add'),
  ('user', 'invalidate'),
  ('user', 'view'),
  ('viewer', 'view')
;

DROP TABLE IF EXISTS role;
CREATE TABLE role (
  staff_id BIGINT,
  role_name TEXT
);
INSERT INTO role VALUES
  (1, 'admin'),
  (2, 'viewer')
;
INSERT INTO role
SELECT staff_id, 'user'
FROM staff
WHERE staff_id not in (
  SELECT staff_id FROM role
);
