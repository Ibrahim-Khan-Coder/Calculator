# -*- coding: utf-8 -*-
"""Calculator.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dl_LQ_2kIen0iCFLUt13e31FAzLumO9C
"""

import streamlit as st
import math

# Calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=10):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

# Streamlit UI
st.title("Scientific Calculator")

operation = st.selectbox("Select Operation", ("Add", "Subtract", "Multiply", "Divide", "Power", "Square Root", "Logarithm", "Sine", "Cosine", "Tangent"))

if operation in ("Add", "Subtract", "Multiply", "Divide", "Power"):
    num1 = st.number_input("Enter first number:", format="%.5f")
    num2 = st.number_input("Enter second number:", format="%.5f")

    if st.button("Calculate"):
        if operation == "Add":
            st.write("Result:", add(num1, num2))
        elif operation == "Subtract":
            st.write("Result:", subtract(num1, num2))
        elif operation == "Multiply":
            st.write("Result:", multiply(num1, num2))
        elif operation == "Divide":
            st.write("Result:", divide(num1, num2))
        elif operation == "Power":
            st.write("Result:", power(num1, num2))

elif operation == "Square Root":
    num = st.number_input("Enter number:", format="%.5f")
    if st.button("Calculate"):
        st.write("Result:", square_root(num))

elif operation == "Logarithm":
    num = st.number_input("Enter number:", format="%.5f")
    base = st.number_input("Enter logarithm base (default is 10):", value=10, format="%.5f")
    if st.button("Calculate"):
        st.write("Result:", logarithm(num, base))

elif operation == "Sine":
    num = st.number_input("Enter angle in degrees:", format="%.5f")
    if st.button("Calculate"):
        st.write("Result:", sine(num))

elif operation == "Cosine":
    num = st.number_input("Enter angle in degrees:", format="%.5f")
    if st.button("Calculate"):
        st.write("Result:", cosine(num))

elif operation == "Tangent":
    num = st.number_input("Enter angle in degrees:", format="%.5f")
    if st.button("Calculate"):
        st.write("Result:", tangent(num))