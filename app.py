from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    """
    TODO: Implement database connection with proper row factory
    Should return conn 
    """
    # TODO: Connect to 'store.db'
    # TODO: Set row_factory to sqlite3.Row
    # TODO: Return the connection
    return "conn"

@app.route('/')
def index():
    return render_template('index.html')

# Route: GET, POST /register
@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    TODO: Implement user registration
    GET: Should render registration form
    POST: Should process registration and redirect to login
    """
    if request.method == 'POST':
        # TODO: Get username and password from form
        # TODO: Insert new user into database
        # TODO: Redirect to login page after successful registration
        return jsonify({"pass": "Registration"}), 500
    
    # TODO: Render registration template for GET request
    return jsonify({"pass": "Registration form "}), 500

# Route: GET, POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    TODO: Implement user login
    GET: Should render login form
    POST: Should authenticate user and redirect to dashboard or show error
    """
    if request.method == 'POST':
        # TODO: Get username and password from form
        # TODO: Verify credentials against database
        # TODO: Set session if credentials are valid
        # TODO: Redirect to dashboard on success or show error message
        return jsonify({"pass": "login"}), 500
    
    # TODO: Render login template for GET request
    return jsonify({"pass": "login"}), 500

# Route: GET /dashboard
@app.route('/dashboard', methods=['GET'])
def dashboard():
    """
    TODO: Implement dashboard route
    Should check if user is logged in
    Should display products and total cart value
    Total cart value should be calculated from all products
    """
    # TODO: Check if user is logged in (session contains user_id)
    # TODO: Get all products from database
    # TODO: Calculate total value of all products
    # TODO: Render dashboard template with products and total value
    return jsonify({"pass": "Dashboard"}), 500

# Route: GET, POST /add_product
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """
    TODO: Implement add product functionality
    GET: Should render add product form
    POST: Should add product to database and redirect to dashboard
    """
    if request.method == 'POST':
        # TODO: Get product details from form (name, price, description)
        # TODO: Insert product into database
        # TODO: Redirect to dashboard
        return jsonify({"pass": "Add product"}), 500
    
    # TODO: Render add product template for GET request
    return jsonify({"pass": "Add product"}), 500

# Route: GET, POST /edit_product/<int:id>
@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    """
    TODO: Implement edit product functionality
    GET: Should render edit form with current product data
    POST: Should update product in database and redirect to dashboard
    """
    if request.method == 'POST':
        # TODO: Get updated product details from form
        # TODO: Update product in database
        # TODO: Redirect to dashboard
        return jsonify({"pass": "edit product"}), 500
    
    # TODO: Get product by id for editing
    # TODO: Render edit product template with current product data
    return jsonify({"pass": " edit product"}), 500

# Route: GET /delete_product/<int:id>
@app.route('/delete_product/<int:id>', methods=['GET'])
def delete_product(id):
    """
    TODO: Implement delete product functionality
    Should delete product from database and redirect to dashboard
    """
    # TODO: Delete product from database by id
    # TODO: Redirect to dashboard
    return jsonify({"pass": "Delete"}), 500

# Route: GET /api/products
@app.route('/api/products', methods=['GET'])
def get_products():
    """
    TODO: Implement API endpoint to get all products
    Should return JSON list of all products
    """
    # TODO: Get all products from database
    # TODO: Return products as JSON
    return jsonify([]), 500

# Route: POST /api/product
@app.route('/api/product', methods=['POST'])
def add_product_json():
    """
    TODO: Implement API endpoint to add product via JSON
    Should accept JSON data and add product to database
    Should return success status with 201 code
    """
    # TODO: Get JSON data from request
    # TODO: Insert product into database
    # TODO: Return success response with 201 status code
    return jsonify({"status": "failed"}), 400

# Route: GET /logout
@app.route('/logout', methods=['GET'])
def logout():
    """
    TODO: Implement logout functionality
    Should clear user session and redirect to login
    """
    # TODO: Remove user_id from session
    # TODO: Redirect to login page
    return jsonify({"pass": "Logout not implemented"}), 500

if __name__ == '__main__':
    app.run(debug=True)
