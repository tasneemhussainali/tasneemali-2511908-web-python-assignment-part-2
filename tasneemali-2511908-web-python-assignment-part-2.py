#!/usr/bin/env python
# coding: utf-8

# In[3]:


menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

categories = ["Starters", "Mains", "Desserts"]

for category in categories:
    print(f"\n===== {category} =====")

    for item, details in menu.items():
        if details["category"] == category:
            price = details["price"]
            status = "Available" if details["available"] else "Unavailable"

            print(f"{item:<15} ₹{price:>6.2f}   [{status}]")


# In[4]:


# Total number of items
total_items = len(menu)

# Total available items
available_items = sum(1 for item in menu.values() if item["available"])

# Most expensive item
most_expensive = max(menu.items(), key=lambda x: x[1]["price"])
exp_name = most_expensive[0]
exp_price = most_expensive[1]["price"]

# Items under 150
under_150 = [(name, data["price"]) 
             for name, data in menu.items() 
             if data["price"] < 150]

print(f"Total items on menu      : {total_items}")
print(f"Available items          : {available_items}")
print(f"Most expensive item      : {exp_name} (₹{exp_price:.2f})")

print("\nItems under ₹150:")
for name, price in under_150:
    print(f"{name} (₹{price:.2f})")


# In[6]:


cart = []

def add_to_cart(item_name, quantity):
    
    # check if item exists
    if item_name not in menu:
        print("❌ Item not found in menu")
        return
    
    # check availability
    if not menu[item_name]["available"]:
        print("❌ Item currently unavailable")
        return
    
    price = menu[item_name]["price"]
    
    # check if already in cart
    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"✓ Updated {item_name} quantity to {item['quantity']}")
            return
    
    # add new item
    cart.append({
        "item": item_name,
        "quantity": quantity,
        "price": price
    })
    
    print(f"✓ Added {item_name} to cart")


# In[7]:


add_to_cart("Paneer Tikka", 2)
add_to_cart("Garlic Naan", 3)
add_to_cart("Paneer Tikka", 1)   # should increase quantity
add_to_cart("Ice Cream", 1)      # unavailable
add_to_cart("Pizza", 1)          # not in menu

print(cart)


# In[8]:


[
 {'item': 'Paneer Tikka', 'quantity': 3, 'price': 180.0},
 {'item': 'Garlic Naan', 'quantity': 3, 'price': 40.0}
]


# In[9]:


def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"✓ {item_name} removed from cart")
            return
    
    print("❌ Item not found in cart")


# In[10]:


remove_from_cart("Garlic Naan")
remove_from_cart("Pizza")   # not in cart

print(cart)


# In[11]:


def update_quantity(item_name, new_quantity):
    for item in cart:
        if item["item"] == item_name:
            
            if new_quantity <= 0:
                print("❌ Quantity must be greater than 0")
                return
            
            item["quantity"] = new_quantity
            print(f"✓ {item_name} quantity updated to {new_quantity}")
            return
    
    print("❌ Item not found in cart")


# In[12]:


update_quantity("Paneer Tikka", 5)
update_quantity("Pizza", 2)   # not in cart


# In[15]:


cart = []

def add_to_cart(item_name, quantity):
    if item_name not in menu:
        print("❌ Item not found in menu")
        return

    if not menu[item_name]["available"]:
        print("❌ Item currently unavailable")
        return

    price = menu[item_name]["price"]

    for item in cart:
        if item["item"] == item_name:
            item["quantity"] += quantity
            print(f"✓ Updated {item_name} quantity to {item['quantity']}")
            return

    cart.append({"item": item_name, "quantity": quantity, "price": price})
    print(f"✓ Added {item_name} to cart")


def remove_from_cart(item_name):
    for item in cart:
        if item["item"] == item_name:
            cart.remove(item)
            print(f"✓ {item_name} removed from cart")
            return
    print("❌ Item not found in cart")


# 1️⃣ Add Paneer Tikka ×2
add_to_cart("Paneer Tikka", 2)
print("Cart:", cart)

# 2️⃣ Add Gulab Jamun ×1
add_to_cart("Gulab Jamun", 1)
print("Cart:", cart)

# 3️⃣ Add Paneer Tikka ×1 (should update quantity)
add_to_cart("Paneer Tikka", 1)
print("Cart:", cart)

# 4️⃣ Try Mystery Burger
add_to_cart("Mystery Burger", 1)
print("Cart:", cart)

# 5️⃣ Try Chicken Wings (unavailable)
add_to_cart("Chicken Wings", 1)
print("Cart:", cart)

# 6️⃣ Remove Gulab Jamun
remove_from_cart("Gulab Jamun")
print("Cart:", cart)


# In[16]:


print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    name = item["item"]
    qty = item["quantity"]
    price = item["price"]
    total = qty * price
    subtotal += total

    print(f"{name:<18} x{qty}    ₹{total:>7.2f}")

gst = subtotal * 0.05
total_payable = subtotal + gst

print("------------------------------------")
print(f"Subtotal:           ₹{subtotal:>7.2f}")
print(f"GST (5%):           ₹{gst:>7.2f}")
print(f"Total Payable:      ₹{total_payable:>7.2f}")
print("====================================")


# In[18]:


import copy

inventory = {
    "Paneer Tikka":   {"stock": 10, "reorder_level": 3},
    "Chicken Wings":  {"stock":  8, "reorder_level": 2},
    "Veg Soup":       {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka":      {"stock": 20, "reorder_level": 5},
    "Veg Biryani":    {"stock":  6, "reorder_level": 3},
    "Garlic Naan":    {"stock": 30, "reorder_level": 10},
    "Gulab Jamun":    {"stock":  5, "reorder_level": 2},
    "Rasgulla":       {"stock":  4, "reorder_level": 3},
    "Ice Cream":      {"stock":  7, "reorder_level": 4},
}

# Step 1 — Deep copy
inventory_backup = copy.deepcopy(inventory)

# Step 2 — modify original
inventory["Paneer Tikka"]["stock"] = 1

print("Modified inventory:")
print(inventory["Paneer Tikka"])

print("\nBackup inventory (unchanged):")
print(inventory_backup["Paneer Tikka"])

# Step 3 — restore
inventory = copy.deepcopy(inventory_backup)

print("\nRestored inventory:")
print(inventory["Paneer Tikka"])


# In[19]:


# Simulate order fulfilment
for item in cart:
    name = item["item"]
    qty = item["quantity"]

    stock_available = inventory[name]["stock"]

    if stock_available >= qty:
        inventory[name]["stock"] -= qty
        print(f"✓ {name}: deducted {qty}, remaining {inventory[name]['stock']}")
    else:
        print(f"⚠ Insufficient stock for {name}")
        print(f"Only {stock_available} available, deducting all")

        inventory[name]["stock"] = 0


# In[21]:


# Reorder alerts
print("\nReorder Alerts:")
for item, data in inventory.items():
    stock = data["stock"]
    reorder = data["reorder_level"]

    if stock <= reorder:
        print(f"⚠ Reorder Alert: {item} — Only {stock} unit(s) left (reorder level: {reorder})")


# In[22]:


print("\nCurrent Inventory:")
for item, data in inventory.items():
    print(f"{item}: {data}")

print("\nInventory Backup (Original):")
for item, data in inventory_backup.items():
    print(f"{item}: {data}")


# In[24]:


sales_log = {
    "2025-01-01": [
        {"order_id": 1,  "items": ["Paneer Tikka", "Garlic Naan"],          "total": 220.0},
        {"order_id": 2,  "items": ["Gulab Jamun", "Veg Soup"],              "total": 210.0},
        {"order_id": 3,  "items": ["Butter Chicken", "Garlic Naan"],        "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4,  "items": ["Dal Tadka", "Garlic Naan"],             "total": 220.0},
        {"order_id": 5,  "items": ["Veg Biryani", "Gulab Jamun"],           "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6,  "items": ["Paneer Tikka", "Rasgulla"],             "total": 260.0},
        {"order_id": 7,  "items": ["Butter Chicken", "Veg Biryani"],        "total": 570.0},
        {"order_id": 8,  "items": ["Garlic Naan", "Gulab Jamun"],           "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9,  "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"],          "total": 270.0},
    ],
}

print("Daily Revenue:")
print("----------------------------")

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    print(f"{date} : ₹{total:.2f}")


# In[25]:


# Find best-selling day
best_day = None
max_revenue = 0

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)

    if total > max_revenue:
        max_revenue = total
        best_day = date

print("\nBest-Selling Day:")
print(f"{best_day} with revenue ₹{max_revenue:.2f}")


# In[26]:


# Count how many times each item appears in orders
item_count = {}

for date, orders in sales_log.items():
    for order in orders:
        for item in order["items"]:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1

# Find most ordered item
most_item = None
max_count = 0

for item, count in item_count.items():
    if count > max_count:
        max_count = count
        most_item = item

print("\nMost Ordered Item:")
print(f"{most_item} — ordered {max_count} times")


# In[27]:


# Add new day to sales_log
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"],                     "total": 260.0},
]

# Reprint revenue per day
print("Daily Revenue:")
print("----------------------------")

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)
    print(f"{date} : ₹{total:.2f}")

# Find best-selling day again
best_day = None
max_revenue = 0

for date, orders in sales_log.items():
    total = sum(order["total"] for order in orders)

    if total > max_revenue:
        max_revenue = total
        best_day = date

print("\nBest-Selling Day:")
print(f"{best_day} with revenue ₹{max_revenue:.2f}")


# In[30]:


print("All Orders:")
print("----------------------------")

order_no = 1

for date, orders in sales_log.items():
    for order in orders:
        print(f"{order_no}. {date} | Order ID: {order['order_id']} | Total: ₹{order['total']:.2f}")
        order_no += 1


# In[31]:


all_orders = []

for date, orders in sales_log.items():
    for order in orders:
        all_orders.append((date, order))

print("All Orders:")
print("----------------------------")

for i, (date, order) in enumerate(all_orders, start=1):
    print(f"{i}. {date} | Order ID: {order['order_id']} | Total: ₹{order['total']:.2f}")

