LOAD DATA LOCAL INFILE 'cities_vietnam.csv' INTO TABLE cities_vietnam
FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n'  
(@name, @province) set name=@name,province=@province;

(SELECT 'name', 'province' FROM cities_vietnam)
UNION
SELECT * FROM cities_vietnam
INTO OUTFILE 'cities_vietnam_sql.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
