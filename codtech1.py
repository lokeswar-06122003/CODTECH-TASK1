import tkinter as tk
from tkinter import messagebox
import sqlite3
import bcrypt

# Database Setup
def setup_database():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Create products table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            sku TEXT NOT NULL UNIQUE,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# User Authentication
def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    try:
        conn = sqlite3.connect('inventory.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "User registered successfully!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists")

def login_user(username, password):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    record = cursor.fetchone()
    conn.close()

    if record and bcrypt.checkpw(password.encode('utf-8'), record[0]):
        messagebox.showinfo("Success", "Login successful!")
        # Proceed to main application
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Product Management
def add_product(name, sku, price, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, sku, price, quantity) VALUES (?, ?, ?, ?)', 
                   (name, sku, price, quantity))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product added successfully!")

def edit_product(product_id, name, sku, price, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET name=?, sku=?, price=?, quantity=? WHERE id=?', 
                   (name, sku, price, quantity, product_id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product updated successfully!")

def delete_product(product_id):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id=?', (product_id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Product deleted successfully!")

# GUI Setup
def setup_gui():
    root = tk.Tk()
    root.title("Inventory Management System")

    # GUI elements (e.g., buttons, labels, entries) go here

    root.mainloop()

if __name__ == "__main__":
    setup_database()
    setup_gui()
