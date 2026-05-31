-- Use the database you just created
USE BrandManagerDB;
GO

-- Products Table
CREATE TABLE products (
    id INT PRIMARY KEY IDENTITY(1,1), -- IDENTITY(1,1) is SQL Server's equivalent of AUTOINCREMENT
    name NVARCHAR(255),               -- NVARCHAR is a common text type
    category NVARCHAR(255),
    cost_price DECIMAL(10, 2),        -- DECIMAL is better for currency/real numbers
    selling_price DECIMAL(10, 2),
    stock INT
);

-- Categories Table
CREATE TABLE categories (
    id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(255) UNIQUE
);

-- Sales Table
CREATE TABLE sales (
    id INT PRIMARY KEY IDENTITY(1,1),
    product_id INT,
    product_name NVARCHAR(255),
    quantity INT,
    total_amount DECIMAL(10, 2),
    profit DECIMAL(10, 2),
    date DATETIME2                   -- DATETIME2 is the modern type for timestamps
);

-- Expenses Table
CREATE TABLE expenses (
    id INT PRIMARY KEY IDENTITY(1,1),
    title NVARCHAR(255),
    category NVARCHAR(255),
    amount DECIMAL(10, 2),
    date DATETIME2,
    notes NVARCHAR(MAX)              -- NVARCHAR(MAX) for longer text notes
);

USE BrandManagerDB;
GO

-- 1. Check Products
PRINT '--- PRODUCTS DATA ---';
SELECT * FROM products;

-- 2. Check Sales
PRINT '--- SALES DATA ---';
SELECT * FROM sales;

-- 3. Check Expenses
PRINT '--- EXPENSES DATA ---';
SELECT * FROM expenses;

-- 4. Check Categories
PRINT '--- CATEGORIES DATA ---';
SELECT * FROM categories;