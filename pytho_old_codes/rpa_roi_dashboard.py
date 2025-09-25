# Interactive RPA ROI Calculator
# Using Streamlit
# By Heider Jeffer

import streamlit as st

# --- Function to calculate RPA ROI ---
def calculate_rpa_roi(costs dict, benefits dict) - float
    total_costs = sum(costs.values())
    total_benefits = sum(benefits.values())
    if total_costs == 0
        st.error(Total costs cannot be zero.)
        return 0.0
    roi = ((total_benefits - total_costs)  total_costs)  100
    return roi

# --- Streamlit App ---
st.title(Interactive RPA ROI Calculator)

st.header(1. Enter Costs)
cost_components = [License, Implementation, Training, Maintenance]
costs = {}
for component in cost_components
    costs[component] = st.number_input(f{component} Cost ($), min_value=0.0, value=0.0, step=100.0)

st.header(2. Enter Benefits)
benefit_components = [Labor Savings, Error Reduction, Compliance, Efficiency]
benefits = {}
for component in benefit_components
    benefits[component] = st.number_input(f{component} Benefit ($), min_value=0.0, value=0.0, step=100.0)

# --- Calculate ROI ---
if st.button(Calculate ROI)
    roi_value = calculate_rpa_roi(costs, benefits)
    total_costs = sum(costs.values())
    total_benefits = sum(benefits.values())
    
    st.subheader(Results)
    st.write(fTotal Costs ${total_costs,.2f})
    st.write(fTotal Benefits ${total_benefits,.2f})
    st.write(fROI {roi_value.2f}%)
    
    # Optional Color-coded message
    if roi_value  0
        st.success(The RPA project is profitable! ✅)
    elif roi_value == 0
        st.warning(Break-even. ⚠️)
    else
        st.error(The RPA project is not profitable. ❌)
