import streamlit as st
from pickle import load
import pandas as pd



QT_balance = load(open('QT_balance.pkl', 'rb'))
QT_age = load(open('QT_age.pkl', 'rb'))
transformer_file = load(open('transformer.pkl', 'rb'))
kmeans_file = load(open('kmeans.pkl', 'rb'))


st.title("Stock Market Portfolio Advisor")

col1, col2 , col3 = st.columns(3)

with col1:
    st.subheader("Age")
    age = st.slider('', min_value= 18 , max_value=90)  # 👈 this is a widget

    st.subheader("Education")
    education = st.radio("What is your level of Education" , ('primary', 'secondary', 'tertiary', 'others') , key = "education")

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
    balance = st.slider("", min_value=100, max_value= 11000 , step = 100)


    st.subheader("Marital Status")
    marital = st.radio("Current Marital Status", ("single", 'married', 'divorced'), key = 'marital')

    st.subheader("Housing")
    housing = st.radio("Do you own a house" , ('yes','no' ) , key = "housing")

    st.subheader("Loan")
    loan = st.radio("Do you have a loan" , ('yes','no' ) , key = "loan")




st.header("Your Details: ")
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


if st.button("Submit"):
    if job == 'admin':
        job = 'admin.'
    temp = {
        'age': age,
        'job': job,
        'marital': marital,
        'education': education,
        'balance': balance,
        'housing': housing,
        'loan': loan}

    temp = pd.DataFrame(temp , index = [0])
    temp['balance'] = QT_balance.transform(temp['balance'].values.reshape(-1,1))
    temp['age'] = QT_age.transform(temp['age'].values.reshape(-1,1))
    temp = transformer_file.transform(temp)
    answer = kmeans_file.predict(temp)
    print(temp)
    print(answer)
    #st.header(answer)

    if answer[0] == 0:
        st.header(" Portfolio Mix:")
        st.subheader("95% to BAC(Bank of America)")
        st.subheader("5% to PG(Proctor Gamble) ")

    elif answer[0] == 1:
        st.header(" Portfolio Mix:")
        st.subheader("95% to PFE(Pfizer) ")
        st.subheader("5% to APPL(Apple) ")


    elif answer[0] == 2:
        st.header(" Portfolio Mix:")
        st.subheader("85% to BAC(Bank of America) ")
        st.subheader("10% to PG(Proctor Gamble) ")
        st.subheader("5% to XOM(Exxon mobil) ")


    elif answer[0] == 3:
        st.header(" Portfolio Mix:")
        st.subheader("90% to PFE(Pfizer) ")
        st.subheader("5% to BAC(Bank of America) ")
        st.subheader("5% to XOM(Exxon mobil) ")

    elif answer[0] == 4:
        #st.header(" Portfolio Mix: \n 80% to BAC(Bank of America) \n 10% to PG(Proctor Gamble) \n 5% to BAC(Bank of America) \n 5% to XOM(Exxon mobil) \n 5% to PFE(Pfizer) ")
        st.header(" Portfolio Mix:")
        st.subheader("80% to BAC(Bank of America) ")
        st.subheader("10% to PG(Proctor Gamble) ")
        st.subheader("5% to PFE(Pfizer) ")
        st.subheader("5% to XOM(Exxon mobil) ")

    elif answer[0] == 5:
        #st.header(" Portfolio Mix: \n 90% to BAC(Bank of America) \n 5% to PG(Proctor Gamble) \n 5% to APPL(Apple) ")
        st.header(" Portfolio Mix:")
        st.subheader("90% to BAC(Bank of America) ")
        st.subheader("5% to  APPL(Apple) ")
        st.subheader("5% to XOM(Exxon mobil) ")
    elif answer[0] == 6:

        st.header(" Portfolio Mix:")
        st.subheader("75% to BAC(Bank of America)")
        st.subheader("15% to PG(Proctor Gamble) ")
        st.subheader("5% to APPL(Apple)")
        st.subheader("5% to XOM(Exxon mobil) ")

    elif answer[0] == 7:

        st.header(" Portfolio Mix:")
        st.subheader("80% to BAC(Bank of America)")
        st.subheader("15% to PG(Proctor Gamble)")
        st.subheader("5% to PFE(Pfizer)")


    elif answer[0] == 8:
        st.header(" Portfolio Mix:")
        st.subheader("85% to PFE(Pfizer)")
        st.subheader("5% to BAC(Bank of America)")
        st.subheader("5% to APPL(Apple)")
        st.subheader("5% to XOM(Exxon mobil)")

    elif answer[0] == 9:
        st.header(" Portfolio Mix:")
        st.subheader("75% to BAC(Bank of America)")
        st.subheader("20% to PFE(Pfizer)")
        st.subheader("5% to PG(Proctor Gamble)")

