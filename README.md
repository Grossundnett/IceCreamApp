# Ice Cream App

Welcome to the **Ice Cream App**! This project helps ice cream merchants manage seasonal flavors, inventories, customer flavor recommendations, and allergens. Below are steps needed to set up and run the app on your local machine.

---

## Features:
- **Seasonal Flavors**: Manages seasonal ice cream flavors and all their details.
- **Inventory Management**: Monitor the store of ingredients and their stock.
- **Customer Ideas**: Obtain customer ideas for new flavors.
- **Allergen Information**: Add and manage allergen information for flavorings.

---

## Prerequisites

Before you start, make sure that you have installed the following:

- **Python 3.x**: The language in which the application is developed.
- **SQLite**: Data regarding flavors, inventories, and suggestions will be stored in the database.
- **Git**: Version control tool for code management.

---

## Clone the Repository

To get started with the project, first, clone the repository to your local machine.

1. Open the terminal/command prompt on your computer.
2. Use the following command to clone the repository:

    ```bash
    git clone https://github.com/<your-username>/IceCreamApp.git
    ```

3. Navigate into the project directory:

    ```bash
    cd IceCreamApp
    ```

---

## Set Up the Database

The app uses **SQLite** to store data. The database file (`ice_cream.db`) is created automatically when the app is run for the first time.

1. Open the terminal/command prompt in the project directory.
2. Run the Python script to create the database tables:

    ```bash
    python app.py
    ```

This will create the following tables in your database:

- **flavors**: Stores details about the ice cream flavors.
- **inventory**: Stores ingredient inventory details.
- **suggestions**: Stores customer flavor suggestions and allergens.

---

## Running the Application

Once the database is set up, you can run the app to manage your ice cream business.

1. To **add a new flavor**, run the following:

    ```bash
    python app.py
    ```

This will prompt you to add seasonal flavors and manage your inventory.

2. You can also:
    - **View flavors by season**
    - **Add items to the shopping cart**
    - **Add allergens** via the terminal interface.

---

## Features in Detail

- **Add and View Seasonal Flavors**: Easily add new flavors with details like name and season. View them filtered by season.
- **Maintain a Shopping Cart**: Add flavors to your cart and keep track of the quantity.
- **Manage Ingredient Inventory**: Keep track of your ingredient stock and adjust quantities as needed.
- **Add Allergens for Specific Flavors**: Track allergens related to each flavor for customer safety.
