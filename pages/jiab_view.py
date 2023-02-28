# Draw a title and some text to the app:
'''
# This is the document title

This is some _markdown_.
'''
# Import necessary libraries
import json

import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
import numpy as np

# Custom classes 
# from utils import isNumerical
df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10
'x', x  # 👈 Draw the string 'x' and then the value of x

# Also works with most supported chart types

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

fig  # 👈 Draw a Matplotlib chart
def app():
    st.markdown("## Data jiab jiab")

    # Upload the dataset and save as csv
    st.markdown("### dddd") 
    st.write("\n")


