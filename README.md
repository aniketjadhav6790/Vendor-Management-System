# Vendor Management System with Performance Metrics

Setup Instructions
To run the Vendor Management System locally, follow these instructions:

1. Clone the repository:

git clone https://github.com/your-username/vendor-management-system.git

2. Navigate to the project directory:

cd vendor_management-main

3. Create a virtual environment (optional but recommended):

python -m venv venv

4. Activate the virtual environment:

-On Windows:
venv\Scripts\activate

-On macOS/Linux:
source venv/bin/activate

5. Install dependencies:

 pip install django
pip install djangorestframework
 
6. Apply migrations to set up the database:  

python manage.py migrate

7. Create a superuser account for administrative access:

python manage.py createsuperuser

8. Start the development server:

python manage.py runserver

9. Open your browser and go to http://localhost:8000/admin/ to log in with the superuser          credentials and manage vendors, purchase orders, and other data.




Table of Contents
1. Features
2. Data Models
3. Backend Logic
4. API Endpoints
5. Setup Instructions
6. Additional Technical Considerations
7. Technical Requirements
8. Deliverables

Features
1. Vendor Profile Management:
    -Create, list, retrieve, update, and delete vendor profiles.

2. Purchase Order Tracking:
    -Create, list, retrieve, update, and delete purchase orders.
    -Filter purchase orders by vendor.

3.Vendor Performance Evaluation:
    -Calculate and retrieve performance metrics for vendors.
    -Metrics include On-Time Delivery Rate, Quality Rating Average, Response Time, and               Fulfilment Rate.

Data Models

Vendor Model
*Fields:
name: Vendor's name.
contact_details: Contact information of the vendor.
address: Physical address of the vendor.
vendor_code: A unique identifier for the vendor.
on_time_delivery_rate: Tracks the percentage of on-time deliveries.
quality_rating_avg: Average rating of quality based on purchase orders.
average_response_time: Average time taken to acknowledge purchase orders.
fulfillment_rate: Percentage of purchase orders fulfilled successfully.

Purchase Order (PO) Model
*Fields:
po_number: Unique number identifying the PO.
vendor: Link to the Vendor model.
order_date: Date when the order was placed.
delivery_date: Expected or actual delivery date of the order.
items: Details of items ordered.
quantity: Total quantity of items in the PO.
status: Current status of the PO (e.g., pending, completed, canceled).
quality_rating: Rating given to the vendor for this PO (nullable).
issue_date: Timestamp when the PO was issued to the vendor.
acknowledgment_date: Timestamp when the vendor acknowledged the PO.

Historical Performance Model
*Fields:
vendor: Link to the Vendor model.
date: Date of the performance record.
on_time_delivery_rate: Historical record of the on-time delivery rate.
quality_rating_avg: Historical record of the quality rating average.
average_response_time: Historical record of the average response time.
fulfillment_rate: Historical record of the fulfilment rate.

