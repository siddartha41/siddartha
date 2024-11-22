import streamlit as st

# Define Gen_Eff function to calculate Efficiency and Core-Used Losses
def Gen_Eff(V, CL, IL, K, Rsh, Ra):
    # Calculate Shunt field current (Ish)
    Ish = V / Rsh
    
    # Calculate Armature current (Ia)
    Ia = K * IL - Ish
    
    # Calculate Core-Used Losses (CUL)
    CUL = Ish*2 * Rsh + Ia*2 * Ra
    
    # Calculate Efficiency (Eff)
    Eff = ((K * V * IL - CL - CUL) / (K * V * IL)) * 100
    
    return Eff, CUL

# Streamlit UI
st.title("02341A0259-PS12")  # Title with Roll No. and Problem Statement No.

# Input fields for the user to enter values
V = st.number_input("Enter Voltage (V)", min_value=0.0, step=0.1)
CL = st.number_input("Enter Core Losses (CL in Watts)", min_value=0.0, step=0.1)
IL = st.number_input("Enter Full Load Current (IL in Amps)", min_value=0.0, step=0.1)
K = st.number_input("Enter Loading on Generator (K)", min_value=0.0, step=0.1)
Rsh = st.number_input("Enter Shunt Field Resistance (Rsh in Ohms)", min_value=0.0, step=0.1)
Ra = st.number_input("Enter Armature Resistance (Ra in Ohms)", min_value=0.0, step=0.1)

# Button to calculate efficiency when clicked
if st.button("Calculate Efficiency"):
    # Ensure all input values are greater than zero
    if V > 0 and CL >= 0 and IL > 0 and K > 0 and Rsh > 0 and Ra > 0:
        Eff, CUL = Gen_Eff(V, CL, IL, K, Rsh, Ra)
        st.write(f"Efficiency: {Eff:.2f}%")
        st.write(f"Core-Used Losses (CUL): {CUL:.2f} W")
    else:
        st.error("Please enter valid values for all inputs.")