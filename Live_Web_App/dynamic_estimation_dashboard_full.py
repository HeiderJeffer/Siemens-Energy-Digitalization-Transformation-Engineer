# Dynamic Estimation Dashboard with Machine Learning - By Heider Jeffer
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
from sklearn.linear_model import LinearRegression

sns.set(style="whitegrid")

# =========================
# --- User Info ----------
# =========================
USER_NAME = "Heider Jeffer"
ORG_NAME = "Siemens Energy Digitalization Transformation Engineer"

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
st.sidebar.markdown(f"**Made for {ORG_NAME}**")

# Add "AI" to the menu list so it appears in the sidebar
menu = st.sidebar.radio(
    "Select Tool:",
    ["Dynamic Metrics", "RPA ROI Simulation", "KPI Comparison", "AI"]
	# ["Dynamic Metrics", "RPA ROI Simulation", "KPI Comparison", "Machine Learning", "AI"]


)


# =========================
# --- Dynamic Metrics -----
# =========================
if menu == "Dynamic Metrics":
    st.title(f"Dynamic Estimation Metrics - By {USER_NAME}")
    st.markdown(f"**Tailored for {ORG_NAME}**")
    
    # 1️⃣ Efficiency
    st.header("1️⃣ First 90 Days Efficiency")
    E_max = st.slider("Maximum Efficiency (E_max)", 0.5, 1.5, 1.0)
    days = list(range(91))
    efficiency = [efficiency_over_time(t, E_max) for t in days]
    fig, ax = plt.subplots(figsize=(10,4))
    ax.plot(days, efficiency, marker='o', color='green', label='Efficiency')
    ax.set_xlabel("Day")
    ax.set_ylabel("Efficiency")
    st.pyplot(fig)

    # 2️⃣ Data Quality
    st.header("2️⃣ Data Quality Simulation")
    mode_dq = st.radio("Select Input Mode:", ["Random", "Manual"], key="dq_mode")
    if mode_dq == "Random":
        N_datasets = st.slider("Number of Datasets", 2, 10, 5)
        errors_list = np.random.randint(0, 20, size=N_datasets)
        total_list = np.random.randint(50, 200, size=N_datasets)
    else:
        errors_input = st.text_input("Enter errors per dataset (comma-separated)", "5,2,10")
        total_input = st.text_input("Enter total records per dataset (comma-separated)", "100,50,120")
        errors_list = list(map(int, errors_input.split(',')))
        total_list = list(map(int, total_input.split(',')))
        N_datasets = len(errors_list)
    dq_values = [data_quality(e, t) for e, t in zip(errors_list, total_list)]
    df_dq = pd.DataFrame({'Dataset': [f"DS{i+1}" for i in range(N_datasets)], 'Data_Quality': dq_values})
    st.dataframe(df_dq)
    fig2, ax2 = plt.subplots(figsize=(6,3))
    sns.heatmap(df_dq[['Data_Quality']].T, annot=True, cmap='YlGnBu', ax=ax2)
    st.pyplot(fig2)

    # 3️⃣ Time Saved & ROI
    st.header("3️⃣ Time Saved & ROI Simulation")
    mode_roi = st.radio("Select Input Mode:", ["Random", "Manual"], key="roi_mode")
    if mode_roi == "Random":
        T_manual_list = np.random.randint(50, 200, size=N_datasets)
        R_list = np.random.uniform(0.3, 0.9, size=N_datasets)
        C_saved_list = np.random.randint(10000, 50000, size=N_datasets)
        C_project_list = np.random.randint(5000, 20000, size=N_datasets)
    else:
        T_manual_input = st.text_input("Manual times (comma-separated)", "100,120,90")
        R_input = st.text_input("Automation rates (comma-separated)", "0.6,0.5,0.7")
        C_saved_input = st.text_input("Cost saved (comma-separated)", "20000,15000,25000")
        C_project_input = st.text_input("Project cost (comma-separated)", "5000,7000,10000")
        T_manual_list = list(map(float, T_manual_input.split(',')))
        R_list = list(map(float, R_input.split(',')))
        C_saved_list = list(map(float, C_saved_input.split(',')))
        C_project_list = list(map(float, C_project_input.split(',')))
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

    # 4️⃣ Anomaly Detection
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

    # Excel export
    st.header("💾 Download Metrics Report")
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_dq.to_excel(writer, sheet_name='Data_Quality', index=False)
        df_metrics.to_excel(writer, sheet_name='TimeSaved_ROI', index=False)
        pd.DataFrame({'Data': data, 'Anomaly': [x in anomalies for x in data]}).to_excel(writer, sheet_name='Anomalies', index=False)
    buffer.seek(0)
    st.download_button(
        label="Download Excel Report",
        data=buffer,
        file_name=f"{USER_NAME}_dynamic_estimation.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# =========================
# --- RPA ROI Simulation ---
# =========================
elif menu == "RPA ROI Simulation":
    st.title(f"RPA ROI Simulation - By {USER_NAME}")
    st.markdown(f"**Tailored for {ORG_NAME}**")
    mode_rpa = st.radio("Select Input Mode:", ["Random", "Manual"], key="rpa_mode")
    cost_components = ["License", "Implementation", "Training", "Maintenance"]
    benefit_components = ["Labor Savings", "Error Reduction", "Compliance", "Efficiency"]
    
    if mode_rpa == "Random":
        costs = {c: np.random.randint(1000, 20000) for c in cost_components}
        benefits = {b: np.random.randint(5000, 40000) for b in benefit_components}
    else:
        costs_input = st.text_input("Enter costs per component (comma-separated, License,Implementation,Training,Maintenance)", "10000,15000,12000,8000")
        benefits_input = st.text_input("Enter benefits per component (comma-separated, Labor Savings,Error Reduction,Compliance,Efficiency)", "25000,15000,10000,20000")
        costs_list = list(map(int, costs_input.split(',')))
        benefits_list = list(map(int, benefits_input.split(',')))
        costs = dict(zip(cost_components, costs_list))
        benefits = dict(zip(benefit_components, benefits_list))
    
    st.write(f"{USER_NAME}'s Costs:", costs)
    st.write(f"{USER_NAME}'s Benefits:", benefits)
    
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
    
    # Excel export
    st.header("💾 Download RPA ROI Report")
    buffer = BytesIO()
    df_costs = pd.DataFrame(list(costs.items()), columns=['Cost Component', 'Amount'])
    df_benefits = pd.DataFrame(list(benefits.items()), columns=['Benefit Component', 'Amount'])
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_costs.to_excel(writer, sheet_name='Costs', index=False)
        df_benefits.to_excel(writer, sheet_name='Benefits', index=False)
        pd.DataFrame({'ROI (%)': [roi_value]}).to_excel(writer, sheet_name='ROI', index=False)
    buffer.seek(0)
    st.download_button(
        label="Download RPA Excel Report",
        data=buffer,
        file_name=f"{USER_NAME}_RPA_ROI.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

# =========================
# --- KPI Comparison -----
# =========================
elif menu == "KPI Comparison":
    st.title(f"KPI Comparison Dashboard - By {USER_NAME}")
    st.markdown(f"**Tailored for {ORG_NAME}**")
    mode_kpi = st.radio("Select Input Mode:", ["Random", "Manual"], key="kpi_mode")
    datasets = [f"Project {c}" for c in ["A","B","C","D","E"]]

    if mode_kpi == "Random":
        dq_values = np.random.uniform(0.7, 1.0, size=len(datasets)).round(2)
        time_saved_values = np.random.randint(50, 200, size=len(datasets))
        roi_values = np.random.randint(-10, 50, size=len(datasets))
        efficiency_values = np.random.uniform(0.6, 1.0, size=len(datasets)).round(2)
    else:
        dq_input = st.text_input("Data Quality (comma-separated 0-1)", "0.95,0.92,0.85,0.88,0.90")
        ts_input = st.text_input("Time Saved (comma-separated)", "100,120,90,150,80")
        roi_input = st.text_input("ROI % (comma-separated)", "25,30,-5,10,15")
        eff_input = st.text_input("Efficiency (0-1, comma-separated)", "0.8,0.9,0.7,0.85,0.95")
        dq_values = list(map(float, dq_input.split(',')))
        time_saved_values = list(map(float, ts_input.split(',')))
        roi_values = list(map(float, roi_input.split(',')))
        efficiency_values = list(map(float, eff_input.split(',')))

    df_kpi = pd.DataFrame({
        'Dataset': datasets,
        'Data_Quality': dq_values,
        'Time_Saved': time_saved_values,
        'ROI': roi_values,
        'Efficiency': efficiency_values
    })

    st.header("KPI Table with Anomaly Highlighting")
    k_anom = st.slider("Anomaly Threshold Multiplier (k)", 1.0, 5.0, 2.0)

    def highlight_anomaly(val, col):
        mean = df_kpi[col].mean()
        std = df_kpi[col].std()
        if std == 0:
            return ''
        if abs(val - mean) > k_anom * std:
            return 'background-color: #ff9999'
        return 'background-color: #b3ffb3'

    st.dataframe(df_kpi.style.applymap(lambda x: highlight_anomaly(x, 'Data_Quality'), subset=['Data_Quality'])
                          .applymap(lambda x: highlight_anomaly(x, 'Time_Saved'), subset=['Time_Saved'])
                          .applymap(lambda x: highlight_anomaly(x, 'ROI'), subset=['ROI'])
                          .applymap(lambda x: highlight_anomaly(x, 'Efficiency'), subset=['Efficiency']))

    st.header("KPI Heatmap with Anomalies")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.heatmap(df_kpi.set_index('Dataset').T, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.header("💾 Download KPI Report")
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        df_kpi.to_excel(writer, sheet_name='KPI', index=False)
    buffer.seek(0)
    st.download_button(
        label="Download KPI Excel Report",
        data=buffer,
        file_name=f"{USER_NAME}_KPI_Comparison.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )



# =========================
# --- Machine Learning ----
# =========================
elif menu == "Machine Learning":
    st.title(f"Machine Learning Module - By {USER_NAME}")
    st.markdown(f"**Tailored for {ORG_NAME}**")
    
    # Sample KPI-like data
    N = st.slider("Number of datasets", 10, 50, 20)
    np.random.seed(42)
    df_ml = pd.DataFrame({
        'Data_Quality': np.random.uniform(0.7, 1.0, N).round(2),
        'Time_Saved': np.random.randint(50, 200, N),
        'ROI': np.random.randint(-10, 50, N),
        'Efficiency': np.random.uniform(0.6, 1.0, N).round(2)
    })
    st.dataframe(df_ml.head())

    # Train Linear Regression
    from sklearn.linear_model import LinearRegression
    X = df_ml[['Data_Quality', 'Time_Saved', 'Efficiency']]
    y = df_ml['ROI']
    model = LinearRegression()
    model.fit(X, y)
    df_ml['Predicted_ROI'] = model.predict(X)

    st.subheader("Predicted ROI & Coefficients")
    st.dataframe(pd.DataFrame({'Feature': X.columns, 'Coefficient': model.coef_}))
    st.write(f"Intercept: {model.intercept_:.2f}")
    
    # Anomaly Detection
    k = st.slider("Anomaly Threshold Multiplier (k)", 1.0, 5.0, 2.0)
    mu = df_ml['ROI'].mean()
    sigma = df_ml['ROI'].std()
    df_ml['Anomaly'] = df_ml['ROI'].apply(lambda x: abs(x - mu) > k*sigma)
    st.dataframe(df_ml)

    # Distribution Plot
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(df_ml['ROI'], color='blue', kde=True, stat="density", bins=15, ax=ax)
    sns.histplot(df_ml['Predicted_ROI'], color='green', kde=True, stat="density", bins=15, ax=ax, alpha=0.6)
    ax.set_title("Actual vs Predicted ROI Distribution")
    st.pyplot(fig)

# =========================
# --- AI Module -----------
# =========================
elif menu == "AI":
    st.title(f"AI Insights Module - By {USER_NAME}")
    st.markdown(f"**Tailored for {ORG_NAME}**")

    # Sample project data
    datasets = [f"Project {c}" for c in ["A","B","C","D","E"]]
    df_ai = pd.DataFrame({
        'Dataset': datasets,
        'Data_Quality': np.random.uniform(0.7, 1.0, len(datasets)).round(2),
        'Time_Saved': np.random.randint(50, 200, len(datasets)),
        'ROI': np.random.randint(-10, 50, len(datasets)),
        'Efficiency': np.random.uniform(0.6, 1.0, len(datasets)).round(2)
    })

    st.header("Project Summary")
    st.dataframe(df_ai)

    st.header("AI Insights")
    avg_roi = df_ai['ROI'].mean()
    df_ai['AI_Insight'] = df_ai['ROI'].apply(lambda x: "Low ROI ⚠️" if x < avg_roi else "Healthy ROI ✅")
    st.dataframe(df_ai[['Dataset', 'ROI', 'AI_Insight']])

    st.header("ROI Distribution")
    fig, ax = plt.subplots(figsize=(10,5))
    sns.histplot(df_ai['ROI'], color='purple', kde=True, bins=10, ax=ax)
    ax.set_title("AI ROI Distribution Across Projects")
    st.pyplot(fig)