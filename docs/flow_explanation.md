Product Management and Billing System – Flow Explanation

Overview

    This system is a web-based application built using Django (Python) and HTML/CSS.  
    It provides three types of user access:
            • Admin  
            • Manager  
            • Staff  
    Each user type has a separate workflow and functionality.

Application Flow

1.Home Page (home.html)

    • This is the entry point of the application  
    • Users are presented with a login option  

Navigation:
    
    • Clicking Login → redirects to /login  

2.Login Page (/login)

    • Displays login form for all users  
    • Accepts:
        * Username  
        * Password   

Logic:
    • If credentials are valid:
        * Admin → Redirect → /admin/dashboard  
        * Manager → Redirect → /manager/dashboard  
        * Staff → Redirect → /billing  

    • Else:
        * Show error message ("Invalid credentials...Try again")

3.Admin Dashboard (/admin/dashboard)

    • Accessible only after admin login  
    • Admin can:
        * Manage users (add/delete manager & staff)  
        * Manage categories  
        * Manage products  
        * View inventory and update  
        * View all bills  

4.Product & Category Management (/products)

    • Admin can:
        * Add categories  
        * view and Delete categories  
        * Add products (name, SKU, price, category)  
        * View and delete products list  

Logic:
    • Validate input fields  
    • Prevent duplicate category entries  
    • Store product details in database  

5.Inventory Management (/inventory)

    • Accessible by Admin and Manager  

Functions:
    • View products category-wise  
    • Increase stock (+)  
    • Decrease stock (-)  

Logic:
    • Update quantity in database  
    • Assign stock status:
        * Out of Stock (< 5)  
        * Low Stock (< 15)  
        * In Stock (≥ 15)  

6.Manager Dashboard (/manager/dashboard)

    • Accessible after manager login  
    • Displays:
        * Total products  
        * Low stock items  
        * Out of stock items  

7.Billing Page (/billing)

    • Accessible after staff login  

    • Staff can:
        * Select product  
        * Enter quantity  
        * Add product to bill  

Logic:
    • If product already exists → update quantity  
    • Calculate item total (quantity × price)  
    • Display items in draft table  

8.Generate Bill (/billing/generate)

Logic:
    • Check if bill has products:
        * If NO → Show error ("Select at least one product")  
        * If YES →  
            * Save bill in database  
            * Save bill items  
            * Calculate total  
            * Redirect to bill history  

9.Bill History (/billing/details)

    • Accessible by Admin and Staff  

    • Displays:
        * List of all bills  
        * Bill ID  
        * Total amount  
        * Redirect to bill view

10.Bill Invoice (/billing/view)

    • Accessible by Admin and Staff  

    • Displays:
        * List of selected bill invoice  
        * Bill ID  
        * Display items
        * Total amount  
        * Print Invoice

Request Flow Summary

       User → Home Page  
              ↓  
          Login Page  
              ↓  
         Select Role  
      /       |        \  
  Admin     Manager    Staff  
    ↓          ↓         ↓  
  Admin      Manager   Billing  
Dashboard   Dashboard   Page  
    ↓           ↓        ↓  
Products   Inventory    Billing  
  ↓                 ↓  
Inventory         Generate Bill  
  ↓                 ↓  
View Bills        Bill History  

Summary

    The system ensures a smooth workflow from login to billing, with proper validation and role-based access at each stage. Each module is connected to provide a complete product and billing management solution.