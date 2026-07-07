# PKCERT Summer Internship 2026

## Task 04 – NumPy & Pandas for Data Analysis

### Objective

The objective of this project is to demonstrate the use of the Pandas library for data manipulation and exploratory data analysis using a public Loan Prediction dataset.

---

## Dataset

**Dataset Name:** Loan Prediction Dataset

The dataset contains information about loan applicants, including:

- Age
- Gender
- Education
- Income
- Employment Experience
- Home Ownership
- Loan Amount
- Loan Intent
- Interest Rate
- Credit Score
- Loan Status

---

## Libraries Used

- Pandas
- Matplotlib

---

## Data Cleaning Process

The dataset was loaded using Pandas.

Missing values were checked using:

```python
df.isnull().sum()
```

No missing values were found in the dataset; therefore, no additional data cleaning was required.

---

## Analysis Performed

The following analysis was performed:

- Displayed the first five rows
- Checked dataset information
- Displayed dataset shape
- Listed column names
- Checked missing values
- Generated summary statistics
- Analyzed gender distribution
- Analyzed education distribution
- Analyzed home ownership
- Analyzed loan intent
- Analyzed loan status
- Calculated average age
- Calculated average income
- Calculated average loan amount
- Calculated average credit score
- Performed GroupBy operations
- Filtered records based on income and loan amount
- Sorted applicants by income
- Created visualizations using Matplotlib

---

## Key Findings

- The dataset contains 45,000 records.
- No missing values were present.
- Applicant information includes demographic and financial attributes.
- GroupBy operations helped summarize income, loan amount, and credit score.
- Data visualization made it easier to understand the distribution of applicants and loan status.

---

## Conclusion

This project demonstrates how Pandas can be used for reading datasets, exploring data, generating summary statistics, filtering records, grouping data, and creating basic visualizations. These techniques are important for data preprocessing and exploratory data analysis.