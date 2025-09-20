

---


# Siemens Energy Digitalization Transformation Engineer
*Developed using Python by Heider Jeffer*

---


### 🎯 What this adds to Siemens Energy pitch

1. Not only automates reporting, but also **intelligently monitors production**.
2. **Real-time alerts** possible (e.g., notify managers when output is unusually low).
3. Replaces **manual supervision** with **automated insights**.
4. Scales easily → all factories can plug in their reports and get **standardized dashboards + anomaly detection**.

 **In short:**
 
This code reads production data from Excel, detects days where production is unusually low, and makes a **line chart** showing daily production with anomalies highlighted in **red** and the average shown as a **green dashed line**.

---

### Results:

* **Detected anomalies**:

  * **2025-09-04 (165 units)**
  * **2025-09-08 (185 units)**
    Both days fall below 80% of the factory’s average output.
* **Visualization**: The plot shows daily production with anomalies highlighted in **red**, and the mean production line as a **green dashed reference**.

---

### **1. Importing the library**

```python
import matplotlib.pyplot as plt
```

* This line imports `matplotlib`, a library used for **making charts and plots** in Python.
* `plt` is just a short name we’ll use to call its functions.

---

### **2. Loading data from Excel**

```python
summary = pd.read_excel("automated_reports/summary_report_2025-09-20.xlsx")
```

* This reads an **Excel file** into a table called `summary`.
* Each row is probably one day, with columns like `'Date'` and `'Production_Units'`.
* `pd` is usually short for **pandas**, a library for handling tables in Python. (The code assumes `import pandas as pd` was done earlier.)

---

### **3. Calculating the mean and detecting anomalies**

```python
mean_units = summary['Production_Units'].mean()
threshold = 0.8 * mean_units
summary['Anomaly'] = summary['Production_Units'] < threshold
```

* `mean_units` calculates the **average number of units produced per day**.
* `threshold` is **80% of that average**. This is the cutoff for low production.
* `summary['Anomaly']` creates a new column:

  * `True` if production is **less than the threshold** (low output)
  * `False` if production is normal or high.

This helps **highlight days with unusually low production**.

---

### **4. Making the plot**

```python
plt.figure(figsize=(10,6))
plt.plot(summary['Date'], summary['Production_Units'], marker='o', label="Daily Production")
```

* `plt.figure(figsize=(10,6))` makes a chart bigger so it’s easy to see.
* `plt.plot(...)` draws a **line chart** for daily production.
* `marker='o'` adds little circles on each data point.
* `label="Daily Production"` gives a name for the chart legend.

---

### **5. Showing the average line**

```python
plt.axhline(mean_units, color='green', linestyle='--', label=f"Mean ({mean_units:.1f})")
```

* Draws a **horizontal dashed green line** at the average production.
* Helps you see which days are above or below the average.

---

### **6. Highlighting anomalies**

```python
plt.scatter(summary.loc[summary['Anomaly'], 'Date'],
            summary.loc[summary['Anomaly'], 'Production_Units'],
            color='red', label="Anomaly (Low Output)", zorder=5)
```

* `plt.scatter(...)` adds **red dots** on days where production is too low.
* `summary.loc[summary['Anomaly'], 'Date']` gets the dates of low production.
* `zorder=5` ensures these red dots appear **on top of other plot elements**.

---

### **7. Adding labels, grid, and finalizing the plot**

```python
plt.title("Daily Production Summary with Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Production Units")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

* `plt.title` → gives the chart a title.
* `plt.xlabel` and `plt.ylabel` → label the axes.
* `plt.legend()` → shows what each color/line means.
* `plt.grid(True)` → adds a grid for easier reading.
* `plt.tight_layout()` → adjusts spacing so nothing is cut off.
* `plt.show()` → **displays the chart**.

---

### **8. Showing the summary table**

```python
summary
```

* This just prints the `summary` table.
* Now it also includes the `Anomaly` column, so you can see which days were flagged.

---



