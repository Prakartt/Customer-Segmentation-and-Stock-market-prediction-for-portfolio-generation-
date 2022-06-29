import streamlit as st

st.title("Customer Segementation")

col1, col2 , col3 = st.columns(3)

with col1:
    st.subheader("Age")
    age = st.slider('', min_value= 18 , max_value=90)  # 👈 this is a widget

    st.subheader("Education")
    education = st.radio("What is your level of Education" , ('Primary', 'Secondary', 'Tertiary') , key = "education")

    st.subheader("Job")
    job = st.radio("Current Job level", ('blue-collar', 'management', 'technician',
                                         'admin', 'services', 'retired', 'self-employed',
                                         'entrepreneur', 'unemployed', 'housemaid', 'student',
                                         'other'), key="job")

with col2:
    st.subheader(" ")
#
# Jobs = 'blue-collar', 'management', 'technician', 'admin.', 'services',
#        'retired', 'self-employed', 'entrepreneur', 'unemployed', 'housemaid',
#        # 'student', 'unknown'

with col3:

    st.subheader("Balance")
    balance = st.slider("", min_value=100, max_value=850000 , step = 100)


    st.subheader("Marital Status")
    marital = st.radio("Current Marital Status", ("Single", 'Married', 'Divorced'), key = 'marital')

    st.subheader("Housing")
    housing = st.radio("Do you own a house" , ('Yes','No' ) , key = "housing")

    st.subheader("Loan")
    loan = st.radio("Do you have a loan" , ('Yes','No' ) , key = "loan")




st.header("Customer Details: ")
col4, col5 , col6 = st.columns(3)
with col4:
    st.write("Age: ", age)
    st.write("Balance: ", balance)
    st.write("Education-Level: ", education)

with col5:
    st.write("Job Category: ", job)
    st.write("Marital-Status: ", marital)
    st.write("Loan Status: ", loan)

with col6:
    st.write("Housing: ", housing)


