# GoldSight: ML-Powered Gold Price Prediction

An end-to-end Machine Learning project that predicts GLD (Gold ETF) prices using financial market indicators. The model is trained using Random Forest Regression and deployed through an interactive Streamlit web application.

## Overview

This project uses historical financial data to predict the price of GLD based on the following market indicators:

- SPX (S&P 500 Index)
- USO (United States Oil Fund)
- SLV (Silver ETF)
- EUR/USD Exchange Rate

The trained Random Forest Regression model is integrated into a Streamlit application, allowing users to enter market values and receive instant predictions.

## Features

- Data preprocessing and feature selection
- Random Forest Regression model
- Interactive Streamlit web interface
- Real-time GLD price prediction
- Clean and user-friendly dashboard

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit

## Dataset

The dataset contains historical market data with the following features:

| Feature | Description |
|----------|------------|
| SPX | S&P 500 Index |
| USO | United States Oil Fund |
| SLV | Silver ETF |
| EUR/USD | Euro to US Dollar Exchange Rate |
| GLD | Target Variable (Gold ETF Price) |

Target Variable:

```python
X = gold_data.drop(['Date', 'GLD'], axis=1)
Y = gold_data['GLD']