import streamlit as st
import pandas as pd 
import numpy as np
import numpy_financial as npf
import time
import locale

df = pd.DataFrame({
    'Column One': [1,2,3,4],
    'Column Two': ['Ten','Twenty','Thirty','Fourty']
})

st.write(df) # Chooses what's best way to render the object, in this case chooses dataframe style

st.header("Highlighted Dataframe:")
colored_df = pd.DataFrame(
    np.random.randn(10,20),
    columns=('Col %d' % i for i in range(20))
)

st.write(colored_df.style.highlight_max(axis=0))


#st.header("Map data")
#st.map(latitude="39.51", longitude="-76.64")

st.header("Progress bar")
latest_iter = st.empty()
bar = st.progress(0)
for i in range(10):
    bar.progress(i+1)
    time.sleep(0.5)
st.write('Finished')

st.header("Financial Value Calculation")
rate = st.slider(label="Annual Interest Rate", min_value=0, max_value=30, step=1)
duration  = st.slider(label="Invested Duration in Years", min_value=0, max_value=30, step=2)
initial_amt = st.slider(label="Initial Investment", min_value=10000, max_value=500000, step=10000)
monthly_deposit  = st.slider(label="Monthly Deposit", min_value=0, max_value=20000, step=1000)
future_val = npf.fv(rate/1200, duration*12, -(monthly_deposit), -(initial_amt))
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
st.write(locale.currency(future_val))


# Sidebar example
# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)