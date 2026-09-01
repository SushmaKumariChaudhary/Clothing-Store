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
## 8. Database Design

The Clothing Store Management System uses **Oracle Database** as its relational database management system. The database is designed using five main tables that are connected through primary key and foreign key relationships.

### 8.1 CUSTOMER Table

The `CUSTOMER` table stores information about customers who purchase products from the clothing store.

| Field         | Description                          |
| ------------- | ------------------------------------ |
| `customer_id` | Primary key identifying the customer |
| `first_name`  | Customer's first name                |
| `last_name`   | Customer's last name                 |
| `email`       | Customer's email address             |
| `phone`       | Customer's phone number              |

### 8.2 CATEGORY Table

The `CATEGORY` table stores the different categories of products available in the store.

| Field           | Description                          |
| --------------- | ------------------------------------ |
| `category_id`   | Primary key identifying the category |
| `category_name` | Name of the product category         |
| `description`   | Description of the category          |

### 8.3 PRODUCT Table

The `PRODUCT` table stores information about products sold by the store.

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| `product_id`     | Primary key identifying the product |
| `product_name`   | Name of the product                 |
| `description`    | Description of the product          |
| `category_id`    | Foreign key referencing CATEGORY    |
| `price`          | Price of the product                |
| `stock_quantity` | Available quantity in stock         |

### 8.4 ORDERS Table

The `ORDERS` table stores customer order information.

| Field          | Description                       |
| -------------- | --------------------------------- |
| `order_id`     | Primary key identifying the order |
| `customer_id`  | Foreign key referencing CUSTOMER  |
| `order_date`   | Date of the order                 |
| `order_status` | Current status of the order       |
| `total_amount` | Total value of the order          |

### 8.5 ORDER_ITEM Table

The `ORDER_ITEM` table stores individual products included in an order.

| Field           | Description                            |
| --------------- | -------------------------------------- |
| `order_item_id` | Primary key identifying the order item |
| `order_id`      | Foreign key referencing ORDERS         |
| `product_id`    | Foreign key referencing PRODUCT        |
| `quantity`      | Quantity of the product ordered        |
| `unit_price`    | Price of one unit                      |

---

## 9. Database Relationships

The database uses foreign-key relationships to connect the five entities.

### Category → Product

A category can contain multiple products.

```text
CATEGORY
   |
   | 1 : Many
   ↓
PRODUCT
```

The `category_id` field in the `PRODUCT` table references `category_id` in the `CATEGORY` table.

### Customer → Orders

A customer can place multiple orders.

```text
CUSTOMER
   |
   | 1 : Many
   ↓
ORDERS
```

The `customer_id` field in the `ORDERS` table references `customer_id` in the `CUSTOMER` table.

### Orders → Order Items

An order can contain multiple order items.

```text
ORDERS
   |
   | 1 : Many
   ↓
ORDER_ITEM
```

The `order_id` field in `ORDER_ITEM` references `order_id` in `ORDERS`.

### Product → Order Items

A product can appear in multiple order items.

```text
PRODUCT
   |
   | 1 : Many
   ↓
ORDER_ITEM
```

The `product_id` field in `ORDER_ITEM` references `product_id` in `PRODUCT`.

### Overall Database Relationship

```text
             ┌──────────────┐
             │   CUSTOMER   │
             └──────┬───────┘
                    │
                  1 │
                    │ M
             ┌──────▼───────┐
             │    ORDERS    │
             └──────┬───────┘
                    │
                  1 │
                    │ M
             ┌──────▼───────┐
             │ ORDER_ITEM   │
             └──────┬───────┘
                    │
                  M │
                    │ 1
             ┌──────▼───────┐
             │   PRODUCT    │
             └──────┬───────┘
                    │
                  M │
                    │ 1
             ┌──────▼───────┐
             │  CATEGORY    │
             └──────────────┘
```

> **Note:** A professionally designed ER diagram will be inserted in this section later.

---

## 10. Django ORM Models

Django ORM (Object Relational Mapper) is used to represent the database tables as Python classes. This allows the application to perform database operations using Python objects instead of writing SQL queries for every operation.

The major Django models are:

* `Customer`
* `Category`
* `Product`
* `Order`
* `OrderItem`

### 10.1 Customer Model

The `Customer` model represents customers stored in the `CUSTOMER` database table.

It contains fields for customer identification, name, email, and phone information.

### 10.2 Category Model

The `Category` model represents product categories stored in the `CATEGORY` table.

It contains the category name and description.

### 10.3 Product Model

The `Product` model represents products stored in the `PRODUCT` table.

The model has a relationship with `Category` using a foreign key. This allows every product to be associated with a particular category.

### 10.4 Order Model

The `Order` model represents customer orders stored in the `ORDERS` table.

The model has a foreign-key relationship with `Customer`, allowing each order to be associated with the customer who placed it.

### 10.5 OrderItem Model

The `OrderItem` model represents individual products within an order.

It has foreign-key relationships with both `Order` and `Product`.

Therefore, the model connects orders and products and stores the quantity and unit price of each ordered product.

---

## 11. ORM Relationships

The Django ORM relationships can be summarized as follows:

| Model     | Relationship | Related Model |
| --------- | ------------ | ------------- |
| Category  | One-to-Many  | Product       |
| Customer  | One-to-Many  | Order         |
| Order     | One-to-Many  | OrderItem     |
| Product   | One-to-Many  | OrderItem     |
| OrderItem | Many-to-One  | Order         |
| OrderItem | Many-to-One  | Product       |

These relationships allow the application to retrieve related information efficiently using Django ORM methods such as `select_related()`.

For example, the application uses:

```python
Order.objects.select_related('customer').all()
```

This retrieves orders together with their related customer information.

Similarly:

```python
OrderItem.objects.select_related(
    'order__customer',
    'product'
).all()
```

retrieves order-item information together with the related order, customer, and product.

---

## 12. Database Design Advantages

The relational database design provides several advantages:

* Reduces unnecessary duplication of data.
* Maintains relationships between different entities.
* Improves data consistency.
* Makes business queries easier to perform.
* Supports CRUD operations efficiently.
* Allows multiple entities to be queried together.
* Provides a structured foundation for the Django application.
* Makes the system easier to maintain and extend.

---
## 13. DTO / API Serializer

The application uses **Django REST Framework** to provide a REST API for product data.

A serializer is used to convert Django model objects into a format that can be returned through the API. In this project, the `ProductSerializer` is responsible for converting Product objects into JSON-compatible data.

The serializer is implemented in:

```text
store/serializers.py
```

The product API uses the serializer to return product information.

Example:

```python
@api_view(['GET'])
def product_api(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
```

The `many=True` option is used because the API retrieves multiple product records.

### Product API Endpoint

The API endpoint is:

```text
/api/products/
```

A GET request to this endpoint returns product information in JSON format.

Example response:

```json
[
    {
        "product_id": 10,
        "product_name": "Running Shoes",
        "description": "Comfortable running shoes",
        "category": 1,
        "price": "2500.00",
        "stock_quantity": 20
    }
]
```

The exact returned data depends on the products currently stored in the Oracle database.

---

## 14. Business Service Layer

The application uses a separate **business service layer** to keep business-related operations separate from the view layer.

The service layer is implemented in:

```text
store/services.py
```

The `ProductService` class is used to handle product-related business operations.

For example, the product list view calls the service layer:

```python
def product_list(request):
    products = ProductService.get_all_products()

    return render(request, 'store/product_list.html', {
        'products': products
    })
```

Instead of directly retrieving products in the view, the view delegates the operation to `ProductService`.

This separation provides a cleaner application architecture.

### Advantages of the Service Layer

The service layer provides the following benefits:

* Separates business logic from presentation logic.
* Makes views simpler and easier to understand.
* Improves code organization.
* Makes business logic reusable.
* Makes future changes easier.
* Supports enterprise application architecture.
* Makes the application easier to test and maintain.

### Application Flow

The overall flow can be represented as:

```text
User
  ↓
Web Browser
  ↓
Django URL
  ↓
View
  ↓
Service Layer
  ↓
Django ORM
  ↓
Oracle Database
```

For API requests:

```text
Client
  ↓
API URL
  ↓
Product API View
  ↓
ProductSerializer
  ↓
Django ORM
  ↓
Oracle Database
  ↓
JSON Response
```

---

## 15. CRUD Operations

CRUD stands for:

* **Create**
* **Read**
* **Update**
* **Delete**

The Clothing Store Management System implements CRUD operations for the major entities.

### 15.1 Category CRUD

The Category module supports all four CRUD operations.

| Operation | URL                                 |
| --------- | ----------------------------------- |
| Read      | `/categories/`                      |
| Create    | `/categories/create/`               |
| Update    | `/categories/<category_id>/edit/`   |
| Delete    | `/categories/<category_id>/delete/` |

The category list page displays all categories stored in the database.

The create page allows the user to add a new category.

The update page allows existing category information to be modified.

The delete page asks for confirmation before removing a category.

---

### 15.2 Product CRUD

The Product module supports:

| Operation | URL                              |
| --------- | -------------------------------- |
| Read      | `/products/`                     |
| Create    | `/products/add/`                 |
| Update    | `/products/edit/<product_id>/`   |
| Delete    | `/products/delete/<product_id>/` |

The product module also allows a product to be associated with an existing category.

---

### 15.3 Order CRUD

The Order module supports:

| Operation | URL                          |
| --------- | ---------------------------- |
| Read      | `/orders/`                   |
| Create    | `/orders/add/`               |
| Update    | `/orders/edit/<order_id>/`   |
| Delete    | `/orders/delete/<order_id>/` |

Orders are associated with customers through the `customer_id` foreign key.

---

### 15.4 Order Item CRUD

The Order Item module supports:

| Operation | URL                                    |
| --------- | -------------------------------------- |
| Read      | `/order-items/`                        |
| Create    | `/order-items/add/`                    |
| Update    | `/order-items/edit/<order_item_id>/`   |
| Delete    | `/order-items/delete/<order_item_id>/` |

Order items connect products with orders and store the quantity and unit price.

---

## 16. CRUD Implementation Using Django ORM

The application uses Django ORM methods for database operations.

### Create

A new category can be created using:

```python
Category.objects.create(
    category_name=category_name,
    description=description
)
```

Similarly, products, orders, and order items are created using their respective Django models.

### Read

Records can be retrieved using:

```python
Category.objects.all()
```

or:

```python
Product.objects.all()
```

### Update

Existing records are modified by changing their fields and calling:

```python
object.save()
```

### Delete

An existing record can be deleted using:

```python
object.delete()
```

The application also uses `get_object_or_404()` to safely retrieve individual records.

Example:

```python
product = get_object_or_404(
    Product,
    product_id=product_id
)
```

This returns the requested product or displays a 404 response if the product does not exist.

---

## 17. URL Routing

Django URL routing connects application URLs with their corresponding view functions.

The project-level URL configuration includes the Store application:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]
```

The Store application contains routes for:

* Categories
* Products
* Orders
* Order Items
* Queries
* Product API
* Background task

The root URL is connected to the home page through the `home` view.

---
## 18. Related Queries

The Clothing Store Management System implements several queries using Django ORM. These queries retrieve related information from multiple database entities and demonstrate the relationships between the tables.

The application uses Django ORM methods such as `select_related()`, `annotate()`, `Sum()`, `F()`, and `ExpressionWrapper()`.

---

### 18.1 Product–Category Query

This query retrieves products together with their related categories.

Implementation:

```python
products = Product.objects.select_related('category').all()
```

The `select_related('category')` method retrieves the related category information along with each product.

The query allows the system to display information such as:

```text
Product Name
Category
Price
Stock Quantity
```

This query demonstrates the relationship between:

```text
CATEGORY → PRODUCT
```

---

### 18.2 Order–Customer Query

This query retrieves orders together with the customers who placed them.

Implementation:

```python
orders = Order.objects.select_related('customer').all()
```

The query uses the foreign-key relationship between `Order` and `Customer`.

It allows the system to display information such as:

```text
Order ID
Customer
Order Date
Order Status
Total Amount
```

This query demonstrates:

```text
CUSTOMER → ORDERS
```

---

### 18.3 Order Item Details Query

This query retrieves order items together with their associated orders, customers, and products.

Implementation:

```python
order_items = OrderItem.objects.select_related(
    'order__customer',
    'product'
).all()
```

This query accesses three related entities:

```text
ORDER_ITEM
    ↓
ORDER
    ↓
CUSTOMER

ORDER_ITEM
    ↓
PRODUCT
```

It can display information such as:

```text
Order Item ID
Order ID
Customer
Product
Quantity
Unit Price
```

This query demonstrates how Django ORM can retrieve related data across multiple tables.

---

## 19. Complex Queries

The application also implements two complex queries that combine information from multiple entities to provide useful business information.

---

### 19.1 Customer Purchase Complex Query

The Customer Purchase query retrieves order-item information together with the related customer, order, and product information.

Implementation:

```python
order_items = OrderItem.objects.select_related(
    'order__customer',
    'product'
).all()
```

The query involves the following entities:

* Customer
* Order
* Order Item
* Product

Relationship flow:

```text
CUSTOMER
    ↓
  ORDER
    ↓
ORDER_ITEM
    ↓
 PRODUCT
```

The result can be used to determine which customer purchased which product and the quantity purchased.

This query is useful for analyzing customer purchasing activity.

The corresponding template is:

```text
store/customer_purchase_complex_query.html
```

---

### 19.2 Category Sales Complex Query

The Category Sales query calculates the total quantity sold and total sales amount for products within each category.

Implementation:

```python
categories = Category.objects.annotate(
    total_quantity=Sum(
        'product__orderitem__quantity'
    ),
    total_sales=Sum(
        ExpressionWrapper(
            F('product__orderitem__quantity') *
            F('product__orderitem__unit_price'),
            output_field=DecimalField(
                max_digits=12,
                decimal_places=2
            )
        )
    )
)
```

This query involves:

* Category
* Product
* Order Item

Relationship flow:

```text
CATEGORY
    ↓
 PRODUCT
    ↓
ORDER_ITEM
```

The query calculates:

### Total Quantity

```text
SUM(quantity)
```

This represents the total number of units sold within a category.

### Total Sales

```text
SUM(quantity × unit_price)
```

This represents the total sales value generated by the products in that category.

The query uses:

* `annotate()` to add calculated fields.
* `Sum()` to calculate totals.
* `F()` expressions to reference model fields.
* `ExpressionWrapper()` to perform arithmetic operations.
* `DecimalField()` to ensure the calculated result is handled as a decimal value.

The corresponding template is:

```text
store/category_sales_complex_query.html
```

---

## 20. Query Summary

| Query              | Main Entities                        | Purpose                               |
| ------------------ | ------------------------------------ | ------------------------------------- |
| Product–Category   | Product, Category                    | Display products with categories      |
| Order–Customer     | Order, Customer                      | Display orders with customers         |
| Order Item Details | Order Item, Order, Customer, Product | Display detailed order information    |
| Customer Purchases | Customer, Order, Order Item, Product | Analyze customer purchases            |
| Category Sales     | Category, Product, Order Item        | Calculate category sales and quantity |

These queries demonstrate the use of Django ORM relationships and database aggregation techniques.

---

## 21. Query Results

The implemented queries were tested successfully using the Django application.

Example Django ORM results included:

```text
<QuerySet [{'category_id': 1, 'category_name': 'Shoes', ...}]>
```

Customer-related query results were also successfully retrieved:

```text
<QuerySet [{'customer_id': 1, 'first_name': 'Sita', ...}]>
```

Order query results were successfully retrieved:

```text
<QuerySet [{'order_id': 1, 'customer_id': 1, ...}]>
```

Order item query results were successfully retrieved:

```text
<QuerySet [{'order_item_id': 1, 'order_id': 1,
'product_id': 10, ...}]>
```

These results confirm that the Django application is successfully retrieving data from the Oracle Database through the ORM.

> **Screenshots of the query results will be inserted here later.**

---
