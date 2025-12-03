DROP TABLE IF EXISTS agency;
DROP TABLE IF EXISTS alert;

CREATE TABLE agency (
  id INTEGER PRIMARY KEY,
  name TEXT,
);

-- all times are posix 
CREATE TABLE alert (
  id INTEGER PRIMARY KEY,
  last_modified_timestamp INTEGER,
  alert_lifecycle TEXT,
  active_start INTEGER,
  active_end INTEGER,
  FOREIGN KEY (agency_id) REFERENCES agency id,
  FOREIGN KEY (route_id) REFERENCES route id,
  FOREIGN KEY (stop_id) REFERENCES stop id,
  cause TEXT,
  effect TEXT,
  effect_detail TEXT,
  header TEXT,
  description TEXT,
);