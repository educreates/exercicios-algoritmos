# Integrative Exercise 3 — Weekly Training Report

---

A gym wants to build a small system to record a student's weekly summary. The goal is to calculate calories, consolidate training time and verify whether the target was reached.

In this exercise, you must build a small project with two Python files:

- `training_functions.py` — containing the functions;
- `training_main.py` — containing the main program logic.

---

## Functions — `training_functions.py`

### 1. `calculate_calories(base_calories, bonus=0)`

Create a function that receives the base amount of calories burned in a workout and an optional bonus related to a complementary activity. The function must return the total calories.

**Example:**

```
Input: base_calories = 280, bonus = 40
Expected output: 320
```

---

### 2. `calculate_training_time(main_time, warmup=10)`

Create a function that receives the main training time and an optional warmup time. The function must return the total training time, in minutes.

**Example:**

```
Input: main_time = 45, warmup = 15
Expected output: 60
```

---

### 3. `analyze_performance(total_minutes)`

Create a function that receives the total minutes trained during the week. The function must return two values: the number of complete hours and the remaining minutes.

**Example:**

```
Input: total_minutes = 135
Expected output: (2, 15)
```

---

### 4. `consolidate_training(calories, time, target=300)`

Create a function that receives the calories burned, the total training time and an optional calorie target. The function must return three values: difference from the target, a boolean indicating whether the target was reached and a summary message.

**Example:**

```
Input: calories = 320, time = 60, target = 300
Expected output: (20, True, "Target reached")
```

---

## Main Logic — `training_main.py`

In the main file, import the functions from the module and implement the report logic.

The program must:

1. Read the base calorie amount for the workout;
2. Read the optional calorie bonus;
3. Calculate the total calories burned;
4. Read the main training time;
5. Read the warmup time or use the default value;
6. Calculate the total training time;
7. Analyze the total minutes and convert them into hours and minutes;
8. Read the weekly target or use the default value;
9. Consolidate the data;
10. Display a final report.

---

## Expected Outputs

| Output | Description |
|---|---|
| Total calories | Base calories + bonus |
| Total training time | Main time + warmup |
| Time in hours and minutes | Total minutes converted |
| Difference from target | Calories burned minus the target |
| Target reached | Boolean indicating the result |
| Summary message | Final text about performance |

---

> **Note:** in this exercise, the goal is to show how smaller functions, organized in a separate file, make it simpler to build a larger and more complete report.