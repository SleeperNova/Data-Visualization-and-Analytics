-- Drop Tables In This Order Due To Keys --
DROP TABLE IF EXISTS campaign;
	---------------
DROP TABLE IF EXISTS category;
	---------------	
DROP TABLE IF EXISTS subcategory;
	---------------	
DROP TABLE IF EXISTS contacts;
	---------------
	
-- Contacts Table --
create table contacts(
	contact_id INT NOT NULL PRIMARY KEY,
	first_name VARCHAR(20) NOT NULL,
	last_name VARCHAR(20) NOT NULL,
	email VARCHAR(50) NOT NULL
);	

-- Category Table --
create table category(
	category_id VARCHAR(5) NOT NULL PRIMARY KEY,
	category VARCHAR(15) NOT NULL

);

-- Subcategory Table --
create table subcategory(
	subcategory_id VARCHAR(7) NOT NULL PRIMARY KEY,
	subcategory VARCHAR(20) NOT NULL

);

-- Campaign Table --
create table campaign(
	cf_id INT NOT NULL PRIMARY KEY,
	contact_id INT,
	company_name VARCHAR NOT NULL,
	description VARCHAR(100) NOT NULL,
	goal FLOAT,
	pledged FLOAT,
	outcome VARCHAR(10),
	backers_count INT,
	country VARCHAR(5),
	currency VARCHAR(5),
	launch_date DATE,
	end_date DATE,
	category_id VARCHAR(10) NOT NULL,
	subcategory_id VARCHAR(10),
	FOREIGN KEY (contact_id) REFERENCES contacts(contact_id),
	FOREIGN KEY (category_id) REFERENCES category(category_id),
	FOREIGN KEY (subcategory_id) REFERENCES subcategory(subcategory_id)
	
);


-- Simple queries to view the tables --

--view the contacts table
select * from contacts
where (first_name) = 'Francisco';

select * from contacts
where (last_name) = 'Saavedra';


--view the category table
select * from category;


--view the subcategory table
select * from subcategory;


--view the campaign table
select * from campaign
where (outcome) = 'failed';

select * from campaign
where (outcome) = 'successful';


