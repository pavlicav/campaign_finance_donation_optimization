CREATE TABLE users (
  userID INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  gun_control ENUM(-1,0,1),
  abortion ENUM(-1,0,1),
  healthcare ENUM(-1,0,1),
  immigration ENUM(-1,0,1),
  climate_change ENUM(-1,0,1)
);

CREATE TABLE candidates (
  candidateID INT NOT NULL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  party VARCHAR(255) NOT NULL,
  gun_control ENUM(-1,0,1),
  abortion ENUM(-1,0,1),
  healthcare ENUM(-1,0,1),
  immigration ENUM(-1,0,1),
  education ENUM(-1,0,1),
  budget DECIMAL(10, 2) NOT NULL,
  endorsements NULL:
);