import streamlit as st
import pandas as pd
import joblib

model = joblib.load("random_forest_regressor_model.sav")

st.set_page_config(page_title="GoldSight : GLD ETF Price Predictor", page_icon="🥇")

st.title("🥇 Gold Price Predictor")

col1, col2 = st.columns(2)

with col1:
    spx = st.number_input("SPX", value=4000.0)
    uso = st.number_input("USO", value=70.0)

with col2:
    slv = st.number_input("SLV", value=20.0)
    eur_usd = st.number_input("EUR/USD", value=1.10)

if st.button("Predict", use_container_width=True):

    df = pd.DataFrame(
        [[spx, uso, slv, eur_usd]],
        columns=["SPX", "USO", "SLV", "EUR/USD"]
    )

    prediction = model.predict(df)[0]

    st.metric(
        label="Predicted Gold Price",
        value=f"${prediction:.2f}"
    )