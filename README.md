

# Siemens Energy Digitalization Transformation Engineer

### *Developed in Python by Heider Jeffer*

🔗 [GitHub Repository](https://github.com/HeiderJeffer/Siemens-Energy-Digitalization-Transformation-Engineer)

📓 [Live Workflow – Daily Output Monitor](https://github.com/HeiderJeffer/Siemens-Energy-Digitalization-Transformation-Engineer/blob/main/DailyOutputMonitor.ipynb)

🤖 [Interactive RPA ROI Calculator](https://github.com/HeiderJeffer/Siemens-Energy-Digitalization-Transformation-Engineer/blob/main/Siemens_RPA_ROI_Calculator.py.ipynb)



# ⚡ Smart Factory Digitalization Framework

**Transforming Siemens Energy’s factories with low-cost, high-impact automation.**

This prototype demonstrates how **Python and open-source tools** can replace hours of repetitive manual reporting with a **fully automated workflow** that:

* 📂 Ingests Excel factory reports
* 🧹 Cleans, validates, and monitors data quality
* 📊 Generates daily production summaries automatically
* 🚨 Detects anomalies in real-time (e.g., sudden drops in production)
* 📈 Produces clear dashboards for managers and engineers

**Key benefits:**

* ⏱ 20–30% reduction in repetitive reporting
* 💰 Estimated €60k–180k yearly savings (Trento site)
* 🌍 Scalable across Siemens Energy’s global factory network

This framework is lightweight, scalable, and cost-efficient — a tangible demonstration of Siemens Energy’s digitalization vision.



## ⚡ Quick Start Demo

### 1️⃣ Generate Test Data

```bash
python generate_test_data.py
```

Creates a sample Excel report at:

```
factory_reports/sample_report.xlsx
```

With 30 days of synthetic production data for 3 machines.



### 2️⃣ Run the Automation Framework

```bash
python automation_framework.py
```



### 3️⃣ Check the Output

* 📂 **Excel Report:** `automated_reports/summary_report_YYYY-MM-DD.xlsx`
* 📊 **Dashboard Plot:**

  * Blue line = Daily production
  * Green dashed line = Factory average
  * 🔴 Red dots = Anomalies (production < 80% of average)

**Example Logs:**

```bash
Found 1 file(s). Processing...
  -> Ingested factory_reports/sample_report.xlsx with 90 rows
✅ Automated production summary created: automated_reports/summary_report_2025-09-20.xlsx
```



# 🌍 Siemens Energy – Digitalization Automation Framework

This project demonstrates **how low-cost, open-source tools** can:

* Automate repetitive factory/office processes
* Ensure **data quality & consistency**
* Detect anomalies in production output
* Generate dashboards & visual insights
* Deliver measurable **time and cost savings**



## 🚀 Features

* Batch ingestion of multiple Excel reports
* Data cleaning, normalization, and validation
* Automated daily production summary generation (`.xlsx`)
* Anomaly detection (<80% of average output)
* Visualizations of production trends with anomalies highlighted



## 🏭 Why It Matters

Factories generate **large volumes of repetitive reporting**.
With Python automation, Siemens Energy can:

* Reduce manual work by 20–30%
* Save €60k–180k/year (Trento site)
* Improve data accuracy & decision-making speed
* Scale across global sites



## 📈 Example Output

* **Summary Report:** Daily aggregated production in Excel
* **Dashboard Plot:** Production trend with anomalies in red



## 🔧 Tech Stack

* Python 3.x
* Pandas (data processing)
* OpenPyXL (Excel I/O)
* Matplotlib (visualization)



## 🧭 Next Steps

* Predictive maintenance (ML-based failure forecasts)
* Integration with Power BI dashboards
* Modular RPA pipelines for global deployment



## ⚡ Usage Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/HeiderJeffer/Siemens-Energy-Digitalization-Transformation-Engineer.git
cd Siemens-Energy-Digitalization-Transformation-Engineer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Includes at least:

```
pandas
openpyxl
matplotlib
```

### 3️⃣ Prepare Input Data

Create `factory_reports` and add Excel files with:

| Date       | Production\_Units | Machine\_ID |
| ---------- | ----------------- | ----------- |
| 2025-09-01 | 120               | M1          |
| 2025-09-01 | 95                | M2          |
| 2025-09-02 | 130               | M1          |



### 4️⃣ Run the Framework

```bash
python automation_framework.py
```

**Outputs:**

* ✅ Daily summary Excel → `automated_reports/summary_report_YYYY-MM-DD.xlsx`
* 📊 Dashboard plot → visualizes trends and anomalies



## 🔮 Future Enhancements

* Automated anomaly alerts (email/Slack)
* Predictive maintenance ML models
* Power BI/cloud dashboard integration



# **Interactive RPA ROI Calculator in Python**

**Purpose:** Evaluate ROI of RPA initiatives in Siemens Energy factories.

* Enter cost components (license, implementation, training, maintenance)
* Enter benefit components (labor savings, error reduction, efficiency gains)
* Calculate total costs, benefits, and ROI

The interactive tool ensures **valid inputs** and can adapt for different projects.



### Python Workflow Highlights

**1. Load data:**

```python
summary = pd.read_excel("automated_reports/summary_report_2025-09-20.xlsx")
```

**2. Detect anomalies (<80% of average):**

```python
mean_units = summary['Production_Units'].mean()
threshold = 0.8 * mean_units
summary['Anomaly'] = summary['Production_Units'] < threshold
```

**3. Plot results:**

```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(summary['Date'], summary['Production_Units'], marker='o', label="Daily Production")
plt.axhline(mean_units, color='green', linestyle='--', label=f"Mean ({mean_units:.1f})")
plt.scatter(summary.loc[summary['Anomaly'], 'Date'],
            summary.loc[summary['Anomaly'], 'Production_Units'],
            color='red', label="Anomaly (Low Output)", zorder=5)
plt.title("Daily Production Summary with Anomaly Detection")
plt.xlabel("Date")
plt.ylabel("Production Units")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

