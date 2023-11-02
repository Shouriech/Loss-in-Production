import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the Streamlit app
st.title("Estimated Lost Production")
st.subheader("Raw Data")

# Read the CSV file from the same folder
data = pd.read_csv("project-4-data.csv")
st.write(data)
data_points = data['Units(1000s)'].tolist()

# Calculate control limits
n = len(data_points)
mu = np.mean(data_points)
sigma = np.std(data_points, ddof=1)
upper_action_limit = mu + 3 * (sigma / np.sqrt(n))
lower_action_limit = mu - 3 * (sigma / np.sqrt(n))
upper_warning_limit = mu + 2 * (sigma / np.sqrt(n))
lower_warning_limit = mu - 2 * (sigma / np.sqrt(n))

# Create a control chart
fig, ax = plt.subplots()
x = np.arange(1, n + 1)
ax.plot(x, data_points, marker='o', label='Data Points', color='blue')
ax.axhline(upper_action_limit, linestyle='--', label='UCL (3σ)', color='red')
ax.axhline(lower_action_limit, linestyle='--', label='LCL (3σ)', color='red')
ax.axhline(upper_warning_limit, linestyle='--', label='UWL (2σ)', color='orange')
ax.axhline(lower_warning_limit, linestyle='--', label='LWL (2σ)', color='orange')
ax.set_xlabel('Weeks')
ax.set_ylabel('Units (1000s)')
ax.set_title('Control Chart')
ax.legend()

# Display the chart in Streamlit
st.pyplot(fig)
