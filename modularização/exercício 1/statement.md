# Integrative Exercise 1 - Closing a coffee shop order

---

A coffee shop wants to better organize its order closing process. For this, the system must calculate the coffee price, the side item price, generate small summaries of the items and, at the end, calculate the order totals.

In this exercise, you must build a small project with two Python files:

- `coffeeshop_functions.py` — containing the functions;
- `coffeeshop_main.py` — containing the main program logic.

---

## Functions — `coffeeshop_functions.py`

### 1. `calculate_coffee_price(base_price, surcharge=0)`

Create a function that receives the base price of a coffee and an optional surcharge related to the chosen size. The function must return the final price of the drink.

**Example:**

```
Input: base_price = 8.0, surcharge = 2.0
Expected output: 10.0
```

---

### 2. `calculate_side_item(price, discount=0)`

Create a function that receives the price of a side item and an optional percentage discount. The function must return the final value of the side item after applying the given discount.

**Example:**

```
Input: price = 12.0, discount = 25
Expected output: 9.0
```

---

### 3. `item_summary(name, value)`

Create a function that receives the name of an item and its final value. The function must return two values: a string with the item description and the value formatted for display.

**Example:**

```
Input: name = "Cappuccino", value = 10.5
Expected output: ("Cappuccino", "$ 10.50")
```

---

### 4. `calculate_totals(value1, value2, service_fee=10)`

Create a function that receives the values of two items and an optional service fee. The function must return three values: subtotal, fee amount and the final order total.

**Example:**

```
Input: value1 = 10.0, value2 = 8.0, service_fee = 10
Expected output: (18.0, 1.8, 19.8)
```

---

## Main logic — `coffeeshop_main.py`

In the main file, import the created functions and develop the system logic.

The program must:

1. Read the coffee name and base price;
2. Read the optional size surcharge;
3. Read the side item name and price;
4. Read the optional side item discount;
5. Calculate the final values of both items;
6. Generate a summary for each item;
7. Calculate the subtotal, fee and order total;
8. Display a final order summary.

---

## Expected inputs and outputs

**Suggested inputs:**

| Field | Description |
|---|---|
| Coffee name | Free text |
| Coffee base price | Numeric value |
| Size surcharge | Numeric value (optional) |
| Side item name | Free text |
| Side item price | Numeric value |
| Side item discount | Percentage (optional) |
| Service fee | Percentage (optional) |

**Expected outputs:**

| Output | Description |
|---|---|
| Coffee summary | Name and formatted value |
| Side item summary | Name and formatted value |
| Subtotal | Sum of both items |
| Service fee | Value calculated over the subtotal |
| Final total | Subtotal + fee |

---

> **Note:** in this exercise, the goal is to demonstrate how functions with *optional parameters* and *multiple return values* can be organized in a separate module and reused in a main program.