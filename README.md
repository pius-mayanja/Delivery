**FUNCTIONAL AND TECHNOLOGICAL SPECIFICATIONS FOR OUR PROJECT;**

**1.BUSINESS FUNCTIONALITY for "Hivemind"**

Hivemind is a multi-business entirely online platform that brings together a large network for customers and variety of certified businesses across the nation and overseas.
Business owners are able to register with HIVEMIND by creating accounts on the platform that will enable them to offer their products, services etc. to the target market.

Business owners that are verified by the platform admin will:   
- Be able to create an account emphasizing their details like, business name and slogan, location(s), contact(s), service(s) and product(s) offered, business descripton 
- Will be able to monitor their products, receive order notifications and feedback from customers, 
send replies to customers 
- Users(business owners) will be able to customize account settings by altering the default settings.
- Users will be able to update their products clearly stating; the price changes, product availability, quality status, uploaded and updated images for new and existing products etc....

At the root of the business functionality, the 'HIVEMIND' admin panel will be able to monitor all the registered businesses on its platform. Admin will be able to send alerts, notifications on platform updates among others as specified.....    

**2. CUSTOMER FUNCTIONALITY**  
Hivemind is a multi-business entirely online platform that enables close customed interaction of the customers with the different businesses through different means that include;   
- Customers can browse different businesses and products using different specific filters for example by prices,new or used products, category, location, or keywords.
- Customers will be able to view different product offers and discounts, detailed business profiles, pricelists, product descriptions, shipping and payment methods.
- Customers will be able to place orders and order inquiries to the product suppliers and receive timely feedback.
- Customers can be able to direct message or contact suppliers (business owners) for detailed inquiries about the products and receive instant feedback.
- Customers will have a feedback section for can reviews and ratings for businesses.   

Hivemind will ensure;
- A Mobile-friendly website
- Fast-loading website pages
- User-friendly website architecture, navigation, and search 
- Complete product pages
- Effective customer support system.

**3. ADMIN PANEL FUNCTIONALITY**:   
The admin panel serves as a powerful tool for overseeing the operations of the platform, facilitating seamless interactions between businesses and customers, to authentic business activities.   
Here's an overview of how it functions:    
- The admin panel allows administrators to manage user accounts, including business owners, customers, delivery personnel, and support staff.    
- Admins can oversee the creation, editing, and removal of business listings on the platform.    
- The admin panel provides tools to monitor and manage orders and bookings received through the platform.    
- Admin panels often integrate payment processing functionalities, allowing admins to configure payment gateways, monitor transactions, and handle refunds or disputes.    
- The admin panel provides access to analytics and reporting tools that offer insights into platform performance, user behavior, sales trends, and other key metrics.    
- Admins can facilitate communication between businesses and customers by managing messaging systems, support tickets, and notifications.    
- The admin panel allows administrators to configure various platform settings, such as branding elements, customization options, notification preferences, and operational parameters.   

The admin controls the activites in the background by synchronizing the database models with the user input to always provide up-to date info for users enabling them to monitor their records.

**4.TECHNICAL FUNCTIONALITY:**   

**(i) CLOUD HOSTING**:   
The platform shall be hosted on a secure and scalable cloud infrastructure to provide high availability, performance and resilience.

considerations:
- cloud provider: Python Anywhere, because of it cost efficiency, ease of use and support for python-based applications
- Database:  Utilization of Python Anywhere built-in MYSQL databasee service for hosting the database

Implementation steps:   
- Sign up for a PythonAnywhere account and configure necessary settings.
- Deploy the web application on PythonAnywhere using their provided deployment tools.
- Set up and configure the MySQL database instance within PythonAnywhere.
- Configure any necessary environment variables and settings within PythonAnywhere for optimal performance and security. 

**(ii) BACKEND AND DATABASES.**   
The platform will be constructed using Django which is a useful frame-work for database driven applications.   
Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).  

Django follows the MVT design pattern (Model View Template).
- Model - The data you want to present, usually data from a database with well defined fields.  
- View - A request handler that returns the relevant template and content - based on the request from the user.
- Template - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.   
