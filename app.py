from flask import Flask, jsonify, request
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Định nghĩa route để truy vấn danh sách sản phẩm dựa trên tên
@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # Kiểm tra xem có tham số tìm kiếm 'name' được truyền không
    search_term = request.args.get('name')
    if search_term:
        # Thực hiện truy vấn với điều kiện tìm kiếm tên sản phẩm
        cursor.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search_term + '%',))
    else:
        # Truy vấn tất cả sản phẩm nếu không có tên sản phẩm được tìm kiếm
        cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()
    conn.close()

    product_list = []
    for product in products:
        product_dict = {
            'id': product[0],
            'name': product[1],
            'price': product[2],
            'image': product[3],
            'qty': product[4]
        }
        product_list.append(product_dict)

    return jsonify(product_list)

if __name__ == '__main__':
    app.run(debug=True)
