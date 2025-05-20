INSERT INTO Companies (company_id, company_name)
VALUES (54a2bd2e-df86-4b0c-98a2-82a285a3c786, “Arby’s”);

INSERT INTO Categories (category_id, category_name)
VALUES (065d503b-8d86-4114-8c3c-d09fe02776e7, “Spices”);

INSERT INTO Products (product_id, company_id, company_name, price, description, active)
VALUES (72b7dc1c-0654-412a-8870-aca68822620f, 54a2bd2e-df86-4b0c-98a2-82a285a3c786, “Arby’s”, 5, “Hello world”, true);

INSERT INTO Warranties (warranty_id, product_id, warranty_months)
VALUES (fed86038-a1f0-4a5f-b23c-95895c2ecbbe, 72b7dc1c-0654-412a-8870-aca68822620f, “12 01 02”);

INSERT INTO ProductsCategoriesXref (product_id, category_id)
VALUES (72b7dc1c-0654-412a-8870-aca68822620f, 065d503b-8d86-4114-8c3c-d09fe02776e7);

SELECT * FROM Companies;

SELECT * FROM Categories;

SELECT * FROM Products;

SELECT * FROM Warranties;

SELECT * FROM Products
WHERE active = true;

SELECT * FROM Products
WHERE company_id = 54a2bd2e-df86-4b0c-98a2-82a285a3c786;

SELECT * FROM Companies
WHERE company_id =  54a2bd2e-df86-4b0c-98a2-82a285a3c786;

SELECT * FROM ProductsCategoriesXref pcx
INNER JOIN Products p
ON p.product_id = pcx.product_id
WHERE category_id = 065d503b-8d86-4114-8c3c-d09fe02776e7;

SELECT * FROM Products p
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f
LEFT JOIN Warranties w
ON p.product_id = w.product_id
INNER JOIN ProductsCategoriesXref pcx
ON w.product_id = pcx.product_id;

SELECT * FROM Warranties 
WHERE warranty_id = fed86038-a1f0-4a5f-b23c-95895c2ecbbe;

UPDATE Companies
SET company_name = “Wendy’s”
WHERE company_id = 54a2bd2e-df86-4b0c-98a2-82a285a3c786;

UPDATE Categories
SET category_name = “Gaming”
WHERE category_id = 065d503b-8d86-4114-8c3c-d09fe02776e7;

UPDATE Products
SET description = “New Description”
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f;

UPDATE Warranties
SET warranty_months = “09 03 04 05”
WHERE warranty_id = fed86038-a1f0-4a5f-b23c-95895c2ecbbe;

UPDATE ProductsCategoriesXref
SET product_id = 5eccf405-21b7-4d77-bf4f-fa8353a668d6
WHERE warranty_id = fed86038-a1f0-4a5f-b23c-95895c2ecbbe

DELETE FROM Products 
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f;
DELETE FROM Warranties
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f;
DELETE FROM ProductsCategoriesXref
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f;

DELETE FROM Categories
WHERE category_id = 065d503b-8d86-4114-8c3c-d09fe02776e7;
DELETE FROM ProductsCategoriesXref
WHERE category_id = 065d503b-8d86-4114-8c3c-d09fe02776e7;

DELETE FROM Companies
WHERE company_id = 54a2bd2e-df86-4b0c-98a2-82a285a3c786;
DELETE FROM Products
WHERE company_id = 54a2bd2e-df86-4b0c-98a2-82a285a3c786;
DELETE FROM ProductsCategoriesXref
WHERE product_id = 72b7dc1c-0654-412a-8870-aca68822620f ;

DELETE FROM Warranties 
WHERE warranty_id = fed86038-a1f0-4a5f-b23c-95895c2ecbbe;
