

# TODO Page - Main
# - Design the HTML page for the "Main" page using CSS to create a consistent and user-friendly appearance.
# - Add the option to select products and add them to the shopping cart using JavaScript.
# - Enable users to view the content of the shopping cart in real-time, including quantities and updated prices.

# TODO CSS - Styling for All Pages
# - Create a CSS file to style all the pages in the project consistently and provide a good user experience.

# TODO JSON - Managing Data Using JSON
# - Write functions to read and write data from/to a JSON file for storing information such as products, orders, user details, and more.
# - Display information from a JSON file in HTML pages using JavaScript.

from flask import Flask, render_template, request, session
import json

# יצירת אפליקציה Flask
app = Flask(__name__)

# הגדרת רשימת הפריטים הראשונית
items = [
   
    
    {"item": "Coffee", "price": 25, "image": "/static/cuffee.png"},

    {"item": "Chocolate", "price": 12, "image": "/static/choco.jpeg"},
    {"item": "Bread", "price": 5, "image": "/static/bread.jpeg"},
    {"item": "Pasta", "price": 8, "image": "/static/pasta.png"},
    {"item": "Cereal", "price": 15, "image": "/static/cerial.jpg"},
]


cart = []

def get_cart():
    if 'cart' not in session:
        session['cart'] = []  # אם אין עגלת קניות ב-session, יצור עגלה ריקה
    return session['cart']
@app.route('/')
def logP():
    return render_template('log.html',)
    
@app.route('/1')
def index():
    # חישוב סכום הכולל של המוצרים בעגלת הקניות
    total_price = sum(items['price'] * items['quantity'] for items in cart)
    
    return render_template('index.html', items=items, cart=cart)


@app.route('/add_to_cart_app', methods=['POST'])
def add_to_cart_app():
    user_input = request.form.get('item')
    for item in items:
       
        if user_input == item['item']:
            item_in_cart = next((cart_item for cart_item in cart if cart_item['item'] == item['item']), None)
           
            if item_in_cart:
                item_in_cart['quantity'] += 1
             
            else:
                cart.append({'item': item['item'], 'price': item['price'], 'quantity': 1})

    # Initialize total_price to zero before using it
    total_price = 0
    
    # Calculate the total price
    for cart_item in cart:
        total_price += cart_item['price'] * cart_item['quantity']

    return render_template('index.html', items=items, cart=cart, total_price=total_price)




@app.route('/delete_item', methods=['POST'])
def delete_item():
    item_name_to_delete = request.form.get('item_name')  # שם הפריט למחיקה
    quantity_to_delete = int(request.form.get('quantity'))  # כמות הפריטים למחיקה

    
    for cart_item in cart:
        if cart_item['item'] == item_name_to_delete:
            if quantity_to_delete >= cart_item['quantity']:
                cart.remove(cart_item)  # מחק את הפריט אם הכמות למחיקה היא גדולה או שווה לכמות בעגלה
            else:
                cart_item['quantity'] -= quantity_to_delete  # פחות את הכמות שנבחרה מהכמות בעגלה
            break  # סיים אחרי מציאת הפריט הראשון
    
    
    total_price = sum(item['price'] * item['quantity'] for item in cart)

    return render_template('index.html', items=items, cart=cart, total_price=total_price)



@app.route('/checkout', methods=['GET', 'POST'])
def checkout_page():
    total_price = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('checkout.html', items=items, cart=cart, total_price = total_price)


@app.route('/and', methods=['GET', 'POST'])
def good_buy():
    return render_template('andpoint.html')











if __name__ == "__main__":
    app.run( port= 8000 ,debug=True)

