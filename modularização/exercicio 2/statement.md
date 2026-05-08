# Integrative Exercise 2 — Basic Trip Planning

---

A person wants to take a short trip and use a simple program to estimate the main costs and better organize the information.

In this exercise, you must build a small project with two Python files:

- `travel_functions.py` — containing the functions;
- `travel_main.py` — containing the main program logic.

---

## Functions — `travel_functions.py`

### 1. `calculate_ticket(base_price, luggage=0)`

Create a function that receives the base price of a ticket and an optional luggage fee. The function must return the final ticket price.

**Example:**

```
Input: base_price = 350.0, luggage = 80.0
Expected output: 430.0
```

---

### 2. `calculate_accommodation(daily_rate, days=1, extra_fee=0)`

Create a function that receives the daily rate, the number of days and an optional extra fee. The function must return the final accommodation cost.

**Example:**

```
Input: daily_rate = 200.0, days = 3, extra_fee = 50.0
Expected output: 650.0
```

---

### 3. `convert_duration(total_hours)`

Create a function that receives the total duration of a trip in hours. The function must return two values: the number of complete days and the remaining hours.

**Example:**

```
Input: total_hours = 53
Expected output: (2, 5)
```

---

### 4. `calculate_budget(ticket, accommodation, food=0)`

Create a function that receives the ticket cost, the accommodation cost and an optional food expense. The function must return three values: fixed cost, extra cost and overall total cost.

**Example:**

```
Input: ticket = 430.0, accommodation = 650.0, food = 120.0
Expected output: (1080.0, 120.0, 1200.0)
```

---

## Main Logic — `travel_main.py`

In the main file, import the created functions and develop the application logic.

The program must:

1. Read the base ticket price;
2. Read the optional luggage fee;
3. Calculate the final ticket price;
4. Read the daily rate;
5. Read the number of days;
6. Read an optional extra accommodation fee;
7. Calculate the final accommodation cost;
8. Read the total trip duration in hours;
9. Convert that duration into days and hours;
10. Read the optional food expense;
11. Calculate the overall budget;
12. Display a final trip summary.

---

## Expected Outputs

| Output | Description |
|---|---|
| Final ticket price | Base price + luggage fee |
| Final accommodation cost | Daily rate × days + extra fee |
| Converted duration | Total hours expressed in days and hours |
| Fixed cost | Ticket + accommodation |
| Extra cost | Food expenses |
| Total trip cost | Fixed cost + extra cost |

---

> **Note:** this exercise was designed to show how optional parameters allow flexible calculations and how multiple return values help better organize the output of a larger application.