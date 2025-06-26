# **Week 2 Assessment Questions: Business Understanding**

**Context:** These questions are based on the provided "Customer Support Ticket" dataset. They are designed to assess a student's individual contribution to their Home Group's project during the Business Understanding phase.

### **Category 1: Understanding the Business Context & Data**

*(Bloom's Level: Understand)*

1. What is the primary business problem that this dataset is designed to address?  
2. Identify the target variable in this dataset. What type of variable is it (e.g., categorical, continuous, ordinal)?  
3. Based on the target variable, what kind of data mining task would be most appropriate for this problem (e.g., classification, regression, clustering, association)? Explain your choice in one sentence.  
4. List three features from the dataset that you believe would be most influential in predicting the CSAT Score.  
5. What is the difference between the category and Sub-category fields, and why is this distinction useful for a data analyst?  
6. Explain the purpose of the Tenure Bucket feature. What might you learn from it?  
7. Which two timestamp features could be combined to calculate the "Initial Response Time" for a support ticket?

### **Category 2: Applying Data Mining Concepts**

*(Bloom's Level: Apply)*

8. Formulate a clear and specific data mining goal for this project. (e.g., "The goal is to build a model that predicts...")  
9. Define one **business success criterion** for this project. How would the company measure if the project was a real-world success?  
10. Define one **technical success criterion** for this project. What specific metric would you use to evaluate your model?  
11. A manager wants to use this data to "improve customer satisfaction." Translate this vague request into a concrete, actionable data mining task.  
12. (Multiple Choice) Which of the following is the best example of a project objective?  
    a) To analyze the Customer Remarks.  
    b) To build a model that classifies CSAT Score into 'Satisfied' (4-5) and 'Not Satisfied' (1-3) categories with at least 80% accuracy.  
    c) To find out which Agent\_name has the lowest connected\_handling\_time.  
    d) To visualize the number of tickets per Product\_category.  
13. If you were to build a model, what would be the cost of a "False Negative" in this business context? (Assuming 'Negative' means a low CSAT score).  
14. Describe how you would use the Agent\_name, Supervisor, and Manager fields to create a project plan for analyzing performance at different organizational levels.  
15. You are asked to present your initial project plan. What are the three key items you must include in your presentation to management?  
16. The Customer Remarks field contains raw text. Propose a method to convert this unstructured data into a structured feature that could be used in a model.  
17. Formulate a hypothesis about the relationship between Item\_price and CSAT Score.

### **Category 3: Analyzing the Problem & Constraints**

*(Bloom's Level: Analyze / Evaluate)*

18. Identify the three main stakeholders for this data mining project within the company. For each stakeholder, what is their primary interest or concern?  
19. What is a potential ethical issue or bias that could arise from using Agent\_name as a feature in the model?  
20. What is a potential ethical issue or bias that could arise from using Customer\_City as a feature?  
21. Your project plan has a timeline of two weeks. What is the biggest risk or constraint you face in delivering a successful model within this timeframe, based on the provided data features?  
22. Deconstruct the problem: If your model predicts that a customer is likely to give a low CSAT score, what are two different business actions the company could take based on this prediction?  
23. The connected\_handling\_time could be misleading. Describe a scenario where a very *long* handling time could actually lead to a *high* CSAT score.  
24. Evaluate the usefulness of the Order\_id column. Why is it likely not useful for direct modeling, but potentially useful for another purpose?  
25. Propose a new feature that is not in this dataset but could be highly valuable for predicting CSAT Score. Explain why you believe it would be impactful.