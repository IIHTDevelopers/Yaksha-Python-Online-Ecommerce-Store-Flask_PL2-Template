from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_db_connection():
    """Get database connection with row factory"""
    # TODO: Implement database connection
    # Should connect to 'store.db'
    # Should set row_factory to sqlite3.Row
    # Should return a valid sqlite3.Connection object
    conn = sqlite3.connect(':change database name:')  #---> chnage the database name 
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration functionality"""
    # TODO: Implement user registration
    # For GET: Should render register.html template
    # For POST: Should get username and password from form
    # Should insert new user into users table
    # Should redirect to login page after successful registration
    return "TODO: Implement registration", 500  

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login functionality"""
    # TODO: Implement user login
    # For GET: Should render login.html template
    # For POST: Should get username and password from form
    # Should validate credentials against users table
    # Should set session['user_id'] on successful login
    # Should redirect to dashboard on success
    return "TODO: Implement login", 500  
@app.route('/dashboard')
def dashboard():
    """User dashboard with products and total value"""
    # TODO: Implement dashboard functionality
    # Should check if user is logged in (session['user_id'])
    # Should redirect to login if not authenticated
    # Should fetch all products from database
    # Should calculate total cart value (SUM of all product prices)
    # Should render dashboard.html with products and total_value
    # Total value should be > 150 for tests to pass
    return "TODO: Implement dashboard", 500  

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    """Add new product functionality"""
    # TODO: Implement add product functionality
    # Should check if user is logged in
    # For GET: Should render add_product.html template
    # For POST: Should get name, price, description from form
    # Should insert new product into products table
    # Should redirect to dashboard after successful addition
    # Database should have >= 4 products for tests to pass
    return "TODO: Implement add product", 500  

@app.route('/edit_product/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    """Edit existing product functionality"""
    # TODO: Implement edit product functionality
    # Should check if user is logged in
    # For GET: Should fetch product by id and render edit_product.html
    # For POST: Should update product with new name, price, description
    # Should redirect to dashboard after successful update
    # Should handle salt price update to 100.0 for tests to pass
    return "TODO: Implement edit product", 500  # Will cause TestSaltPriceUpdate to fail

@app.route('/delete_product/<int:id>')
def delete_product(id):
    """Delete product functionality"""
    # TODO: Implement delete product functionality
    # Should check if user is logged in
    # Should delete product with given id from products table
    # Should redirect to dashboard after successful deletion
    # Should handle Gum product deletion for tests to pass
    return "TODO: Implement delete product", 500  

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to get all products"""
    # TODO: Implement get products API
    # Should fetch all products from database
    # Should return JSON array of products
    # Should return status code 200
    # Each product should be a dictionary with all fields
    return jsonify({"e": "TODO: Implement get products json API"}), 500  

@app.route('/api/products', methods=['POST'])
def add_product_json():
    """API endpoint to add product via JSON"""
    # TODO: Implement add product JSON API
    # Should get JSON data from request
    # Should validate required fields: name, price, quantity, description
    # Should insert product into database
    # Should return success status with 201 code
    # Should handle lays product addition for tests to pass
    return jsonify({"e": "TODO: Implement add product JSON API"}), 500  

@app.route('/logout')
def logout():
    """User logout functionality"""
    # TODO: Implement logout functionality
    # Should remove 'user_id' from session
    # Should redirect to login page
    # Session should be cleared after logout
    return "TODO: Implement logout", 500  

if __name__ == '__main__':
    app.run(debug=True)
