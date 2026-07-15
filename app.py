import streamlit as st
import pickle

with open('iris_model.pkl', 'rb') as file:
    classifier = pickle.load(file)

st.title("Iris Classification App")


st.write("used for iris classification")

sl=st.number_input(label="Enter Sepal Length")
sw=st.number_input(label="Enter Sepal Width")
pl=st.number_input(label="Enter Petal Length")
pw=st.number_input(label="Enter Petal Width")


if st.button("Predict"):
    result=classifier.predict([[sl,sw,pl,pw]])
    st.success(result[0])




