# 📦 E-Commerce Product Management API

This project is an **E-commerce Product Management API** built with Django and Django REST Framework. It allows users to view products and enables authenticated admins to perform full CRUD (Create, Read, Update, Delete) operations on product listings.

The API is specifically tailored for the sale of **accessories**, such as **mobile phones** and **laptops** and **African based Clothings**

---

## 🚀 Features

- Full CRUD operations for **products** (by authenticated admins)
- Public access to **view** products
- **Authentication** for managing users and restricting admin access
- **Search and filter** products by name or category
- **Pagination** for product listings

---

## 🔐 User Access Control

- 🔓 **Unauthenticated users** can:
  - View all products
  - Search for products

- 🔐 **Authenticated admins** can:
  - Create new products
  - Update existing products
  - Delete products

---

## 🧑‍💼 User Management Endpoints

| Method | Endpoint             | Description                    |
|--------|----------------------|--------------------------------|
| GET    | `/api/users/`        | List all registered users      |
| POST   | `/api/users/`        | Create a new user              |
| GET    | `/api/auth/login/`   | Login a user                   |
| POST   | `/api/auth/logout/`  | Logout the current user        |

---

## 📦 Product Management Endpoints

| Method | Endpoint                    | Description             |
|--------|-----------------------------|-------------------------|
| POST   | `/api/products/`            | Create a new product    |
| GET    | `/api/products/`            | Retrieve all products   |
| GET    | `/api/products/{id}/`       | Retrieve a single product |
| PUT    | `/api/products/{id}/`       | Update an existing product |
| PATCH  | `/api/products/{id}/`       | Partially update a product |
| DELETE | `/api/products/{id}/`       | Delete a product        |

---

## 🔎 Product Search

You can search products by name or category using query parameters:

