import streamlit as st

st.set_page_config(layout="wide")

st.title("📈 Mi Stock Dashboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("AVTX", "7.70", "+3.2%")

with col2:
    st.metric("ABVX", "90.27", "+1.5%")

with col3:
    st.metric("NVDA", "220.50", "+0.8%")

st.write("Dashboard en construcción...")
