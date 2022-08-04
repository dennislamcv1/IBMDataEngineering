-- Drop the table in case it exists

DROP TABLE ShoeShop;

-- Create the table

CREATE TABLE ShoeShop (
    Product VARCHAR(25) NOT NULL,
    Stock INTEGER NOT NULL,
    Price DECIMAL(8,2) CHECK(Price>0) NOT NULL,
    PRIMARY KEY (Product)
    );

-- Insert sample data into the table
    
INSERT INTO ShoeShop VALUES
('Boots',11,200),
('High heels',8,600),
('Brogues',10,150),
('Trainers',14,300);

-- Retrieve all records from the table

SELECT * FROM ShoeShop;


