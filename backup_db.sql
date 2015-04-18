BEGIN TRANSACTION;
CREATE TABLE users (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	fullname VARCHAR, 
	password VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO `users` VALUES (1,'Quasar','Quasar Jarosz','4');
CREATE TABLE systemcorps (
	id INTEGER NOT NULL, 
	corp VARCHAR, 
	system INTEGER, 
	number INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(system) REFERENCES system (id)
);
INSERT INTO `systemcorps` VALUES (1,'TEST',1,80);
CREATE TABLE system (
	id INTEGER NOT NULL, 
	name VARCHAR, 
	stratop INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(stratop) REFERENCES stratop (id)
);
INSERT INTO `system` VALUES (1,'F-QQ5N',1);
CREATE TABLE stratop (
	id INTEGER NOT NULL, 
	constellation VARCHAR, 
	good_guys VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO `stratop` VALUES (1,'J-9M7D','TEST Alliance Please Ignore');
CREATE TABLE event (
	id INTEGER NOT NULL, 
	time DATE, 
	stratop INTEGER, 
	text VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(stratop) REFERENCES stratop (id)
);
INSERT INTO `event` VALUES (1,'2015-04-18',1,'OH NOES THE NEWLINES');
CREATE TABLE corpstatus (
	id INTEGER NOT NULL, 
	corp VARCHAR, 
	number INTEGER, 
	stratop INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(stratop) REFERENCES stratop (id)
);
INSERT INTO `corpstatus` VALUES (1,'TEST',547,1);
INSERT INTO `corpstatus` VALUES (2,'BNI',1547,1);
CREATE TABLE controlnode (
	id INTEGER NOT NULL, 
	battle INTEGER, 
	system_name VARCHAR, 
	control VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(battle) REFERENCES battle (id)
);
INSERT INTO `controlnode` VALUES (1,1,'F-QQ5N',NULL);
INSERT INTO `controlnode` VALUES (2,1,'H6-EYX','TEST');
CREATE TABLE battle (
	id INTEGER NOT NULL, 
	stratop INTEGER, 
	system_name VARCHAR, 
	structure_name VARCHAR, 
	PRIMARY KEY (id), 
	FOREIGN KEY(stratop) REFERENCES stratop (id)
);
INSERT INTO `battle` VALUES (1,1,'U-HVIX','Station');
COMMIT;
