# Modeling Automation for Smarter Digitalization at Siemens Energy

### **1) Time Saved by Automation**

$$
T_\text{saved} = T_\text{manual} \times R
$$

**Value meaning:**

* Represents the **actual hours saved per employee or team** by automating a process.
* Higher values → more time freed for **strategic or higher-value work**.
* 0 → no time saved; 1 (or 100%) → entire process automated.



### **2) ROI (Return on Investment)**

$$
\text{ROI} = \frac{C_\text{saved} - C_\text{project}}{C_\text{project}} \times 100\%
$$

**Value meaning:**

* Measures **financial effectiveness** of your project.
* Positive % → project saves more money than it costs.
* 0% → break-even; negative → costs more than it saves.
* Larger % → stronger business case and faster payback.



### **3) Data Quality Index**

$$
\text{Data Quality} = 1 - \frac{N_\text{errors}}{N_\text{total}}
$$

**Value meaning:**

* Shows **accuracy and reliability of data**.
* 0 → completely unreliable (all data has errors).
* 1 → perfect data quality (no errors).
* Higher values → better decisions, less rework, fewer mistakes.



### **4) Anomaly Detection (Threshold Method)**

$$
\text{Anomaly if } |x_i - \mu| > k \cdot \sigma
$$

**Value meaning:**

* Identifies **data points or events that deviate significantly** from expected behavior.
* Helps flag potential **production issues or errors**.
* Value outside threshold → requires attention; inside → normal operation.



### **5) System Optimization**

$$
S_\text{total} = \sum_i P_i + \sum_{i,j} C_{ij}
$$

**Value meaning:**

* Represents **overall system performance**, combining component performance and inter-component efficiency.
* Higher $S_\text{total}$ → smoother, faster, more efficient operations.
* Used to evaluate **mechanical, electrical, or process improvements**.



### **6) CIA Principles (Confidentiality, Integrity, Availability)**

$$
\text{Secure System Index} = P_\text{confidentiality} \cdot P_\text{integrity} \cdot P_\text{availability}
$$

**Value meaning:**

* Measures **security and reliability** of a system.
* 0 → completely insecure or unavailable.
* 1 → fully secure, accurate, and always accessible.
* Ensures **data protection, trust, and operational continuity**.



### **7) KPI Aggregation**

$$
\text{KPI Index} = \frac{\sum_i w_i \cdot K_i}{\sum_i w_i}
$$

**Value meaning:**

* Represents **overall performance across multiple key metrics**.
* Value between 0–100% → weighted measure of success.
* Higher → better performance across targeted business objectives.
* Useful for **management dashboards and progress tracking**.



### **8) Automation Pipeline Success Probability**

$$
P_\text{success} = P_\text{ETL} \cdot P_\text{RPA} \cdot P_\text{report}
$$

**Value meaning:**

* Probability that the **entire automated workflow completes correctly**.
* 0 → pipeline always fails; 1 → pipeline always succeeds.
* High value → confidence that automation reduces manual errors and delivers consistent results.



### **9) First 90 Days Efficiency**

$$
E(t) = E_\text{max} \cdot \frac{t}{90}, \quad t = 0,1,2,...,90
$$

**Value meaning:**

* Represents **percentage of expected operational impact** over time.
* 0 → just starting, no impact.
* 1 (or 100%) → full efficiency realized.
* Helps track **progression and effectiveness of initial implementation**.



### **10) Scaling Factor**

$$
\text{Total Improvement} = N_\text{sites} \cdot S_\text{unit}
$$

**Value meaning:**

* Shows **cumulative benefit of replicating improvements across multiple sites**.
* 0 → no sites scaled.
* Higher → larger impact at the organizational level.
* Useful for **business case of digitalization rollout**.
