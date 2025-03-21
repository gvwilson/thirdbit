-- create SQL for adding passwords
ALTER TABLE staff
ADD COLUMN username TEXT NOT NULL DEFAULT "";
ALTER TABLE staff
ADD COLUMN password TEXT NOT NULL DEFAULT "";
WITH new_data(staff_id, username, password) AS (VALUES
{% for item in data %}
  ({{item.staff_id}}, "{{item.username}}", "{{item.password}}"){% if not loop.last %},{% endif %}
{% endfor %}
)
UPDATE staff
SET username = new_data.username, password = new_data.password
FROM new_data
WHERE (staff.staff_id = new_data.staff_id);
