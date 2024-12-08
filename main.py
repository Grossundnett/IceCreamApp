import sqlite3

# Establish connection to the SQLite database (creates it if not exists)
conn = sqlite3.connect('data/ice_cream.db')
cursor = conn.cursor()


# table for seasonal flavors
cursor.execute("""
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    season TEXT NOT NULL
)
""")

# table for ingredient inventory
cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient_name TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
""")

# table for customer flavor suggestions
cursor.execute("""
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavor_suggestion TEXT NOT NULL,
    allergy_concern TEXT
)
""")

print("Tables created")
conn.commit()
conn.close()




def add_flavor(name, season):
    conn = sqlite3.connect('data/ice_cream.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flavors (name, season) VALUES (?, ?)", (name, season))
    conn.commit()
    print(f"Flavor '{name}' added for the '{season}' season!")
    conn.close()


add_flavor("Mango", "Summer")
add_flavor("Pumpkin Spice", "Autumn")




def search_flavors(season=None):
    conn = sqlite3.connect('data/ice_cream.db')
    cursor = conn.cursor()

    if season:
        cursor.execute("SELECT * FROM flavors WHERE season = ?", (season,))
    else:
        cursor.execute("SELECT * FROM flavors")

    results = cursor.fetchall()
    print("Flavors:")
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Season: {row[2]}")
    conn.close()

search_flavors("Summer")  # Filter by season
search_flavors()          # Show all flavors




cart = {}

def add_to_cart(flavor_id, quantity):
    conn = sqlite3.connect('data/ice_cream.db')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM flavors WHERE id = ?", (flavor_id,))
    flavor = cursor.fetchone()

    if flavor:
        flavor_name = flavor[0]
        cart[flavor_name] = cart.get(flavor_name, 0) + quantity
        print(f"Added {quantity} of {flavor_name} to the cart.")
    else:
        print("Flavor not found!")
    conn.close()

def view_cart():
    print("Cart Contents:")
    for item, qty in cart.items():
        print(f"{item}: {qty}")



add_to_cart(1, 2)
view_cart()



def add_allergen(flavor_id, allergen):
    conn = sqlite3.connect('data/ice_cream.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO suggestions (flavor_suggestion, allergy_concern) VALUES (?, ?)", (flavor_id, allergen))
    conn.commit()
    print(f"Allergen '{allergen}' added for flavor ID {flavor_id}.")
    conn.close()


add_allergen(1, "Dairy")
