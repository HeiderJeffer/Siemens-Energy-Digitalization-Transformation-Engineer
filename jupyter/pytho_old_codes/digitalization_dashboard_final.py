# Siemens Energy Digitalization Unified Dashboard - Final Version
# Developed by Heider Jeffer

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
from typing import List
from io import BytesIO
import numpy as np

sns.set(style="whitegrid")

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

st.sidebar.title("Digitalization Dashboard v3 - By Heider Jeffer")
menu = st.sidebar.radio("Select Tool:", ["Siemens Metrics", "RPA ROI Calculator", "Automated Reports", "KPI Comparison"])

# =========================
# --- Siemens Metrics -----
# =========================

if menu == "Siemens Metrics":
    st.title("Siemens Energy Digitalization Metrics - By Heider Jeffer")
    
    # Efficiency Plot
    st.header("1. First 90 Days Efficiency")
    E_max = st.slider("Maximum Efficiency (E_max)", 0.0, 2.0, 1.0)
    days = list(range(91))
    efficiency = [efficiency_over_time(t, E_max) for t in days]
    fig, ax = plt.subplots(figsize=(10,5))
    ax.plot(days, efficiency, marker='o', color='green', label='Efficiency')
    ax.set_xlabel("Day")
    ax.set_ylabel("Efficiency")
    ax.set_title("First 90 Days Efficiency")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)
    
    # Data Quality Heatmap
    st.header("2. Data Quality Index Heatmap")
    errors_input = st.text_input("Enter errors per dataset (comma-separated)", "5,2,10")
    total_input = st.text_input("Enter total records per dataset (comma-separated)", "100,50,120")
    errors_list = list(map(int, errors_input.split(',')))
    total_list = list(map(int, total_input.split(',')))
    dq_values = [data_quality(e, t) for e, t in zip(errors_list, total_list)]
    df_dq = pd.DataFrame({'Dataset': range(len(dq_values)), 'Data_Quality': dq_values})
    fig2, ax2 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_dq[['Data_Quality']].T, annot=True, cmap='YlGnBu', cbar=True, ax=ax2)
    ax2.set_xlabel("Dataset Index")
    ax2.set_ylabel("Data Quality")
    st.pyplot(fig2)
    
    # Time Saved & ROI Heatmap
    st.header("3. Time Saved & ROI Heatmap")
    T_manual_list = list(map(float, st.text_input("Enter manual times (comma-separated)", "100,80,120").split(',')))
    R_list = list(map(float, st.text_input("Enter automation rates (comma-separated)", "0.6,0.5,0.7").split(',')))
    C_saved_list = list(map(float, st.text_input("Enter cost saved (comma-separated)", "20000,15000,25000").split(',')))
    C_project_list = list(map(float, st.text_input("Enter project cost (comma-separated)", "5000,7000,10000").split(',')))
    time_saved_values = [time_saved(t,r) for t,r in zip(T_manual_list, R_list)]
    roi_values = [roi(cs, cp) for cs, cp in zip(C_saved_list, C_project_list)]
    df_metrics = pd.DataFrame({
        'Time_Saved': time_saved_values,
        'ROI': roi_values
    })
    fig3, ax3 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_metrics.T, annot=True, cmap='coolwarm', cbar=True, ax=ax3)
    ax3.set_xlabel("Project Index")
    st.pyplot(fig3)
    
    # Anomaly Detection Interactive Plot
    st.header("4. Anomaly Detection")
    data_input = st.text_input("Enter dataset values (comma-separated)", "100,105,120,98,150,102")
    mu = st.number_input("Mean (mu)", value=100.0)
    sigma = st.number_input("Standard Deviation (sigma)", value=10.0)
    k = st.number_input("Threshold multiplier (k)", value=2.0)
    data = list(map(float, data_input.split(',')))
    anomalies = [x for x in data if is_anomaly(x, mu, sigma, k)]
    fig4, ax4 = plt.subplots(figsize=(10,4))
    ax4.plot(data, 'bo-', label='Data')
    for i, x in enumerate(data):
        if x in anomalies:
            ax4.plot(i, x, 'ro', markersize=10, label='Anomaly' if i==0 else "")
    ax4.axhline(mu + k*sigma, color='red', linestyle='--', label='Upper Threshold')
    ax4.axhline(mu - k*sigma, color='red', linestyle='--', label='Lower Threshold')
    ax4.set_xlabel("Index")
    ax4.set_ylabel("Value")
    ax4.set_title("Anomaly Detection")
    ax4.legend()
    st.pyplot(fig4)

# =========================
# --- RPA ROI Calculator ---
# =========================

elif menu == "RPA ROI Calculator":
    st.title("Interactive RPA ROI Calculator - By Heider Jeffer")
    
    st.header("1. Enter Costs")
    cost_components = ["License", "Implementation", "Training", "Maintenance"]
    costs = {c: st.number_input(f"{c} Cost ($):", min_value=0.0, value=0.0, step=100.0) for c in cost_components}
    
    st.header("2. Enter Benefits")
    benefit_components = ["Labor Savings", "Error Reduction", "Compliance", "Efficiency"]
    benefits = {b: st.number_input(f"{b} Benefit ($):", min_value=0.0, value=0.0, step=100.0) for b in benefit_components}
    
    if st.button("Calculate ROI"):
        roi_value = calculate_rpa_roi(costs, benefits)
        total_costs = sum(costs.values())
        total_benefits = sum(benefits.values())
        st.subheader("Results")
        st.write(f"**Total Costs:** ${total_costs:,.2f}")
        st.write(f"**Total Benefits:** ${total_benefits:,.2f}")
        st.write(f"**ROI:** {roi_value:.2f}%")
        if roi_value > 0:
            st.success("The RPA project is profitable! ✅")
        elif roi_value == 0:
            st.warning("Break-even. ⚠️")
        else:
            st.error("The RPA project is not profitable. ❌")

# =========================
# --- Automated Reports ----
# =========================

elif menu == "Automated Reports":
    st.title("Siemens Energy Automated Production Reports - By Heider Jeffer")
    st.markdown("""
Upload multiple factory Excel reports. The system will:
- Combine all files  
- Clean and normalize data  
- Summarize production units per day  
- Display trend charts and anomalies  
- Allow downloading the summary report
""")
    
    uploaded_files = st.file_uploader("Upload Excel files", type="xlsx", accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
        df_list = [pd.read_excel(file) for file in uploaded_files]
        df = pd.concat(df_list, ignore_index=True)
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df = df.dropna(subset=['Production_Units'])
        
        invalid_units = df[df['Production_Units'] < 0]
        if not invalid_units.empty:
            st.warning("⚠️ Found invalid Production_Units (negative values):")
            st.dataframe(invalid_units)
        
        summary = df.groupby('Date')['Production_Units'].sum().reset_index()
        st.subheader("Production Summary")
        st.dataframe(summary)
        
        # Production Trend Chart
        st.subheader("Production Trend")
        fig, ax = plt.subplots(figsize=(10,4))
        ax.plot(summary['Date'], summary['Production_Units'], marker='o', color='blue', label='Production Units')
        ax.set_xlabel("Date")
        ax.set_ylabel("Production Units")
        ax.set_title("Production Trend Over Time")
        ax.grid(True)
        st.pyplot(fig)
        
        # Anomaly Detection
        mu_prod = summary['Production_Units'].mean()
        sigma_prod = summary['Production_Units'].std()
        k_prod = st.slider("Anomaly Threshold Multiplier (k)", 1.0, 5.0, 2.0)
        anomalies_prod = summary[np.abs(summary['Production_Units'] - mu_prod) > k_prod*sigma_prod]
        st.subheader("Detected Anomalies")
        if anomalies_prod.empty:
            st.write("No anomalies detected ✅")
        else:
            st.dataframe(anomalies_prod)
        
        # Download summary report
        today = datetime.date.today()
        output_file_name = f"summary_report_{today}.xlsx"
        buffer = BytesIO()
        summary.to_excel(buffer, index=False)
        buffer.seek(0)
        st.download_button(
            label="Download Summary Report",
            data=buffer,
            file_name=output_file_name,
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    else:
        st.info("Upload one or more Excel files to start processing.")

# =========================
# --- KPI Comparison Section ---
# =========================

elif menu == "KPI Comparison":
    st.title("KPI Comparison Dashboard - By Heider Jeffer")
    
    st.markdown("""
Visualize key KPIs across datasets/projects:
- Data Quality  
- Time Saved  
- ROI  
- Efficiency
""")
    
    # User inputs
    datasets = st.text_input("Enter dataset/project names (comma-separated)", "Project A,Project B,Project C").split(',')
    dq_values = list(map(float, st.text_input("Enter Data Quality values (0-1, comma-separated)", "0.95,0.96,0.85").split(',')))
    time_saved_values = list(map(float, st.text_input("Enter Time Saved values, hours (comma-separated)", "100,120,90").split(',')))
    roi_values = list(map(float, st.text_input("Enter ROI percentages (comma-separated)", "25,30,-5").split(',')))
    efficiency_values = list(map(float, st.text_input("Enter Efficiency values (0-1, comma-separated)", "0.8,0.9,0.7").split(',')))
    
    df_kpi = pd.DataFrame({
        'Dataset': datasets,
        'Data_Quality': dq_values,
        'Time_Saved': time_saved_values,
        'ROI': roi_values,
        'Efficiency': efficiency_values
    })
    
    # Color-coded table for KPI
    def color_code(val, metric):
        if metric == 'ROI' or metric == 'Time_Saved' or metric == 'Efficiency':
            return 'background-color: #b3ffb3' if val > 0 else 'background-color: #ff9999'
        elif metric == 'Data_Quality':
            return 'background-color: #b3ffb3' if val >= 0.9 else 'background-color: #ff9999'
        return ''
    
    st.subheader("KPI Table")
    st.dataframe(df_kpi.style.applymap(lambda x: color_code(x, 'Data_Quality'), subset=['Data_Quality'])
                .applymap(lambda x: color_code(x, 'Time_Saved'), subset=['Time_Saved'])
                .applymap(lambda x: color_code(x, 'ROI'), subset=['ROI'])
                .applymap(lambda x: color_code(x, 'Efficiency'), subset=['Efficiency']))
    
    # KPI Heatmap
    st.subheader("KPI Heatmap")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.heatmap(df_kpi.set_index('Dataset').T, annot=True, cmap='YlGnBu', cbar=True, ax=ax)
    ax.set_ylabel("KPI")
    ax.set_xlabel("Dataset/Project")
    st.pyplot(fig)
