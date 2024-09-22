# Sidd's Pizza Ordering System

**Sidd's Pizza Ordering System** is an interactive console-based application that simulates a real-world pizza ordering experience. This project allows users to select from a variety of pizzas, sizes, and toppings, and provides a clear order receipt with a total cost calculation.

## Project Overview

This project is designed to provide a simple, engaging, and user-friendly way for customers to order pizza. The system allows for real-time customization of pizza orders, tracks selected options, and outputs a detailed summary of the user's choices and the corresponding costs.

## Objectives

- **Create a functional pizza ordering system**: Provide users with an intuitive interface to select pizza types, sizes, and toppings.
- **Simulate a real-world pizza menu**: Offer a variety of pizzas with pricing for different sizes and additional toppings.
- **Automate order calculation**: Ensure the total cost is calculated based on the size, number of pizzas, and additional toppings.
- **Provide an order summary**: Generate a detailed receipt for the user to confirm their order details, including the total price.

## Features

- **Pizza Menu**: Users can view a menu of available pizzas and their prices before placing an order.
- **Pizza Size Options**: Small, Medium, and Large sizes are available with corresponding prices.
- **Toppings Selection**: Up to three toppings are free, and additional toppings are charged a small fee.
- **Order Management**: Users can place multiple orders, and the system tracks the quantities and selections for each pizza.
- **Dynamic Price Calculation**: The system automatically calculates the total price based on the size and number of pizzas ordered, along with any additional toppings.
- **Order Receipt**: A comprehensive order receipt is generated, detailing the flavors, sizes, number of pizzas, toppings, and total cost.

## Menu Options

- **Pizza Flavors**:
  - Pepperoni Pizza: AED 60
  - Margherita Pizza: AED 65
  - Vegetarian Pizza: AED 40
  - Neapolitan Pizza: AED 54

- **Pizza Sizes**:
  - Small: AED 40
  - Medium: AED 60
  - Large: AED 100

- **Toppings**:
  - Olives
  - Tomatoes
  - Mushrooms
  - Jalapenos

  (First 3 toppings are free; additional toppings are charged AED 4 each.)

## How It Works

1. **Initial User Input**: The user is asked to enter their name and is presented with options to either view the menu or place an order.
2. **Placing an Order**:
   - The user selects a pizza flavor and specifies the number of pizzas.
   - The user then selects the pizza size (Small, Medium, or Large).
   - Topping selections are made, with the first three being free and additional ones incurring a cost.
3. **Order Summary**: After all selections are made, the program generates a detailed order receipt, displaying the selected pizzas, their size, toppings, and the final price.
4. **Final Output**: The program outputs a friendly thank-you message and shows the user the total amount to be paid.

## Example Walkthrough

```plaintext
Please enter your name: Sarah

Welcome to Sidd's Pizza Sarah! Please select the following options to proceed.
1. MENU
2. Order a Pizza
3. Exit

You selected: Pepperoni Pizza
Size: Large
Toppings: Olives, Tomatoes, Jalapenos

THANK YOU FOR ORDERING!
--------------------------------------------------------
                           YOUR ORDER RECEIPT
--------------------------------------------------------
Flavours           No. of Pizzas            Size               Price
Pepperoni           x1                      Large              100
                   -----------------------------------
                    Order Toppings       Topping Price
                   -----------------------------------
                    Olives                  0
                    Tomatoes                0
                    Jalapenos               0

TOTAL AMOUNT TO BE PAID: AED 100
--------------------------------------------------------
