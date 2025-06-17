# Insurance Risk Analytics Project

## Overview

This project analyzes insurance risk using data science techniques and builds the foundation for a dynamic, risk-based pricing system. The pipeline is developed using **Data Version Control (DVC)** to ensure that data inputs and model outputs are version-controlled, enhancing reproducibility, auditability, and regulatory compliance in the financial and insurance sectors.

## Installation

Ensure Python and pip are installed. Then, install the required dependencies:

```bash
pip install -r requirements.txt
````

Install DVC:

```bash
pip install dvc
```

## Data Version Control

DVC is used to:

* Track datasets and models under version control
* Ensure reproducibility of analysis across teams
* Manage storage of large files and model artifacts


## Methodology

This project follows a four-task methodology that progressively builds from data cleaning to advanced modeling and pricing.

### 1. Data Cleaning and Preprocessing

* **Import**: Loaded the raw data into a pandas DataFrame.
* **Missing Values**: Identified and handled missing values through imputation or removal.
* **Data Type Conversion**: Converted relevant features to appropriate types (e.g., datetime, categorical).
* **Outliers**: Detected using IQR/z-scores; capped or removed where necessary.
* **Feature Engineering**: Derived meaningful features such as `ClaimFrequency`, `ClaimSeverity`, and `Margin`.

### 2. Exploratory Data Analysis (EDA)

* **Summary Stats**: Used `.describe()` to understand central tendencies and variance.
* **Univariate & Bivariate Analysis**:

  * Plots of `TotalPremium`, `TotalClaims`, etc.
  * Boxplots and histograms for visual patterns.
* **Correlation Matrix**: Analyzed linear correlations between numeric variables.
* **Distribution by Categories**: Count plots and bar charts by `Province`, `Gender`, `CoverType`, etc.

### 3. Hypothesis Testing (Risk Segmentation Strategy)

To inform a new segmentation strategy, statistical hypothesis testing was conducted:

* **Key Metrics**:

  * **Claim Frequency** = (Number of policies with ≥1 claim) / (Total policies)
  * **Claim Severity** = (TotalClaims) / (Number of claims)
  * **Margin** = TotalPremium - TotalClaims

* **Tests Conducted**:

  * **Chi-squared Test**: Tested risk differences across `Province` and `PostalCode`.
  * **T-tests**: Compared claim severity and margin between:

    * `Province` groups
    * `Zip Codes`
    * `Gender` (Women vs. Men)

* **Significant Findings**:

  * Risk **varied significantly across provinces** (p < 0.001).
  * No significant **gender-based differences** were found.
  * **Zip codes** showed some differences in margins, suggesting possible pricing inefficiencies.

### 4. Predictive Modeling (Dynamic Pricing System)

#### Claim Severity Prediction (Regression Task)

* **Objective**: Predict `TotalClaims` for policies with at least one claim.

* **Models**:

  * Linear Regression
  * Random Forest Regressor
  
* **Evaluation Metrics**:

  * **Root Mean Squared Error (RMSE)**
  * **R² Score**

* **Best Performer**: Random Forest

  * Captured non-linear relationships better than Linear Regression
  * Feature importance revealed key drivers: `SumInsured`, `CalculatedPremiumPerTerm`, `VehicleType`, and `Province`

#### Premium Optimization Framework *(Advanced Task In Progress)*

* **Concept**:
  `Premium = (Predicted Claim Probability × Predicted Claim Severity) + Expenses + Margin`
* Lays groundwork for deploying a **risk-based premium calculator**.


## Visualizations

* Distribution of `TotalPremium` and `TotalClaims`
* Boxplots comparing claims by `CoverType` and `Province`
* Pairplots for multivariate exploration
* Count plots for categorical distributions
* Feature importance plot from Random Forest model

## Final Remarks

This project built an end-to-end, reproducible insurance risk analytics workflow. It combined:

* Rigorous data cleaning and EDA
* Hypothesis-driven insights for segmentation
* Predictive modeling for claim severity
* A framework for risk-adjusted premium pricing
