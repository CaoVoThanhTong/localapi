import sqlite3

# Kết nối tới cơ sở dữ liệu hoặc tạo một cơ sở dữ liệu mới
conn = sqlite3.connect('mydatabase.db')

# Tạo đối tượng cursor để thao tác với cơ sở dữ liệu
cursor = conn.cursor()

# Xóa bảng products nếu tồn tại
cursor.execute("DROP TABLE IF EXISTS products")

# Tạo bảng 'products' với các cột tương ứng
cursor.execute('''CREATE TABLE products
                  (id INTEGER PRIMARY KEY,
                  name TEXT,
                  price REAL,
                  image TEXT,
                  qty INTEGER)''')

# Dữ liệu sản phẩm
data = [
    {
        'id': 1,
        'name': 'Bearbrick x BAPE ABC Camo Shark Clear Green',
        'price': 500,
        'image': 'img/br1.png',
        'qty': 1
    },
    {
        'id': 2,
        'name': 'Bearbrick x Action City Jiangshi Glow In The Dark 1000%',
        'price': 600,
        'image': 'img/br2.png',
        'qty': 1
    },
    {
        'id': 3,
        'name': 'Bearbrick Captain A 400%',
        'price': 700,
        'image': 'img/br3.png',
        'qty': 1
    },
    {
        'id': 4,
        'name': 'Bearbrick Pink Panther',
        'price': 800,
        'image': 'img/br4.png',
        'qty': 1
    },
    {
        'id': 5,
        'name': 'Bearbrick x Toy Story Rozzo',
        'price': 1000,
        'image': 'img/br5.png',
        'qty': 1
    },
    {
        'id': 6,
        'name': 'Bearbrick Leonardo De Vinci Mona Lisa',
        'price': 1000,
        'image': 'img/br6.png',
        'qty': 1
    }
]

# Chèn dữ liệu vào bảng 'products'
for item in data:
    cursor.execute("INSERT INTO products (id, name, price, image, qty) VALUES (?, ?, ?, ?, ?)",
                   (item['id'], item['name'], item['price'], item['image'], item['qty']))

# Thêm cột mới "name_lowercase"
cursor.execute("ALTER TABLE products ADD COLUMN name_lowercase TEXT")

# Cập nhật giá trị cho cột "name_lowercase"
cursor.execute("UPDATE products SET name_lowercase = LOWER(name)")

# Tạo chỉ mục cho cột "name_lowercase"
cursor.execute("CREATE INDEX idx_name_lowercase ON products (name_lowercase)")

# Lưu các thay đổi vào cơ sở dữ liệu
conn.commit()

# Tìm kiếm sản phẩm dựa trên tên
search_term = "bearbrick"
cursor.execute("SELECT * FROM products WHERE name_lowercase LIKE ?", ('%' + search_term.lower() + '%',))
results = cursor.fetchall()
for row in results:
    print(row)

# Đóng kết nối với cơ sở dữ liệu
conn.close()
