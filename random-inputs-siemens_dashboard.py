# Siemens Energy Digitalization Unified Dashboard - Random Inputs
# Personalized for Heider Jeffer

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import datetime
from io import BytesIO

sns.set(style="whitegrid")

# =========================
# ----- User Info ----------
# =========================

USER_NAME = "Heider Jeffer"

# =========================
# ----- Metric Functions ---
# =========================

def time_saved(T_manual: float, R: float) -> float:
    return T_manual * R

def roi(C_saved: float, C_project: float) -> float:
    return ((C_saved - C_project) / C_project) * 100

def data_quality(N_errors: int, N_total: int) -> float:
    if N_total == 0:
        return 0.0
    return 1 - (N_errors / N_total)

def is_anomaly(x_i: float, mu: float, sigma: float, k: float) -> bool:
    return abs(x_i - mu) > k * sigma

def efficiency_over_time(t: int, E_max: float) -> float:
    t = max(0, min(t, 90))
    return E_max * (t / 90)

def calculate_rpa_roi(costs: dict, benefits: dict) -> float:
    total_costs = sum(costs.values())
    total_benefits = sum(benefits.values())
    if total_costs == 0:
        st.error("Total costs cannot be zero.")
        return 0.0
    roi_value = ((total_benefits - total_costs) / total_costs) * 100
    return roi_value

# =========================
# --- Sidebar Navigation ---
# =========================

st.sidebar.title(f"{USER_NAME}'s Digitalization Dashboard")
menu = st.sidebar.radio("Select Tool:", ["Siemens Metrics", "RPA ROI Calculator", "Automated Reports", "KPI Comparison"])

# =========================
# --- Siemens Metrics -----
# =========================

if menu == "Siemens Metrics":
    st.title(f"Siemens Energy Digitalization Metrics - By {USER_NAME}")
    
    # Efficiency Plot
    st.header("1. First 90 Days Efficiency")
    E_max = np.random.uniform(0.5, 1.5)
    st.write(f"{USER_NAME}'s Random E_max: {E_max:.2f}")
    days = list(range(91))
    efficiency = [efficiency_over_time(t, E_max) for t in days]
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(days, efficiency, marker='o', color='green', label='Efficiency')
    st.pyplot(fig)
    
    # Data Quality Heatmap
    st.header("2. Data Quality Index Heatmap")
    errors_list = np.random.randint(1, 20, size=5).tolist()
    total_list = np.random.randint(50, 200, size=5).tolist()
    st.write(f"{USER_NAME}'s Random Errors:", errors_list)
    st.write(f"{USER_NAME}'s Random Totals:", total_list)
    dq_values = [data_quality(e, t) for e, t in zip(errors_list, total_list)]
    df_dq = pd.DataFrame({'Dataset': range(len(dq_values)), 'Data_Quality': dq_values})
    fig2, ax2 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_dq[['Data_Quality']].T, annot=True, cmap='YlGnBu', cbar=True, ax=ax2)
    st.pyplot(fig2)
    
    # Time Saved & ROI Heatmap
    st.header("3. Time Saved & ROI Heatmap")
    T_manual_list = np.random.randint(50, 200, size=5).tolist()
    R_list = np.random.uniform(0.3, 0.9, size=5).tolist()
    C_saved_list = np.random.randint(10000, 50000, size=5).tolist()
    C_project_list = np.random.randint(5000, 20000, size=5).tolist()
    st.write(f"{USER_NAME}'s Random T_manual:", T_manual_list)
    st.write(f"{USER_NAME}'s Random R:", R_list)
    st.write(f"{USER_NAME}'s Random Cost Saved:", C_saved_list)
    st.write(f"{USER_NAME}'s Random Project Costs:", C_project_list)
    time_saved_values = [time_saved(t,r) for t,r in zip(T_manual_list, R_list)]
    roi_values = [roi(cs, cp) for cs, cp in zip(C_saved_list, C_project_list)]
    df_metrics = pd.DataFrame({'Time_Saved': time_saved_values,'ROI': roi_values})
    fig3, ax3 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_metrics.T, annot=True, cmap='coolwarm', cbar=True, ax=ax3)
    st.pyplot(fig3)
    
    # Anomaly Detection
    st.header("4. Anomaly Detection")
    data = np.random.randint(90, 150, size=15).tolist()
    mu = np.mean(data)
    sigma = np.std(data)
    k = 2.0
    st.write(f"{USER_NAME}'s Random Data:", data)
    anomalies = [x for x in data if is_anomaly(x, mu, sigma, k)]
    fig4, ax4 = plt.subplots(figsize=(10,4))
    ax4.plot(data, 'bo-', label='Data')
    for i, x in enumerate(data):
        if x in anomalies:
            ax4.plot(i, x, 'ro', markersize=10, label='Anomaly' if i==0 else "")
    ax4.axhline(mu + k*sigma, color='red', linestyle='--', label='Upper Threshold')
    ax4.axhline(mu - k*sigma, color='red', linestyle='--', label='Lower Threshold')
    ax4.legend()
    st.pyplot(fig4)

# =========================
# --- RPA ROI Calculator ---
# =========================

elif menu == "RPA ROI Calculator":
    st.title(f"Interactive RPA ROI Calculator - By {USER_NAME}")
    cost_components = ["License", "Implementation", "Training", "Maintenance"]
    costs = {c: np.random.randint(1000, 20000) for c in cost_components}
    benefit_components = ["Labor Savings", "Error Reduction", "Compliance", "Efficiency"]
    benefits = {b: np.random.randint(5000, 40000) for b in benefit_components}
    
    st.write(f"{USER_NAME}'s Random Costs:", costs)
    st.write(f"{USER_NAME}'s Random Benefits:", benefits)
    
    roi_value = calculate_rpa_roi(costs, benefits)
    st.subheader("Results")
    st.write(f"**Total Costs:** ${sum(costs.values()):,.2f}")
    st.write(f"**Total Benefits:** ${sum(benefits.values()):,.2f}")
    st.write(f"**ROI:** {roi_value:.2f}%")
    if roi_value > 0:
        st.success(f"{USER_NAME}: The RPA project is profitable! ✅")
    elif roi_value == 0:
        st.warning(f"{USER_NAME}: Break-even. ⚠️")
    else:
        st.error(f"{USER_NAME}: The RPA project is not profitable. ❌")

# =========================
# --- KPI Comparison Section ---
# =========================

elif menu == "KPI Comparison":
    st.title(f"KPI Comparison Dashboard - By {USER_NAME}")
    datasets = [f"Project {c}" for c in ["A","B","C","D","E"]]
    dq_values = np.random.uniform(0.7, 1.0, size=len(datasets)).round(2).tolist()
    time_saved_values = np.random.randint(50, 200, size=len(datasets)).tolist()
    roi_values = np.random.randint(-10, 50, size=len(datasets)).tolist()
    efficiency_values = np.random.uniform(0.6, 1.0, size=len(datasets)).round(2).tolist()
    
    df_kpi = pd.DataFrame({
        'Dataset': datasets,
        'Data_Quality': dq_values,
        'Time_Saved': time_saved_values,
        'ROI': roi_values,
        'Efficiency': efficiency_values
    })
    
    st.subheader(f"{USER_NAME}'s KPI Table")
    st.dataframe(df_kpi)
    
    st.subheader(f"{USER_NAME}'s KPI Heatmap")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.heatmap(df_kpi.set_index('Dataset').T, annot=True, cmap='YlGnBu', cbar=True, ax=ax)
    st.pyplot(fig)
