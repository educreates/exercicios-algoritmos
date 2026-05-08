# 🏆 CHALLENGE — Complete Registration Report System for an Event

---

An organization is developing a system to consolidate registrations for a themed event with workshops and extra activities. Unlike the previous exercises, this challenge requires a more robust solution, with more elaborate functions, chained calls and greater problem decomposition.

The goal is to build a small modular application, where each function is responsible for one processing step, and some of them depend directly on the result of others.

---

## Expected Project Structure

You must create two Python files:

- `event_functions.py` — with the auxiliary and processing functions;
- `event_main.py` — with the main program logic.

---

## Functions — `event_functions.py`

### 1. `calculate_base_price(ticket_type, default_price=120)`

Create a function that receives the ticket type chosen by the participant and an optional default price. Consider the following multipliers over the default price:

- `"regular"` → 100% of the default price;
- `"vip"` → 150% of the default price;
- `"student"` → 60% of the default price.

The function must return the calculated base price for the ticket.

**Example:**

```
Input: ticket_type = "vip", default_price = 120
Expected output: 180.0
```

---

### 2. `calculate_extras(base_price, workshops=0, extra_material=False)`

Create a function that receives the base ticket price, the number of extra workshops chosen and a boolean indicating whether the participant wants extra material.

Consider the following rules:

- each extra workshop adds $30.00;
- if extra material is requested, add $20.00.

The function must return three values: total workshop cost, extra material cost and updated partial total.

**Example:**

```
Input: base_price = 120.0, workshops = 2, extra_material = True
Expected output: (60.0, 20.0, 200.0)
```

---

### 3. `apply_discount(partial_value, coupon=0, admin_fee=5)`

Create a function that receives a partial value, an optional percentage coupon discount and a default administrative fee percentage.

The function must:

- calculate the discount amount;
- apply the discount;
- calculate the administrative fee on the already discounted value;
- return three values: discount amount, administrative fee amount and final price to pay.

**Example:**

```
Input: partial_value = 200.0, coupon = 10, admin_fee = 5
Expected output: (20.0, 9.0, 189.0)
```

---

### 4. `classify_participation(workshops, extra_material, final_total)`

Create a function that receives the number of workshops, the extra material information and the final registration value. The function must return a textual classification for the registration profile.

Classification rules:

- 2 or more workshops **and** extra material → `"Complete registration"`;
- at least 1 workshop → `"Intermediate registration"`;
- otherwise → `"Basic registration"`.

**Example:**

```
Input: workshops = 2, extra_material = True, final_total = 189.0
Expected output: "Complete registration"
```

---

### 5. `generate_participant_report(name, ticket_type, default_price, workshops, extra_material, coupon=0)`

> ⚠️ **Main function of the challenge** — this function chains all the previous ones.

It must:

1. call `calculate_base_price`;
2. use the result to call `calculate_extras`;
3. use the partial value to call `apply_discount`;
4. use the final total to call `classify_participation`;
5. return multiple values with the participant's main consolidated data.

The function must return:

- base price;
- workshop cost;
- material cost;
- discount amount;
- administrative fee amount;
- final price;
- registration classification.

**Example:**

```
Input: name = "Marina", ticket_type = "vip", default_price = 120,
       workshops = 2, extra_material = True, coupon = 10
Expected output: (180.0, 60.0, 20.0, 26.0, 11.7, 245.7, "Complete registration")
```

---

## Main Logic — `event_main.py`

In the main file, import the functions from the module and develop the system logic.

The program must process the data of **3 participants**. For each participant, the program must:

1. Read the name;
2. Read the ticket type;
3. Read the number of extra workshops;
4. Read whether extra material is requested;
5. Read an optional discount coupon;
6. Call the `generate_participant_report` function;
7. Display an organized summary for that participant.

---

## Expected Outputs

| Output | Description |
|---|---|
| Participant name | Free text |
| Ticket type | regular, vip or student |
| Base ticket price | Calculated according to the type |
| Total extra workshop cost | Quantity × $30.00 |
| Extra material cost | $20.00 if requested |
| Applied discount amount | Coupon percentage |
| Administrative fee amount | 5% over the discounted value |
| Final registration price | Total to pay |
| Registration classification | Basic, intermediate or complete |

---

## ✅ Additional Challenge Requirements

- Correctly organize the functions in the library file;
- Import the functions in the main file;
- Use optional parameters in more than one function;
- Use multiple return values in more than one function;
- Build at least one function with chained calls between functions;
- Avoid repeating code in the main file.

---

> **Note:** unlike the previous exercises, this challenge requires more planning and organization. Function chaining is the central point — master it and the rest will follow naturally.