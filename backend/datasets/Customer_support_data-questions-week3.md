# **Week 3 Assessment Questions: Data Preparation**

**Context:** These questions are based on the provided "Customer Support Ticket" dataset. They are designed to assess a student's individual contribution to their Home Group's project during the Data Preparation phase.

### **Category 1: Understanding Data Preparation Concepts**

*(Bloom's Level: Understand)*

1. What is the primary purpose of data preparation in the CRISP-DM cycle?  
2. Define "imputation" in the context of missing data.  
3. Explain the difference between an "outlier" and an "error" in a dataset like this.  
4. What is one-hot encoding? For which feature in this dataset would it be an appropriate technique?  
5. Why is feature scaling (e.g., normalization or standardization) important for certain machine learning algorithms?  
6. Look at the connected\_handling\_time feature. What is a potential data quality issue you might suspect or want to check for in this numerical column?  
7. The Customer Remarks field contains unstructured text. List two common text pre-processing steps that would be necessary before this feature could be used for modeling.

### **Category 2: Applying Data Preparation Techniques**

*(Bloom's Level: Apply)*

8. Assume some rows have a missing Item\_price. Describe a simple, logical method you would use to impute these missing values.  
9. The Tenure Bucket feature is categorical (e.g., "0-6 months"). Describe the steps you would take to convert this into a numerical format that a model can understand.  
10. Propose a new feature that could be engineered by combining Issue\_reported at and issue\_responded. What would you name this new feature?  
11. If you discovered a connected\_handling\_time of \-120 seconds, how would you handle this specific data point during data cleaning?  
12. (Multiple Choice) Which data preparation technique is most suitable for converting the channel\_name feature into a format usable by most machine learning models?  
    a) Binning  
    b) One-Hot Encoding  
    c) Log Transformation  
    d) Imputation  
13. Describe the steps to create a new binary feature called is\_weekend from the Issue\_reported at timestamp.  
14. Propose a method to identify and handle potential outliers in the Item\_price feature.  
15. The Agent Shift feature has values like 'Day' and 'Night'. How would you encode this feature so it can be used in a model?  
16. Formulate a plan to convert the Sub-category feature into numerical values.  
17. You want to create a new feature called response\_time\_in\_minutes. Write down the formula or pseudocode to calculate it using the existing timestamp columns.

### **Category 3: Evaluating & Justifying Choices**

*(Bloom's Level: Evaluate / Analyze)*

18. A colleague suggests simply deleting every row that contains any missing value. Argue for or against this strategy for this specific dataset.  
19. For the Tenure Bucket feature, evaluate the pros and cons of using Ordinal Encoding (e.g., 0, 1, 2\) versus One-Hot Encoding. Which would you choose and why?  
20. A teammate suggests creating a new feature by dividing Item\_price by connected\_handling\_time. Critique this idea. Is it likely to be a useful feature? Why or why not?  
21. Justify your choice: For handling missing values in the Item\_price column, why might imputing with the *median* be a better choice than imputing with the *mean*?  
22. If you were to one-hot encode the Customer\_City feature, what is a major potential problem you might introduce into your dataset?  
23. Your goal is to predict CSAT Score. Evaluate whether you should keep the Agent\_name feature in your model as-is. What is a better approach to using this information, and why?  
24. Justify why it is generally a bad practice to perform data preparation (like calculating the mean for imputation) on your entire dataset *before* splitting it into training and testing sets.  
25. After cleaning the data, you find that the channel\_name 'Phone' is associated with much lower CSAT Scores. Does this mean the phone channel is causing bad scores? Explain your reasoning.