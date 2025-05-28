from flask import Flask, jsonify, request
import psycopg2
import os

database_name = os.environ.get('DATABASE_NAME')
app_host = os.environ.get('APP_HOST')
app_port = os.environ.get('APP_PORT')
app_user = os.environ.get('APP_USER')
app_password = os.environ.get('APP_PASSWORD')

conn = psycopg2.connect(f"dbname='{database_name}' user='{app_user}' host='{app_host}' password='{app_password}'")
cursor = conn.cursor()

def create_all():
    print("Creating tables...")
    query = """
        CREATE TABLE IF NOT EXISTS Companies (
            company_id SERIAL PRIMARY KEY,
            company_name VARCHAR NOT NULL
        );
        CREATE TABLE IF NOT EXISTS Products (
            product_id SERIAL PRIMARY KEY,
            company_id INTEGER REFERENCES Companies(company_id) UNIQUE NOT NULL,
            company_name VARCHAR,
            price INTEGER,
            description VARCHAR,
            active BOOLEAN DEFAULT true
        );
        CREATE TABLE IF NOT EXISTS Warranties (
            warranty_id SERIAL PRIMARY KEY,
            product_id INTEGER REFERENCES Products(product_id) NOT NULL UNIQUE,
            warranty_months VARCHAR NOT NULL
        );   
        CREATE TABLE IF NOT EXISTS Categories (
            category_id SERIAL PRIMARY KEY,
            category_name VARCHAR NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS ProductsCategoriesXref (
            product_id INTEGER REFERENCES Products(product_id) NOT NULL,
            category_id INTEGER REFERENCES Categories(category_id) NOT NULL
        );   
    """
    cursor.execute(query)
    conn.commit()
    print("Tables created successfully.")



app = Flask(__name__)


@app.route('/category', methods=['POST'])
def add_category():
    data = request.form if request.form else request.get_json()
    category_name = data.get('category_name')

    if not category_name:
        return jsonify({"message": "category_name is a Required Field"}), 400

    cursor.execute("""
        INSERT INTO Categories (category_name)
        VALUES (%s)
        RETURNING category_id;
    """, (category_name,))
    
    category_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({'category_id': category_id}), 201

@app.route('/company', methods=['POST'])
def add_company():
    data = request.form if request.form else request.get_json()
    company_name = data.get('company_name')

    if not company_name:
        return jsonify({"message": "company_name is a Required Field"}), 400

    cursor.execute("""
        INSERT INTO Companies (company_name)
        VALUES (%s)
        RETURNING company_id;
    """, (company_name,))
    
    company_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({'company_id': company_id}), 201


@app.route('/product', methods=['POST'])
def add_product():
    data = request.form if request.form else request.get_json()
    company_id = data.get('company_id')
    company_name = data.get('company_name')
    price = data.get('price')
    description = data.get('description')

    cursor.execute("""
        INSERT INTO Products (company_id, company_name, price, description)
        VALUES (%s, %s, %s, %s)
        RETURNING product_id;
    """, (company_id, company_name, price, description))
    
    product_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({'product_id': product_id}), 201

@app.route('/warranty', methods=['POST'])
def add_warranty():
    data = request.form if request.form else request.get_json()
    product_id = data.get('product_id')
    warranty_months = data.get('warranty_months')

    if not warranty_months:
        return jsonify({"message": "warranty_months is a Required Field"}), 400

    cursor.execute("""
        INSERT INTO Warranties (product_id, warranty_months)
        VALUES (%s, %s)
        RETURNING warranty_id;
    """, (product_id, warranty_months))
    
    warranty_id = cursor.fetchone()[0]
    conn.commit()

    return jsonify({'warranty_id': warranty_id}), 201

@app.route('/companies', methods=['GET'])
def get_companies():
    cursor.execute("SELECT * FROM Companies;")
    companies = cursor.fetchall()
    return jsonify(companies), 200

@app.route('/products', methods=['GET'])
def get_products():
    cursor.execute("SELECT * FROM Products;")
    products = cursor.fetchall()
    return jsonify(products), 200

@app.route('/categories', methods=['GET']) 
def get_categories():
    cursor.execute("SELECT * FROM Categories;")
    categories = cursor.fetchall()
    return jsonify(categories), 200

@app.route('/products/active', methods=['GET'])
def get_active_products():
    cursor.execute("SELECT * FROM Products WHERE active = true;")
    active_products = cursor.fetchall()
    return jsonify(active_products), 200

@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    cursor.execute("SELECT * FROM Products WHERE product_id = %s;", (product_id,))
    product = cursor.fetchone()
    if product:
        return jsonify(product), 200
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/company/<company_id>', methods=['GET'])
def get_company_by_id(company_id):
    try:
        cursor.execute("SELECT * FROM Companies WHERE company_id = %s;", (company_id,))
        company = cursor.fetchone()
        if company:
            return jsonify(company), 200
        else:
            return jsonify({"message": "Company not found"}), 404
    except psycopg2.Error as e:
        return jsonify({"message": "Error fetching company data", "error": str(e)}), 500

@app.route('/warranty/<warranty_id>', methods=['GET'])
def get_warranty_by_id(warranty_id):
    cursor.execute("SELECT * FROM Warranties WHERE warranty_id = %s;", (warranty_id,))
    warranty = cursor.fetchone()
    if warranty:
        return jsonify(warranty), 200
    else:
        return jsonify({"message": "Warranty not found"}), 404

@app.route('/category/<category_id>', methods=['GET'])
def get_category_by_id(category_id):
    cursor.execute("SELECT * FROM Categories WHERE category_id = %s;", (category_id,))
    category = cursor.fetchone()
    if category:
        return jsonify(category), 200
    else:
        return jsonify({"message": "Category not found"}), 404

@app.route('/company/<company_id>', methods=['PUT'])
def update_company(company_id):
    data = request.form if request.form else request.get_json()
    company_name = data.get('company_name')

    if not company_name:
        return jsonify({"message": "company_name is a Required Field"}), 400

    cursor.execute("""
        UPDATE Companies
        SET company_name = %s
        WHERE company_id = %s;
    """, (company_name, company_id))
    
    conn.commit()
    return jsonify({"message": "Company updated successfully"}), 200

@app.route('/product/<product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.form if request.form else request.get_json()
    company_id = data.get('company_id')
    company_name = data.get('company_name')
    price = data.get('price')
    description = data.get('description')

    cursor.execute("""
        UPDATE Products
        SET company_id = %s, company_name = %s, price = %s, description = %s
        WHERE product_id = %s;
    """, (company_id, company_name, price, description, product_id))
    
    conn.commit()
    return jsonify({"message": "Product updated successfully"}), 200

@app.route('/category/<category_id>', methods=['PUT'])
def update_category(category_id):
    data = request.form if request.form else request.get_json()
    category_name = data.get('category_name')

    if not category_name:
        return jsonify({"message": "category_name is a Required Field"}), 400

    cursor.execute("""
        UPDATE Categories
        SET category_name = %s
        WHERE category_id = %s;
    """, (category_name, category_id))
    
    conn.commit()
    return jsonify({"message": "Category updated successfully"}), 200

@app.route('/warranty/<warranty_id>', methods=['PUT'])
def update_warranty(warranty_id):
    data = request.form if request.form else request.get_json()
    product_id = data.get('product_id')
    warranty_months = data.get('warranty_months')

    if not warranty_months:
        return jsonify({"message": "warranty_months is a Required Field"}), 400

    cursor.execute("""
        UPDATE Warranties
        SET product_id = %s, warranty_months = %s
        WHERE warranty_id = %s;
    """, (product_id, warranty_months, warranty_id))
    
    conn.commit()
    return jsonify({"message": "Warranty updated successfully"}), 200

@app.route('/company/delete', methods=['DELETE'])
def delete_company():
    data = request.form if request.form else request.get_json()
    company_id = data.get('company_id')

    if not company_id:
        return jsonify({"message": "company_id is a Required Field"}), 400
    cursor.execute("SELECT product_id FROM Products WHERE company_id = %s;", (company_id,))
    product_id = cursor.fetchone()
    cursor.execute("DELETE FROM Warranties WHERE product_id = %s;", (product_id,))
    conn.commit()
    cursor.execute("DELETE FROM Products WHERE company_id = %s;", (company_id,))
    conn.commit()
    cursor.execute("DELETE FROM Companies WHERE company_id = %s;", (company_id,))
    conn.commit()

    return jsonify({"message": "Company deleted successfully"}), 200

@app.route('/product/delete', methods=['DELETE'])
def delete_product():
    data = request.form if request.form else request.get_json()
    product_id = data.get('product_id')

    if not product_id:
        return jsonify({"message": "product_id is a Required Field"}), 400
    cursor.execute("DELETE FROM Warranties WHERE product_id = %s;", (product_id,))
    conn.commit()
    cursor.execute("DELETE FROM Products WHERE product_id = %s;", (product_id,))
    conn.commit()

    return jsonify({"message": "Product deleted successfully"}), 200

@app.route('/category/delete', methods=['DELETE'])
def delete_category():
    data = request.form if request.form else request.get_json()
    category_id = data.get('category_id')

    if not category_id:
        return jsonify({"message": "category_id is a Required Field"}), 400

    cursor.execute("DELETE FROM Categories WHERE category_id = %s;", (category_id,))
    conn.commit()

    return jsonify({"message": "Category deleted successfully"}), 200

@app.route('/warranty/delete', methods=['DELETE'])
def delete_warranty():
    data = request.form if request.form else request.get_json()
    warranty_id = data.get('warranty_id')

    if not warranty_id:
        return jsonify({"message": "warranty_id is a Required Field"}), 400

    cursor.execute("DELETE FROM Warranties WHERE warranty_id = %s;", (warranty_id,))
    conn.commit()

    return jsonify({"message": "Warranty deleted successfully"}), 200

if __name__ == '__main__':
    create_all()
    app.run(host=app_host, port=app_port)