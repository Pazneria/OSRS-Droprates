import streamlit as st
import plotly.graph_objects as go
import math

st.title('OSRS Drop Calculator')

# Basic input for drop rate
drop_rate = st.number_input('Drop Rate (1/x)', value=1256, min_value=1)

# Calculate probabilities for first plot
kills = list(range(0, drop_rate * 3))
probabilities = [100 * (1 - math.pow(1 - 1/drop_rate, k)) for k in kills]

# Create basic plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=kills, y=probabilities, mode='lines', name='Probability'))
fig.update_layout(
    title='Drop Probability by Kill Count',
    xaxis_title='Kill Count',
    yaxis_title='Probability (%)'
)

st.plotly_chart(fig)