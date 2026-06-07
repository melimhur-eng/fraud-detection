# Fraud Detection for E-Commerce and Bank Transactions

## Overview

This project aims to detect fraudulent transactions in both e-commerce and banking environments using machine learning techniques. The work includes data preprocessing, exploratory data analysis (EDA), feature engineering, class imbalance handling, model training, and explainability.

## Project Structure

```text
fraud-detection/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── eda-fraud-data.ipynb
│   ├── eda-creditcard.ipynb
│   ├── feature-engineering.ipynb
│   ├── data-transformation-imbalance.ipynb
│   └── geolocation-integration.ipynb

├── src/
├── models/
├── tests/
├── requirements.txt
└── README.md
```

## Datasets

* **Fraud_Data.csv** – E-commerce transaction data
* **IpAddress_to_Country.csv** – IP-to-country mapping data
* **creditcard.csv** – Credit card transaction data

## Key Tasks

### Task 1: Data Analysis & Preprocessing

* Data cleaning
* EDA
* Geolocation integration
* Feature engineering
* Data transformation
* Class imbalance handling


## Installation

Clone the repository:

```bash
create repository
cd fraud-detection
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Project

Execute notebooks in the following order:

1. eda-fraud-data.ipynb
2. eda-creditcard.ipynb
3. feature-engineering.ipynb
4. modeling.ipynb
5. shap-explainability.ipynb

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Imbalanced-learn
* Matplotlib
* Seaborn
* SHAP





