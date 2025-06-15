# Insurance Risk Analytics Project

## Overview

This project aims to analyze insurance risk using data analytics techniques. The goal is to establish a reproducible and auditable data pipeline using Data Version Control (DVC) to ensure that data inputs are rigorously version-controlled, facilitating regulatory compliance and debugging in the finance and insurance sectors.

## Installation

To set up the project, ensure you have Python and pip installed. Then, run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

Install DVC:

```bash
pip install dvc
```

## Data Version Control

This project uses DVC to manage datasets and models. DVC allows for:

- Versioning datasets and models
- Reproducibility of analysis
- Efficient data management

## Methodology

This project follows a structured methodology to ensure rigorous analysis and insights. The process can be divided into the following main steps:

### 1. Data Cleaning and Preprocessing

- **Data Import**: Load the dataset into a pandas DataFrame.
  
- **Handling Missing Values**:
  - Identify missing values using methods like `isnull()` and `sum()`.
  - Decide on a strategy to handle them: 
    - Impute missing values (mean, median, mode).
    - Drop rows or columns with excessive missing values.

- **Data Type Conversion**:
  - Convert data types as necessary (e.g., converting date strings to datetime objects).
  - Ensure categorical variables are appropriately encoded.

- **Outlier Detection**:
  - Identify outliers using statistical methods (e.g., IQR, Z-score).
  - Decide on a method to handle outliers (e.g., capping, removal).

- **Feature Engineering**:
  - Create new features that may enhance model performance (e.g., extracting year from dates, creating interaction terms).

### 2. Exploratory Data Analysis (EDA)

- **Summary Statistics**:
  - Generate descriptive statistics using `describe()` to understand the dataset's central tendency and variability.

- **Data Distribution Analysis**:
  - Visualize the distribution of key numerical variables using histograms and density plots.

- **Correlation Analysis**:
  - Examine relationships between numerical variables using correlation matrices and heatmaps.

- **Categorical Analysis**:
  - Analyze categorical variables using count plots to understand the distribution of different categories.

### 3. Visualization

- **Key Visualizations Produced**:
  1. **Distribution Plot**: Visualizes the distribution of `TotalPremium` to understand its spread and skewness.
  2. **Box Plot**: Compares `TotalClaims` across different `CoverType`, highlighting central tendency and variability.
  3. **Pair Plot**: Explores relationships among multiple numerical variables to identify potential correlations.
  4. **Count Plot**: Displays the count of policies by `CoverType`, providing insights into the distribution of insurance products.

