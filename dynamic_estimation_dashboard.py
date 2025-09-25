# Dynamic Estimation Dashboard - By Heider Jeffer
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

# =========================
# --- User Info ----------
# =========================
USER_NAME = "Heider Jeffer"

# =========================
# --- Metric Functions ----
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

# =========================
# --- Sidebar -------------
# =========================
st.sidebar.title(f"{USER_NAME}'s Dynamic Estimation Dashboard")
menu = st.sidebar.radio("Select Tool:", ["Dynamic Metrics", "RPA ROI Simulation", "KPI Comparison"])

# =========================
# --- Dynamic Metrics -----
# =========================
if menu == "Dynamic Metrics":
    st.title(f"Dynamic Estimation Metrics - By {USER_NAME}")
    
    st.header("1️⃣ First 90 Days Efficiency")
    E_max = st.slider("Maximum Efficiency (E_max)", 0.5, 1.5, 1.0)
    days = list(range(91))
    efficiency = [efficiency_over_time(t, E_max) for t in days]
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(days, efficiency, marker='o', color='green', label='Efficiency')
    ax.set_xlabel("Day")
    ax.set_ylabel("Efficiency")
    st.pyplot(fig)
    
    st.header("2️⃣ Data Quality Simulation")
    N_datasets = st.slider("Number of Datasets", 2, 10, 5)
    errors_list = np.random.randint(0, 20, size=N_datasets)
    total_list = np.random.randint(50, 200, size=N_datasets)
    dq_values = [data_quality(e, t) for e, t in zip(errors_list, total_list)]
    df_dq = pd.DataFrame({'Dataset': [f"DS{i+1}" for i in range(N_datasets)], 'Data_Quality': dq_values})
    st.write(f"{USER_NAME}'s Random Data Quality")
    st.dataframe(df_dq)
    fig2, ax2 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_dq[['Data_Quality']].T, annot=True, cmap='YlGnBu', ax=ax2)
    st.pyplot(fig2)
    
    st.header("3️⃣ Time Saved & ROI Simulation")
    T_manual_list = np.random.randint(50, 200, size=N_datasets)
    R_list = np.random.uniform(0.3, 0.9, size=N_datasets)
    C_saved_list = np.random.randint(10000, 50000, size=N_datasets)
    C_project_list = np.random.randint(5000, 20000, size=N_datasets)
    time_saved_values = [time_saved(t,r) for t,r in zip(T_manual_list, R_list)]
    roi_values = [roi(cs, cp) for cs, cp in zip(C_saved_list, C_project_list)]
    df_metrics = pd.DataFrame({
        'Dataset': [f"DS{i+1}" for i in range(N_datasets)],
        'Time_Saved': time_saved_values,
        'ROI': roi_values
    })
    st.dataframe(df_metrics)
    fig3, ax3 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_metrics.set_index('Dataset').T, annot=True, cmap='coolwarm', ax=ax3)
    st.pyplot(fig3)
    
    st.header("4️⃣ Anomaly Detection")
    data = np.random.randint(90, 150, size=15)
    mu = np.mean(data)
    sigma = np.std(data)
    k = st.slider("Anomaly Threshold Multiplier (k)", 1.0, 5.0, 2.0)
    anomalies = [x for x in data if is_anomaly(x, mu, sigma, k)]
    fig4, ax4 = plt.subplots(figsize=(10,4))
    ax4.plot(data, 'bo-', label='Data')
    for i, x in enumerate(data):
        if x in anomalies:
            ax4.plot(i, x, 'ro', markersize=10, label='Anomaly' if i==0 else "")
    ax4.axhline(mu + k*sigma, color='red', linestyle='--', label='Upper Threshold')
    ax4.axhline(mu - k*sigma, color='red', linestyle='--', label='Lower Threshold')
    ax4.set_title(f"{USER_NAME}'s Anomaly Detection")
    ax4.legend()
    st.pyplot(fig4)

# =========================
# --- RPA ROI Simulation ---
# =========================
elif menu == "RPA ROI Simulation":
    st.title(f"RPA ROI Simulation - By {USER_NAME}")
    cost_components = ["License", "Implementation", "Training", "Maintenance"]
    benefit_components = ["Labor Savings", "Error Reduction", "Compliance", "Efficiency"]
    costs = {c: np.random.randint(1000, 20000) for c in cost_components}
    benefits = {b: np.random.randint(5000, 40000) for b in benefit_components}
    st.write(f"{USER_NAME}'s Random Costs:", costs)
    st.write(f"{USER_NAME}'s Random Benefits:", benefits)
    
    total_costs = sum(costs.values())
    total_benefits = sum(benefits.values())
    roi_value = ((total_benefits - total_costs) / total_costs) * 100
    st.subheader("Results")
    st.write(f"Total Costs: ${total_costs:,}")
    st.write(f"Total Benefits: ${total_benefits:,}")
    st.write(f"ROI: {roi_value:.2f}%")
    if roi_value > 0:
        st.success(f"{USER_NAME}: Profitable! ✅")
    elif roi_value == 0:
        st.warning(f"{USER_NAME}: Break-even ⚠️")
    else:
        st.error(f"{USER_NAME}: Not profitable ❌")

# =========================
# --- KPI Comparison -----
# =========================
elif menu == "KPI Comparison":
    st.title(f"KPI Comparison Dashboard - By {USER_NAME}")
    datasets = [f"Project {c}" for c in ["A","B","C","D","E"]]
    dq_values = np.random.uniform(0.7, 1.0, size=len(datasets)).round(2)
    time_saved_values = np.random.randint(50, 200, size=len(datasets))
    roi_values = np.random.randint(-10, 50, size=len(datasets))
    efficiency_values = np.random.uniform(0.6, 1.0, size=len(datasets)).round(2)
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
    sns.heatmap(df_kpi.set_index('Dataset').T, annot=True, cmap='YlGnBu', ax=ax)
    st.pyplot(fig)
