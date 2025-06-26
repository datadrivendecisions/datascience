# **Baserow Database Schema**

This document outlines the schema for each table required by the Jigsaw & Bayesian Mastery application. Use this as a guide to create the fields in your Baserow database.

### **1\.** users **Table**

Stores information about both students and instructors.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| username | Text | The unique name of the user. |
| email | Email | The user's unique email address. |
| role | Single Select | The user's role. Options: student, instructor. |
| created\_at | Date | *Optional:* The date the user was created. |

### **2\.** courses **Table**

Represents a single course or classroom.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| name | Text | The name of the course (e.g., "Data Mining Fall 2025"). |
| instructor | Link to Table | Links to the users table. **Should be limited to one user.** |
| activities | Link to Table | Links to all activities within this course. (This is the other side of the link from the activities table). |

### **3\.** activities **Table**

The central table for a Jigsaw activity.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| title | Text | The title of the Jigsaw activity. |
| instructions | Long Text | Detailed instructions for the students. |
| central\_resource\_url | URL | *Optional:* A link to a central document or resource. |
| course | Link to Table | Links to the courses table. **Should be limited to one course.** |

### **4\.** learning\_objectives **Table**

Stores the specific skills being tracked for an activity.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| description | Text | The description of the objective (e.g., "Understands K-Means Clustering"). |
| activity | Link to Table | Links back to the activities table. **Should be limited to one activity.** |

### **5\.** expert\_topics **Table**

Stores the topics for the "expert group" phase.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| title | Text | The title of the expert topic. |
| questions | Long Text | Specific questions or tasks for the expert group to work on. |
| activity | Link to Table | Links back to the activities table. |

### **6\.** quizzes **Table**

Represents the quiz associated with an activity.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| title | Text | The title of the quiz. |
| activity | Link to Table | Links back to the activities table. **Should be limited to one activity.** |

### **7\.** questions **Table**

Stores each individual question for a quiz.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| text | Long Text | The full text of the question. |
| options | Long Text | A JSON string of the multiple-choice options, e.g., \["Option A", "Option B", "Option C"\]. |
| correct\_option\_index | Number | The index (0-based) of the correct answer in the options array. |
| quiz | Link to Table | Links back to the quizzes table. **Should be limited to one quiz.** |
| learning\_objective | Link to Table | Links to the learning\_objectives table. **Should be limited to one objective.** |

### **8\.** submissions **Table**

Records a student's answer to a single question.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| student | Link to Table | Links to the users table (the student who answered). **Limit to one.** |
| question | Link to Table | Links to the questions table. **Limit to one.** |
| is\_correct | Boolean | A checkbox indicating if the answer was correct. |
| submitted\_at | Date | *Optional:* The timestamp of the submission. |

### **9\.** mastery\_scores **Table**

The core table for tracking Bayesian mastery.

| Field Name | Field Type | Description |
| :---- | :---- | :---- |
| student | Link to Table | Links to the users table. **Limit to one.** |
| learning\_objective | Link to Table | Links to the learning\_objectives table. **Limit to one.** |
| alpha | Number | The alpha parameter of the Beta distribution. (Set Decimal places \> 1). |
| beta | Number | The beta parameter of the Beta distribution. (Set Decimal places \> 1). |
| mastery\_estimate | Formula | A formula to calculate the mastery: field('alpha') / (field('alpha') \+ field('beta')). **Set format to Percent.** |

