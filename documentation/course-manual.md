# **Data Mining: A Collaborative & Applied Approach**

### **Course Philosophy**

This course is designed around a "Vibrant Learning Ecosystem" model. It leverages the **Jigsaw** collaborative learning protocol structured around the core phases of the **CRISP-DM data mining cycle**. Each student "Home Group" works on a **unique, course-long project**, fostering genuine application of learned skills. Student assessment is continuous and based on a weekly **Bayesian Mastery** model for each topic, measuring understanding as a probability. The primary goal is to develop practical, applied data mining skills, with an emphasis on process, collaboration, and critical thinking.

## **1\. Learning Outcomes & Bloom's Taxonomy**

The course outcomes are defined using the Revised Bloom's Taxonomy, focusing on both the Cognitive Process and Knowledge Dimensions. **To pass the course, students must demonstrate mastery at the "Apply / Procedural" level or higher for all four core CRISP-DM phases.**

| CRISP-DM Phase | Cognitive Process | Knowledge Dimension | Learning Outcome (Students will be able to...) |
| :---- | :---- | :---- | :---- |
| **Business Understanding** | Understand | Conceptual | Explain how a business problem translates into a data mining objective. |
|  | **Apply** | **Procedural** | **(Passing Level)** Formulate a data mining goal and success criteria for a given business case. |
|  | Analyze | Metacognitive | Deconstruct a business case to identify key stakeholders and potential project constraints. |
| **Data Understanding** | Understand | Factual | Describe different data types and summary statistics. |
|  | **Apply** | **Procedural** | **(Passing Level)** Perform initial data exploration using code to generate descriptive statistics and visualizations. |
|  | Analyze | Conceptual | Differentiate between relevant and irrelevant data for a given project objective. |
| **Data Preparation** | Understand | Conceptual | Explain the purpose of data cleaning, feature selection, and transformation. |
|  | **Apply** | **Procedural** | **(Passing Level)** Execute data cleaning and feature engineering tasks on a provided dataset using code. |
|  | Evaluate | Metacognitive | Justify the choices made during the data preparation phase for a specific dataset. |
| **Modeling** | Understand | Conceptual | Explain the fundamental principles of a selected modeling technique (e.g., classification, clustering). |
|  | **Apply** | **Procedural** | **(Passing Level)** Implement a data mining model and generate predictions or patterns using a programming library. |
|  | Evaluate | Procedural | Assess the performance of a model using appropriate metrics (e.g., confusion matrix, accuracy). |
| **Deployment (Final Assessment)** | Create | Procedural | Integrate all CRISP-DM phases to build and present a cohesive data mining project from a new dataset. |

## **2\. Six-Week Programme Schedule (6 hours/week total)**

**Course Structure:** Students are pre-assigned to "Home Groups" of 5\. These groups remain consistent throughout the course. Each week includes 3 hours of in-class sessions and an expected 3 hours of out-of-class work.

| Week | Session Focus & Expert Group Task | In-Class Activities (3 hours) | Out-of-Class Work (3 hours) |
| :---- | :---- | :---- | :---- |
| **1** | **Business Understanding** *(Expert Group 1\)* | **Hour 1:** Course Intro. Instructor distributes a **unique business case and dataset to each Home Group.** **Hour 2:** Expert Group 1 meets with the instructor to plan their general-purpose guide on Business Understanding. **Hour 3:** Home Groups do an initial analysis of their *own* assigned case. | **Expert Group 1:** Using AI for assistance, create a **general-purpose 2-page guide** and a **5-question quiz**. **Home Groups:** Begin work on the Business Understanding phase of their unique project. |
| **2** | **Data Understanding** *(Expert Group 2\)* | **Hour 1:** Expert Group 1 teaches "Business Understanding." All students take Expert Group 1's quiz. **Hour 2:** Expert Group 2 meets with instructor. **Hour 3:** Home Groups apply Business Understanding to their project. **Instructor assesses individual contributions.** | **Expert Group 2:** Create a **general-purpose tutorial notebook** and a **5-question quiz** on Data Understanding. **Home Groups:** Finalize Business Understanding section of their project. |
| **3** | **Data Preparation** *(Expert Group 3\)* | **Hour 1:** Expert Group 2 teaches "Data Understanding." All students take Expert Group 2's quiz. **Hour 2:** Expert Group 3 meets with instructor. **Hour 3:** Home Groups work on Data Understanding for their project. **Instructor assesses individual contributions.** | **Expert Group 3:** Create a **general 'best practices' checklist** and a **5-question quiz** on Data Preparation. **Home Groups:** Complete the Data Understanding phase. |
| **4** | **Modeling** *(Expert Group 4\)* | **Hour 1:** Expert Group 3 teaches "Data Preparation." All students take Expert Group 3's quiz. **Hour 2:** Expert Group 4 meets with instructor. **Hour 3:** Home Groups work on Data Preparation for their project. **Instructor assesses individual contributions.** | **Expert Group 4:** Create a **general-purpose code template** and a **5-question quiz** on Modeling. **Home Groups:** Complete the Data Preparation phase. |
| **5** | **Project Workshop & Peer Feedback** *(No new Expert Group)* | **Hour 1:** Expert Group 4 teaches "Modeling." All students take Expert Group 4's quiz. **Hour 2:** **Project Workshop** and status updates. **Instructor assesses individual contributions** to the Modeling application. **Hour 3:** **Structured Peer Feedback** session. | **Home Groups:** Refine final project based on feedback. Finalize their analysis and model and begin preparing their video presentation. |
| **6** | **Deployment as Assessment** *(No new Expert Group)* | **Hours 1-3:** **Course Wrap-Up & Retrospective.** Final Q\&A and review of key course takeaways. | **Home Groups:** Record a 15-minute video presentation. **Submit a final package to HANDIN** containing the video and all supporting materials. |

## **3\. Student Manual & Instructor Manual**

*(These should be updated to reflect the new assessment model below for clarity and transparency.)*

## **4\. Assessment Framework & Scoring**

The final grade is derived from two core Bayesian scores, calculated progressively throughout the course. This model measures your knowledge of each topic, your ability to apply it, and your effectiveness in teaching it.

**Final Grade \= 60% (Average of 4 Individual Mastery Scores) \+ 40% (Teaching Effectiveness Score)**

### **Component 1: Individual Mastery Score (Calculated Weekly for Each of 4 Topics)**

*This score measures your personal, applied understanding of each specific course topic. It is based solely on your own work and assessments.*

* **How it works (for a single topic, e.g., "Data Understanding"):**  
  * **A) The Prior (Your Quiz Performance):** Your individual score on the 5-question peer-created quiz for that topic establishes your baseline belief.  
  * **B) The Evidence (Your Individual Instructor Assessment):** The instructor uses the detailed weekly rubric to score your personal contribution to your group's project that week. This score becomes the evidence to update your baseline.  
  * **C) The Posterior (Final Topic Score):** The evidence from the instructor's assessment updates your quiz prior, producing a final, more accurate mastery score *for that specific topic*.  
* **Example Calculation (for one student on one topic):**  
  * You get **4/5** on the "Data Understanding" quiz. **Prior: alpha=4, beta=1**.  
  * The instructor assesses your individual contribution to the "Data Understanding" part of your project and gives you a score of **2/5**. **Evidence: successes \= 2**, failures \= 3\.  
  * **Posterior alpha \= 4 (prior) \+ 2 (evidence) \= 6**  
  * **Posterior beta \= 1 (prior) \+ 3 (evidence) \= 4**  
  * **Final Mastery Score for this topic \= 6 / (6 \+ 4\) \= 60.0%**  
  * *This process is repeated for all four topics. Your final grade component is the average of these four scores.*  
* **Passing Threshold:** A student's final calculated mastery score for **each of the four topics** must be **≥ 65%**.

### **Component 2: Teaching Effectiveness Score (Calculated Once per Student)**

*This score measures how effectively you, as an expert, enabled your Home Group peers to learn a topic. It is based entirely on your group's average performance.*

* **How it works:**  
  * **A) The Prior (Peer Performance on Your Quiz):** The initial belief is based on your 4 Home Group peers' combined performance on the 5-question quiz *you created*.  
  * **B) The Evidence (Peer Performance on Instructor Assessment):** The evidence is your Home Group's average score on the weekly instructor assessments for the topic you taught.  
  * **C) The Posterior (Final Score):** The group's average assessed application score updates their average quiz performance, producing your final Teaching Effectiveness score.  
* **Example Calculation:**  
  * An expert's peers collectively answer **15/20** questions correctly on the quiz they made. **Prior: alpha=15, beta=5**.  
  * The same Home Group members later earn an average score of **4/5** on the instructor's individual assessments for that topic. **Evidence: successes \= 4**, failures \= 1\.  
  * **Posterior alpha \= 15 (prior) \+ 4 (evidence) \= 19**  
  * **Posterior beta \= 5 (prior) \+ 1 (evidence) \= 6**  
  * **Final Teaching Effectiveness Score \= 19 / (19 \+ 6\) \= 76.0%**

## **5\. Detailed Weekly Assessment Rubrics**

The instructor uses the following rubrics to assess individual contributions each week. This score provides the "evidence" for the Bayesian calculations.

### **Week 2: Assessing Business Understanding**

*This assessment evaluates how well students translate their assigned business case into a structured data mining plan.*

* **Topics:** Data mining goals, success criteria, project planning, stakeholder needs.  
* **Bloom's Levels:** Understand (the business problem), Apply (formulating goals), Analyze (deconstructing constraints).

| Criteria | Level 0 (Insufficient) | Level 1 (Sufficient) | Level 2 (Excellent) | Score |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Problem Framing** | Student's contributions show a misunderstanding of the core business problem. | Student accurately identifies the business problem and participates in framing the data mining goal. | Student provides key insights that help the group frame a sharp, specific, and measurable data mining goal. | / 2 |
| **2\. Success Criteria Definition** | Student does not contribute to defining success criteria, or the suggestions are not measurable. | Student contributes to defining clear and measurable technical and business success criteria. | Student proposes nuanced success criteria that directly link technical outputs to business value. | / 3 |
| **Total** |  |  |  | **/ 5** |

### **Week 3: Assessing Data Understanding**

*This assessment evaluates the student's ability to explore a dataset and extract initial insights.*

* **Topics:** Exploratory Data Analysis (EDA), summary statistics, data quality checks, initial visualization.  
* **Bloom's Levels:** Apply (performing EDA), Analyze (differentiating relevant from irrelevant data).

| Criteria | Level 0 (Insufficient) | Level 1 (Sufficient) | Level 2 (Excellent) | Score |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Technical Execution** | Student struggles to generate basic statistics or visualizations, or their code is non-functional. | Student correctly executes code to generate descriptive statistics and relevant initial plots. | Student writes clean, efficient code and explores multiple visualization types to investigate the data. | / 2 |
| **2\. Insight Generation** | Student simply presents data/plots without interpretation. | Student correctly interprets the summary statistics and visualizations to describe the data. | Student analyzes the initial findings to form hypotheses or identify specific data quality issues to address next. | / 3 |
| **Total** |  |  |  | **/ 5** |

### **Week 4: Assessing Data Preparation**

*This assessment evaluates the student's contribution to cleaning data and preparing it for modeling.*

* **Topics:** Handling missing data, outlier treatment, data transformation, feature engineering.  
* **Bloom's Levels:** Apply (executing cleaning tasks), Evaluate (justifying choices).

| Criteria | Level 0 (Insufficient) | Level 1 (Sufficient) | Level 2 (Excellent) | Score |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Technique Application** | Student's contributions to data cleaning are incorrect or inappropriate for the data type. | Student correctly applies standard data preparation techniques (e.g., imputation, scaling) to the project dataset. | Student proposes and correctly implements multiple or advanced techniques appropriate for the group's specific data challenges. | / 2 |
| **2\. Justification of Process** | Student cannot explain why certain data preparation steps were taken. | Student can clearly justify the choices the group made for handling missing data and creating features. | Student provides a strong, data-driven argument for their preparation strategy, considering the potential impact on the future model. | / 3 |
| **Total** |  |  |  | **/ 5** |

### **Week 5: Assessing Modeling**

*This assessment evaluates the student's contribution to building and evaluating a predictive model.*

* **Topics:** Algorithm implementation, model training, parameter tuning, performance metrics.  
* **Bloom's Levels:** Apply (implementing a model), Evaluate (assessing performance).

| Criteria | Level 0 (Insufficient) | Level 1 (Sufficient) | Level 2 (Excellent) | Score |
| :---- | :---- | :---- | :---- | :---- |
| **1\. Model Implementation** | Student's contributions to the model code are incorrect or do not run. | Student correctly implements the modeling algorithm and trains it on the prepared data. | Student contributes to refining the model, for example, by implementing proper cross-validation or initial hyperparameter tuning. | / 2 |
| **2\. Performance Evaluation** | Student does not assess the model's performance or uses an inappropriate metric. | Student calculates and correctly interprets standard performance metrics (e.g., accuracy, confusion matrix). | Student analyzes the model's performance in the context of the business success criteria and identifies specific areas of weakness (e.g., high false positives). | / 3 |
| **Total** |  |  |  | **/ 5** |

