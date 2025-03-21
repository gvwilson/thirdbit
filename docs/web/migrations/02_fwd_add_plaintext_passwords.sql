-- create SQL for adding passwords
ALTER TABLE staff
ADD COLUMN username TEXT NOT NULL DEFAULT "";
ALTER TABLE staff
ADD COLUMN password TEXT NOT NULL DEFAULT "";
WITH new_data(staff_id, username, password) AS (VALUES

  (1, "vello.p", "8375"),

  (2, "viktoria.h", "3410"),

  (3, "linda.m", "0680"),

  (4, "sergey.r", "7761"),

  (5, "anu.v", "5181"),

  (6, "maria.k", "0227"),

  (7, "laura.m", "3783")

)
UPDATE staff
SET username = new_data.username, password = new_data.password
FROM new_data
WHERE (staff.staff_id = new_data.staff_id);
