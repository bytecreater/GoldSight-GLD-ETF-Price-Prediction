# GoldSight: ML-Powered Gold Price Prediction

An end-to-end Machine Learning project that predicts GLD (Gold ETF) prices using financial market indicators. The model is built using Random Forest Regression and deployed through an interactive Streamlit web application.

## Project Overview

Gold prices are influenced by several financial and economic factors. This project leverages historical market data to predict the price of the SPDR Gold Shares ETF (GLD) using machine learning.

The application allows users to input market indicators and instantly receive a predicted GLD price through a user-friendly Streamlit interface.

## Features

- Data preprocessing and analysis
- Random Forest Regression model
- Interactive Streamlit web application
- Real-time GLD price prediction
- Clean and responsive user interface
- Model serialization using Joblib

## Dataset

This project uses the Gold Price Data dataset from Kaggle.

**Dataset Link:**
https://www.kaggle.com/datasets/altruistdelhite04/gold-price-data

**CSV File:**
https://www.kaggle.com/datasets/altruistdelhite04/gold-price-data?select=gld_price_data.csv

### Dataset Information

The dataset contains historical financial market indicators and Gold ETF prices.

| Feature | Description |
|----------|------------|
| Date | Trading Date |
| SPX | S&P 500 Index |
| USO | United States Oil Fund |
| SLV | Silver ETF |
| EUR/USD | Euro to US Dollar Exchange Rate |
| GLD | Gold ETF Price (Target Variable) |

The dataset contains approximately **2,290 records**.

### Target Variable

```python
X = gold_data.drop(['Date', 'GLD'], axis=1)
Y = gold_data['GLD']
```

The model predicts the **GLD ETF Price** using:

- SPX
- USO
- SLV
- EUR/USD

## Machine Learning Model

### Algorithm Used

- Random Forest Regressor

### Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Selection
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Model Serialization using Joblib
8. Streamlit Deployment

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Streamlit

## Project Structure

```text
GoldSight/
│
├── app.py
├── random_forest_regressor_model.sav
├── requirements.txt
├── README.md
├── Gold_Price_Prediction.ipynb
├── dataset/
│   └── gld_price_data.csv
│
└── images/
    └── app_screenshot.png
```

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/goldsight.git
cd goldsight
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit App

```bash
streamlit run app.py
```

## Application Usage

1. Enter values for:
   - SPX
   - USO
   - SLV
   - EUR/USD

2. Click the **Predict** button.

3. View the predicted GLD ETF price.

## Example Prediction

| Input Feature | Value |
|--------------|--------|
| SPX | 4000 |
| USO | 70 |
| SLV | 20 |
| EUR/USD | 1.10 |

### Output

```text
Predicted GLD Price: $185.42
```

## Application Preview

Add a screenshot of your Streamlit application inside the `images` folder and update the file name if necessary.

```markdown
![Application Screenshot](images/app_screenshot.png)
```

## Results

The Random Forest Regressor successfully captures relationships between market indicators and GLD prices, providing accurate predictions on unseen data.

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Future Improvements

- Hyperparameter tuning
- Comparison with other regression models
- XGBoost implementation
- Live market data integration using APIs
- Automated retraining pipeline
- Cloud deployment
- Time-series forecasting models

## Skills Demonstrated

- Machine Learning
- Regression Analysis
- Feature Engineering
- Data Preprocessing
- Model Evaluation
- Python Programming
- Streamlit Development
- Model Deployment

## Author

**Nihal Ahemad Khan**

B.Tech Computer Science & Engineering

## License

This project is licensed under the MIT License.

## Acknowledgements

- Kaggle Gold Price Dataset
- Scikit-Learn Documentation
- Streamlit Documentation