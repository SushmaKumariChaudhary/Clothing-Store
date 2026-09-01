# Clothing Store Management System

## Enterprise Application Development Report

**Name:** Sushma Kumari Chaudhary
**College:** KFA Business School & IT
**Course:** BCS.IT 4th Semester

---

## 1. Introduction

The Clothing Store Management System is a web-based enterprise application developed to manage the daily operations of a clothing store.

The system provides functionality for managing customers, product categories, products, orders, and order items. It uses Python Django as the web application framework and Oracle Database as the backend database.

The application follows a layered approach using Django models, services, serializers/API, views, templates, and database queries.

## 2. Objectives

The main objectives of the system are:

* To manage clothing store product information.
* To manage product categories.
* To manage customer orders.
* To manage order items and quantities.
* To perform CRUD operations on the main entities.
* To establish relationships between database tables.
* To implement queries involving multiple related entities.
* To implement complex business queries.
* To provide a REST API for products.
* To demonstrate a background/asynchronous task.
* To provide a user-friendly web-based graphical interface.
* To use Oracle Database for persistent data storage.

## 3. Technologies Used

| Technology            | Purpose                   |
| --------------------- | ------------------------- |
| Python                | Programming language      |
| Django                | Web application framework |
| Oracle Database       | Database management       |
| Django ORM            | Database interaction      |
| Django REST Framework | REST API                  |
| HTML                  | Web page structure        |
| CSS                   | Web page styling          |
| Bootstrap             | User interface design     |
| Git                   | Version control           |
| GitHub                | Project repository        |

## 4. System Overview

The system consists of five main entities:

1. Customer
2. Category
3. Product
4. Order
5. Order Item

These entities are connected through relationships. A customer can place multiple orders, a category can contain multiple products, and an order can contain multiple order items. Each order item is associated with a product.

The overall relationship can be represented as:

**Customer → Order → Order Item → Product → Category**

> **Figure 1: Entity Relationship Diagram (ERD)**
> *Diagram will be inserted here later.*

## 5. Project Structure

The Django project is organized into the following major components:

* `clothing_store/` – Main Django project configuration.
* `store/` – Main application containing models, views, services, serializers, tasks, URLs, and templates.
* `templates/store/` – HTML templates used by the web interface.
* `manage.py` – Django project management utility.
* `README.md` – Project overview and technology information.
* `REPORT.md` – Detailed assignment report.
