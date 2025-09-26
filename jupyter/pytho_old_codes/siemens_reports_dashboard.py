# Siemens Energy Digitalization Transformation Engineer
# Interactive Streamlit Version
# By Heider Jeffer

import streamlit as st
import pandas as pd
import datetime

st.title(Siemens Energy Automated Production Summary)

st.markdown(
Upload multiple factory Excel reports. The system will
- Combine all files  
- Clean and normalize data  
- Summarize production units per day  
- Allow downloading the summary report
)

# --- Step 1 File upload ---
uploaded_files = st.file_uploader(Upload Excel files, type=xlsx, accept_multiple_files=True)

if uploaded_files
    st.success(f{len(uploaded_files)} file(s) uploaded successfully!)

    df_list = []
    for file in uploaded_files
        temp = pd.read_excel(file)
        st.write(f{file.name} {len(temp)} rows ingested)
        df_list.append(temp)

    # --- Step 2 Combine data ---
    df = pd.concat(df_list, ignore_index=True)

    # --- Step 3 Clean data ---
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Production_Units'])

    # --- Step 4 Data quality check ---
    invalid_units = df[df['Production_Units']  0]
    if not invalid_units.empty
        st.warning(⚠️ Found invalid Production_Units (negative values))
        st.dataframe(invalid_units)

    # --- Step 5 Aggregate & summarize ---
    summary = df.groupby('Date')['Production_Units'].sum().reset_index()
    st.subheader(Production Summary)
    st.dataframe(summary)

    # --- Step 6 Download report ---
    today = datetime.date.today()
    output_file_name = fsummary_report_{today}.xlsx

    # Create a downloadable Excel file
    from io import BytesIO
    buffer = BytesIO()
    summary.to_excel(buffer, index=False)
    buffer.seek(0)

    st.download_button(
        label=Download Summary Report,
        data=buffer,
        file_name=output_file_name,
        mime=applicationvnd.openxmlformats-officedocument.spreadsheetml.sheet
    )
else
    st.info(Upload one or more Excel files to start processing.)
