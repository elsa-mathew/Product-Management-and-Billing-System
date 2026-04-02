Product Management and Billing System

-Developer : Elsa Mathew

Description :

    The Product Management and Billing System is a web-based application developed using Django that streamlines product handling, inventory tracking, and billing operations. The system is designed with role-based access control, allowing Admins, Managers, and Staff to perform specific tasks efficiently.

        Users :
	            1.	Admin (Superuser)
	                •	Full control over the system
	                •	Manages users, products, categories and overall monitoring
	            2.	Manager
	                •	Responsible for inventory management
	                •	Monitors stock levels and updates quantities
	            3.	Staff
	                •	Handles billing and invoicing

        Module Description :

                1.  User Management Module

                    Description : This module handles user creation, authentication, and role-based access control.

                    Functions:
	                    •	Add new users (Manager / Staff)
	                    •	Delete users
	                    •	Login authentication
	                    •	Role-based redirection (Admin / Manager / Staff dashboards)

                    Key Features:
	                    •	Uses Django authentication system
	                    •	Separate dashboards for each role
	                    •	Secure login validation

                2.  Product & Category Management Module

                    Description : This module manages product details and categorization for better organization.

                    Functions:
	                    •	Add new categories
	                    •	Delete categories
	                    •	Add new products
	                    •	Delete products
	                    •	Assign category to products
	                    •	View all products
	                    •	View all categories

                    Key Features:
	                    •	Validation for duplicate categories
	                    •	Product linked with category using foreign key
                        •   Validation for the uniqueness of SKU for each product

                3.  Inventory Management Module

                    Description : This module tracks stock levels of all products and provides status updates.

                    Functions:
	                    •	View inventory (category-wise)
	                    •	Increase stock quantity
	                    •	Decrease stock quantity
	                    •	Auto update stock status :
                                        Stock Status Logic:
	                                        •	Out of Stock → quantity < 5
	                                        •	Low Stock → quantity < 15
	                                        •	In Stock → quantity ≥ 15

                    Key Features:
	                    •	Real-time stock updates
	                    •	Separate access for Manager and Admin
	
                4.   Bill & Invoice Management Module

                    Description : This module handles billing operations, invoice generation, and bill history.

                    Functions:
	                    •	Create new bill
	                    •	Add products to bill
	                    •	Update quantity of products in bill
	                    •	Prevent duplicate product entries (updates quantity instead)
	                    •	Calculate total amount automatically
	                    •	Generate bill
	                    •	Store bill and bill items in database
	                    •	View all bills (bill history)
                        •   Generate invoice for each bill on selection

                    Key Features:
	                    •	Multiple products per bill
	                    •	Auto total calculation
	                    •	Validation to prevent empty bill generation
	                    •	Role-based access (Admin & Staff)

        Table Design :

                1.User Table (Django Default)

                Description : Stores authentication details of all users.

                | Field Name   | Type         | Description        |
                |-----------   |------        |------------        |
                | id           | Integer (PK) | Unique user ID     |
                | username     | Varchar      | Login username     |
                | password     | Varchar      | Encrypted password |
                | is_superuser | Boolean      | Identifies Admin   |

                2.User Profile Table (Role Management)

                Description : Stores roles of users (Manager / Staff).

                | Field Name | Type         | Description     |
                |----------- |------        |------------     |
                | id         | Integer (PK) | Unique ID       |
                | user_id    | FK (User)    | Linked user     |
                | role       | Varchar      | manager / staff |

                3.Category Table

                Description : Stores product categories.

                | Field Name | Type         | Description   |
                |----------- |------        |------------   |
                | id         | Integer (PK) | Unique ID     |
                | name       | Varchar      | Category name |

                4.Product Table

                Description : Stores product details.

                | Field Name  | Type             | Description     |
                |-----------  |------            |------------     |
                | id          | Integer (PK)     | Unique ID       |
                | name        | Varchar          | Product name    |
                | sku         | Varchar (Unique) | Product SKU     |
                | price       | Decimal          | Product price   |
                | category_id | FK (Category)    | Linked category |

                5.Inventory Table

                Description : Tracks stock levels of each product.

                | Field Name | Type         | Description     |
                |----------- |------        |------------     |
                | id         | Integer (PK) | Unique ID       |
                | product_id | FK (Product) | Linked product  |
                | quantity   | Integer      | Available stock |

                6.Bill Table

                Description : Stores bill summary details.

                | Field Name | Type         | Description        |
                |----------- |------        |------------        |
                | id         | Integer (PK) | Unique Bill ID     |
                | created_by | FK (User)    | Staff/Admin        |
                | total      | Decimal      | Total bill amount  |
                | created_at | DateTime     | Bill creation time |

                7.BillItem Table

                Description : Stores individual products in a bill.

                | Field Name | Type         | Description       |
                |----------- |------        |------------       |
                | id         | Integer (PK) | Unique ID         |
                | bill_id    | FK (Bill)    | Linked bill       |
                | product_id | FK (Product) | Product           |
                | quantity   | Integer      | Quantity          |
                | price      | Decimal      | Price at purchase |


        Relationships

            . One User → One Role (Profile)
            . One Category → Many Products
            . One Product → One Inventory
            . One Bill → Many BillItems
            . One Product → Many BillItems

Technology Stack :

    Backend
	    •	Framework: Django
	    •	Language: Python
	    •	Architecture: MVT (Model-View-Template)
	    •	ORM: Django ORM for database operations

    Frontend
	    •	HTML – Structure of web pages
	    •	CSS3 – Styling and layout design
	
    Database
	    •	SQLite3
	        
    Development Tools
	    •	IDE: Visual Studio Code
	    •	Version Control: Git

Project Structure:
	
product-management-and-billing-system/
│
├── config/                     # Main project configuration
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Root URL configuration
│   ├── asgi.py
│   └── wsgi.py
│
├── users/                      # User management module
│   ├── models.py               # User profile / roles
│   ├── views.py                # Login, user handling
│   ├── urls.py
│   └── templates/
│
├── products/                   # Product & category module
│   ├── models.py               # Product, Category
│   ├── views.py
│   ├── urls.py
│   └── templates/
│
├── inventory/                  # Inventory module
│   ├── models.py               # Inventory (stock)
│   ├── views.py                # Stock update logic
│   ├── urls.py
│   └── templates/
│
├── billing/                    # Billing module
│   ├── models.py               # Bill, BillItem
│   ├── views.py                # Billing logic
│   ├── urls.py
│   └── templates/
│
├── templates/                  # Common templates
│   ├── home.html
│   ├── login.html
│   ├── admin_base.html
│   ├── manager_base.html
│   ├── staff_base.html
│   ├── bill_details.html
│   ├── bill_view.html
│   ├── billing.html
│   ├── dashboard.html
│   ├── inventory.html
│   ├── manager_dashboard.html
│   ├── manager_inventory.html
│   ├── product_management.html
│   ├── staff_dashboard.html
│   ├── user_management.html
│   ├── view_categories.html
│   ├── view_products.html
│
├── static/                     # Static files (CSS)
│   └── css/
│       ├── home.css
│       ├── login.css
│       ├── admin.css
│       ├── manager.css
│       ├── staff.css
│       ├── product.css
│       ├── inventory.css
│       ├── billing.css
│       └── manager_dashboard.css
│
├── db.sqlite3                  # Database file
├── manage.py                   # Django project manager
├── tests/                      # project test cases
│   ├── testcase_user.md
│   ├── testcase_product.md
│   ├── testcase_inventory.md
│   ├── testcase_billing.md
├── docs/                       # project documentation folder
│   ├── flow_explanation.md
│   ├── project_overview.md
├── README.md                   # project readme file
└── requirements.txt            # Project dependencies


Usecase / How to run the program:

    If you want to run the code you will need to do the following steps:

        . Open terminal in project directory
        . Create virtual environment
        . Initialize git and connect to repo
        . Move to project folder (command : cd config)
        . Run the following command : python manage.py runserver

IMPORTANT STEPS:

    . Make sure you have installed python (version : 3.x )
    . open terminal in your system 
    . create a directory (mkdir product-management-and-billing-system)
    . Initialize a virtual environment
    . Inside this directory install python framework django (pip install django)
    . Create a project folder (django-admin startproject config)
    . Change directory to config (cd config)
    . Create apps (
        python manage.py startapp accounts,
        python manage.py startapp products,
        python manage.py startapp inventory,
        python manage.py startapp billing,
        )
    . Open VS code (code .)
    . Implement the code and run

Conclusion :
     
     This project demonstrates the implementation of a complete business workflow system by integrating product management, inventory control, and billing into a single platform. It provides a practical solution for small to medium-scale operations and serves as a strong foundation for further enhancements such as analytics, reporting, and deployment.
    

    