# Siemens Energy Digitalization Unified Dashboard
# Streamlit Version by Heider Jeffer

import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime
from typing import List
from io import BytesIO

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
    if t < 0: return 0.0
    t = min(t, 90)
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

st.sidebar.title("Digitalization Dashboard")
menu = st.sidebar.radio("Select Tool:", ["Siemens Metrics", "RPA ROI Calculator", "Automated Reports"])

# =========================
# --- Siemens Metrics -----
# =========================

if menu == "Siemens Metrics":
    st.title("Siemens Energy Digitalization Metrics")
    
    st.header("1. First 90 Days Efficiency")
    E_max = st.slider("Maximum Efficiency (E_max)", 0.0, 2.0, 1.0)
    days = list(range(91))
    efficiency = [efficiency_over_time(t, E_max) for t in days]
    fig, ax = plt.subplots()
    ax.plot(days, efficiency, marker='o', color='green')
    ax.set_xlabel("Day")
    ax.set_ylabel("Efficiency")
    ax.set_title("First 90 Days Efficiency")
    st.pyplot(fig)
    
    st.header("2. Data Quality Index")
    errors_input = st.text_input("Enter errors per dataset (comma-separated)", "5,2,10")
    total_input = st.text_input("Enter total records per dataset (comma-separated)", "100,50,120")
    errors_list = list(map(int, errors_input.split(',')))
    total_list = list(map(int, total_input.split(',')))
    dq_values = [data_quality(e, t) for e, t in zip(errors_list, total_list)]
    fig2, ax2 = plt.subplots()
    sns.barplot(x=list(range(len(dq_values))), y=dq_values, color='skyblue', ax=ax2)
    ax2.set_ylim(0,1)
    ax2.set_xlabel("Dataset")
    ax2.set_ylabel("Data Quality")
    ax2.set_title("Data Quality Index per Dataset")
    st.pyplot(fig2)
    
    st.header("3. Time Saved & ROI")
    T_manual_list = list(map(float, st.text_input("Enter manual times (comma-separated)", "100,80,120").split(',')))
    R_list = list(map(float, st.text_input("Enter automation rates (comma-separated)", "0.6,0.5,0.7").split(',')))
    C_saved_list = list(map(float, st.text_input("Enter cost saved (comma-separated)", "20000,15000,25000").split(',')))
    C_project_list = list(map(float, st.text_input("Enter project cost (comma-separated)", "5000,7000,10000").split(',')))
    time_saved_values = [time_saved(t,r) for t,r in zip(T_manual_list, R_list)]
    roi_values = [roi(cs, cp) for cs, cp in zip(C_saved_list, C_project_list)]
    fig3, ax3 = plt.subplots()
    ax3.bar([i-0.2 for i in range(len(time_saved_values))], time_saved_values, width=0.4, label='Time Saved')
    ax3.bar([i+0.2 for i in range(len(roi_values))], roi_values, width=0.4, label='ROI (%)')
    ax3.set_xticks(range(len(time_saved_values)))
    ax3.set_title("Time Saved and ROI Comparison")
    ax3.set_xlabel("Project Index")
    ax3.set_ylabel("Value")
    ax3.legend()
    st.pyplot(fig3)
    
    st.header("4. Anomaly Detection")
    data_input = st.text_input("Enter dataset values (comma-separated)", "100,105,120,98,150,102")
    mu = st.number_input("Mean (mu)", value=100.0)
    sigma = st.number_input("Standard Deviation (sigma)", value=10.0)
    k = st.number_input("Threshold multiplier (k)", value=2.0)
    data = list(map(float, data_input.split(',')))
    anomalies = [x for x in data if is_anomaly(x, mu, sigma, k)]
    fig4, ax4 = plt.subplots()
    ax4.plot(data, 'bo-', label='Data')
    for i, x in enumerate(data):
        if x in anomalies:
            ax4.plot(i, x, 'ro', markersize=10, label='Anomaly' if i==0 else "")
    ax4.axhline(mu + k*sigma, color='red', linestyle='--', label='Threshold')
    ax4.axhline(mu - k*sigma, color='red', linestyle='--')
    ax4.set_xlabel("Index")
    ax4.set_ylabel("Value")
    ax4.set_title("Anomaly Detection")
    ax4.legend()
    st.pyplot(fig4)

# =========================
# --- RPA ROI Calculator ---
# =========================

elif menu == "RPA ROI Calculator":
    st.title("Interactive RPA ROI Calculator")
    
    st.header("1. Enter Costs")
    cost_components = ["License", "Implementation", "Training", "Maintenance"]
    costs = {}
    for component in cost_components:
        costs[component] = st.number_input(f"{component} Cost ($):", min_value=0.0, value=0.0, step=100.0)
    
    st.header("2. Enter Benefits")
    benefit_components = ["Labor Savings", "Error Reduction", "Compliance", "Efficiency"]
    benefits = {}
    for component in benefit_components:
        benefits[component] = st.number_input(f"{component} Benefit ($):", min_value=0.0, value=0.0, step=100.0)
    
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
# --- Automated Reports ---
# =========================

elif menu == "Automated Reports":
    st.title("Siemens Energy Automated Production Reports")
    st.markdown("""
Upload multiple factory Excel reports. The system will:
- Combine all files  
- Clean and normalize data  
- Summarize production units per day  
- Allow downloading the summary report
""")
    
    uploaded_files = st.file_uploader("Upload Excel files", type="xlsx", accept_multiple_files=True)
    
    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
        df_list = []
        for file in uploaded_files:
            temp = pd.read_excel(file)
            st.write(f"**{file.name}**: {len(temp)} rows ingested")
            df_list.append(temp)
        
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
        
        # Download button
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
