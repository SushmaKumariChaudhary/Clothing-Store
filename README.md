# Clothing Store Management System

A web-based Clothing Store Management System developed using Python Django and Oracle Database.

**Name:** Sushma Kumari Chaudhary
**College:** KFA Business School & IT
**Course:** BCS.IT 4th Semester

---

## 1. Introduction

The **Clothing Store Management System** is an enterprise web application developed to manage the daily operations of a clothing store efficiently. The system provides a centralized platform for managing customers, product categories, products, orders, and order items.

The application is developed using **Python and Django** as the application framework and **Oracle Database** as the backend database. Django ORM is used to interact with the database, while Django templates are used to provide a user-friendly web interface.

The system implements CRUD (Create, Read, Update, Delete) operations for the major entities. It also provides related database queries, complex queries involving multiple entities, a REST API for products, and a low-stock background task.

The main purpose of this system is to demonstrate how an enterprise application can integrate a relational database with a web-based application while maintaining a structured business and service layer.

---

## 2. Objectives

The main objectives of the Clothing Store Management System are:

* To develop a web-based clothing store management application.
* To connect a Django application with an Oracle Database.
* To implement multiple related database tables.
* To use Django ORM for database operations.
* To implement CRUD operations for the major entities.
* To establish relationships between customers, orders, products, categories, and order items.
* To implement related queries for retrieving meaningful business information.
* To implement complex queries involving multiple entities.
* To provide a REST API for retrieving product information.
* To implement a background task for identifying low-stock products.
* To provide a simple and user-friendly web GUI.
* To demonstrate enterprise application development concepts using Python and Django.

---

## 3. System Scenario

The system is designed for a clothing store that sells different types of clothing and fashion products. The store maintains information about its product categories, products, customers, orders, and individual items included in each order.

A **Category** represents a group of products, such as Shoes, Shirts, Dresses, or Accessories. Each category can contain multiple products.

A **Product** represents an individual item sold by the store. Each product belongs to a category and contains information such as product name, description, price, and stock quantity.

A **Customer** represents a person who purchases products from the store. A customer can place multiple orders.

An **Order** represents a customer's purchase transaction. Each order is associated with one customer and contains information such as order date, status, and total amount.

An **Order Item** represents a specific product included in an order. It connects an order with a product and stores the quantity and unit price.

### Main Relationships

* One **Category** can have many **Products**.
* One **Customer** can have many **Orders**.
* One **Order** can contain many **Order Items**.
* One **Product** can appear in many **Order Items**.
* **Order Items** connect Products and Orders.

---

## 4. Technology Stack

| Technology            | Purpose                             |
| --------------------- | ----------------------------------- |
| Python                | Main programming language           |
| Django                | Web application framework           |
| Django ORM            | Database interaction                |
| Oracle Database       | Relational database                 |
| Django REST Framework | Product REST API                    |
| HTML                  | Web page structure                  |
| CSS                   | Styling                             |
| Bootstrap             | User interface styling              |
| Git/GitHub            | Version control and project hosting |

---

## 5. Main Modules

### 5.1 Category Management

The category module provides:

* View categories
* Add categories
* Edit categories
* Delete categories

### 5.2 Product Management

The product module provides:

* View products
* Add products
* Edit products
* Delete products
* Assign products to categories
* Manage product prices
* Manage stock quantities

### 5.3 Order Management

The order module provides:

* View orders
* Create orders
* Update orders
* Delete orders
* Associate orders with customers

### 5.4 Order Item Management

The order-item module provides:

* View order items
* Create order items
* Update order items
* Delete order items
* Associate products with orders
* Manage quantity and unit price

### 5.5 Query Module

The system provides the following queries:

1. Product–Category Query
2. Order–Customer Query
3. Order Item Details Query
4. Customer Purchase Complex Query
5. Category Sales Complex Query

### 5.6 REST API

The system provides a REST API endpoint for retrieving product information in JSON format.

### 5.7 Background Task

The system includes a low-stock checking task that identifies products with low stock and generates a report in the terminal.

---

## 6. Database Entities

The system consists of five main entities:

1. **CUSTOMER**
2. **CATEGORY**
3. **PRODUCT**
4. **ORDERS**
5. **ORDER_ITEM**

### Entity Relationship Diagram

> **ER Diagram will be inserted here.**

---

## 7. Project Structure

```text
ClothingStoreManagement/
│
├── clothing_store/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   ├── services.py
│   ├── tasks.py
│   │
│   └── templates/
│       └── store/
│           ├── base.html
│           ├── home.html
│           ├── category_list.html
│           ├── category_form.html
│           ├── category_confirm_delete.html
│           ├── product_list.html
│           ├── product_create.html
│           ├── product_update.html
│           ├── product_confirm_delete.html
│           ├── order_list.html
│           ├── order_create.html
│           ├── order_update.html
│           ├── order_confirm_delete.html
│           ├── order_item_list.html
│           ├── order_item_create.html
│           ├── order_item_update.html
│           ├── order_item_confirm_delete.html
│           ├── product_category_query.html
│           ├── order_customer_query.html
│           ├── order_item_details_query.html
│           ├── customer_purchase_complex_query.html
│           └── category_sales_complex_query.html
│
├── manage.py
└── README.md
```

---
