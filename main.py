import streamlit as st

# App Title
st.title("CDC Opioid Prescribing Guidelines")

# Introduction
st.write("""
This application helps healthcare providers follow the CDC guidelines for prescribing opioids for chronic pain. By inputting patient-specific information, providers can receive recommendations aligned with best practices to ensure safe and effective pain management.
""")

# Collecting Patient Information
st.header("Patient Information")

age = st.number_input("Age", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", options=["Male", "Female", "Other"])
pain_severity = st.slider("Pain Severity (0 = No Pain, 10 = Worst Pain)", 0, 10, 5)
opioid_naive = st.selectbox("Is the patient opioid-naive?", options=["Yes", "No"])
co_morbid_conditions = st.multiselect("Select co-morbid conditions", ["COPD", "Sleep Apnea", "Depression", "Anxiety", "Substance Use Disorder", "None"])

# Provide Recommendations Based on Guidelines
st.header("Recommendations")

if opioid_naive == "Yes":
    st.write("Consider non-opioid therapies as the first-line treatment.")
    if pain_severity > 6:
        st.write("For severe pain, if opioids are considered, prescribe the lowest effective dose of immediate-release opioids.")
else:
    st.write("Evaluate the current opioid therapy and consider tapering to lower dosages or discontinuing if benefits do not outweigh harms.")
    if "Substance Use Disorder" in co_morbid_conditions:
        st.write("Exercise caution and consider consulting a specialist in addiction treatment.")

st.write("""
### General Guidelines:
1. **Non-Opioid Therapies**: Use non-opioid therapy for chronic pain outside of active cancer, palliative, and end-of-life care.
2. **Lowest Effective Dose**: When opioids are used, prescribe the lowest effective dose.
3. **Immediate-Release**: Start with immediate-release opioids rather than extended-release/long-acting opioids.
4. **Risk Assessment**: Evaluate risk factors for opioid-related harms before and during therapy.
5. **Monitoring**: Regularly review the patient's progress and adjust treatment as needed.
6. **Duration and Follow-Up**: Prescribe no greater quantity than needed for the expected duration of pain severe enough to require opioids.

Refer to the full [CDC guidelines](https://www.cdc.gov/drugoverdose/prescribing/guideline.html) for detailed information.
""")
