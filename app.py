import streamlit as st
import os

# Set Page Title and Icon
st.set_page_config(page_title='Student Depression Analytics', page_icon='📊', layout='wide')

# Title of the Portfolio
st.title('📊 Student Depression Analytics Dashboard')

# Display Thumbnail Image
st.image('Analytics Thumbnail.png', caption='Student Depression Analytics Dashboard', use_container_width=True)

# Introduction
st.markdown("""
### 📌 About This Dashboard
This interactive Tableau dashboard analyzes factors contributing to student depression, including:
- Sleep duration, study hours, financial stress, and more.
- Gender and age group breakdowns.
- Correlations between academic pressure and mental health.
""")

# Debugging: Show current working directory & files
st.write("Current Directory:", os.getcwd())
st.write("Files in Directory:", os.listdir())

# Load Image from Project Directory
image_path = "Analytics_Thumbnail.png"  # Ensure this file is in the same directory as app.py
if os.path.exists(image_path):
    st.image(image_path, caption='Student Depression Analytics Dashboard', use_container_width=True)
else:
    st.warning(f"Image not found: {image_path}")

# Link to Tableau Dashboard
st.markdown("""
### 🎯 Project Overview  
This Tableau dashboard analyzes **student depression trends** based on factors like **sleep, academic pressure, diet, study hours, and financial stress**.  
It provides insights into **how different factors impact mental health** and what patterns emerge in student well-being.  

### 📈 View the Full Interactive Dashboard
🔗 **[Click Here to Open Tableau Dashboard](https://public.tableau.com/app/profile/sriram.tc/viz/StudentDepressionAnalyticsMarch/DepressionAnalytics?publish=yes)**
""")

# Section: Objectives, Real-World Impact & Insights for Each Sheet
st.header('🔍 Dashboard Sheets: Objectives, Insights & Real-World Impact')

sheets = {
    "1️⃣ Depression by Gender": {
        "Objective": "Understand how depression rates vary between male and female students.",
        "Insights": "Females show slightly higher depression rates, indicating societal or psychological pressures.",
        "Real-World Impact": "Encourages gender-specific mental health programs in educational institutions."
    },
    "2️⃣ Depression by Age Group": {
        "Objective": "Analyze whether depression is more common in younger or older students.",
        "Insights": "Students aged 18-24 (A1 group) exhibit the highest depression rates.",
        "Real-World Impact": "Early intervention programs should be designed for freshmen and younger students."
    },
    "3️⃣ Depression Count by Sleep Duration": {
        "Objective": "Examine the relationship between sleep patterns and depression.",
        "Insights": "Less than 5 hours of sleep significantly increases depression risk.",
        "Real-World Impact": "Promotes sleep awareness campaigns in universities."
    },
    "4️⃣ Academic Pressure vs Depression": {
        "Objective": "Determine if academic stress correlates with depression levels.",
        "Insights": "Higher academic pressure correlates strongly with higher depression rates.",
        "Real-World Impact": "Educational institutions should emphasize mental well-being alongside academic excellence."
    },
    "5️⃣ Dietary Habits vs Depression": {
        "Objective": "Investigate whether diet impacts student mental health.",
        "Insights": "Unhealthy diets correspond to higher depression rates.",
        "Real-World Impact": "Encourages universities to offer healthier meal options."
    },
    "6️⃣ Financial Stress vs Depression": {
        "Objective": "Analyze the role of financial burdens on depression.",
        "Insights": "Students facing financial difficulties show increased depression cases.",
        "Real-World Impact": "Suggests the need for financial aid programs and scholarships."
    },
    "7️⃣ Study Hours vs Depression": {
        "Objective": "Find the optimal study hours for mental well-being.",
        "Insights": "Both excessive (>10 hrs) and minimal (<3 hrs) study time correlate with high depression.",
        "Real-World Impact": "Balanced study schedules should be encouraged."
    },
    "8️⃣ Family History of Mental Illness vs Depression": {
        "Objective": "See if genetic factors impact depression levels.",
        "Insights": "Students with a family history of mental illness have higher depression rates.",
        "Real-World Impact": "Encourages targeted counseling services."
    },
    "9️⃣ Suicidal Thoughts vs Depression": {
        "Objective": "Identify the relationship between depression and suicidal tendencies.",
        "Insights": "Most students with depression report suicidal thoughts, highlighting a critical issue.",
        "Real-World Impact": "Universities should implement suicide prevention programs."
    },
    "🔟 Overall Insights & Recommendations": {
        "Objective": "Summarize findings and provide key recommendations.",
        "Insights": "Academic pressure, sleep deprivation, financial stress, and unhealthy habits are major contributors to depression.",
        "Real-World Impact": "Comprehensive student wellness programs must be implemented in universities."
    }
}

for sheet, details in sheets.items():
    with st.expander(sheet):
        st.write(f"**Objective:** {details['Objective']}")
        st.write(f"**Insights:** {details['Insights']}")
        st.write(f"**Real-World Impact:** {details['Real-World Impact']}")


st.markdown("""
## 💡 Conclusion  
This analysis highlights **key lifestyle and academic factors affecting student depression**.  
By identifying these triggers, educational institutions can implement **targeted interventions** to improve student well-being.
""")

# Download Section
tableau_file = "Student_Depression_Analytics.twb"  # Ensure this file is in the same directory
if os.path.exists(tableau_file):
    with open(tableau_file, 'rb') as f:
        st.download_button(label='Download Tableau Workbook', data=f, file_name='Student_Depression_Analytics.twb', mime='application/octet-stream')
else:
    st.warning(f"Tableau file not found: {tableau_file}")

# Footer
st.markdown("---")
st.markdown("👨‍💻 **Built by Sriram | Data Analytics Portfolio**")
