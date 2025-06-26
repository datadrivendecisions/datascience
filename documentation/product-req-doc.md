# **Product Requirements Document: Jigsaw & Bayesian Mastery System**

**Version:** 1.0

**Status:** Draft

## **1\. Introduction**

This document outlines the requirements for a new educational tool that combines the **Jigsaw collaborative learning technique** with **Bayesian Mastery Assessment**.

* **Problem:** Instructors need a way to move beyond simple right/wrong grading and understand a student's true mastery of a topic. Furthermore, they need tools that encourage collaborative, process-oriented learning that is less vulnerable to AI misuse.  
* **Goal:** To create an integrated system that allows an instructor to easily set up, manage, and assess a Jigsaw activity. The system will use the results from a post-activity quiz to calculate and track each student's content mastery level using a Bayesian model, providing both instructors and students with clear, data-driven feedback.

## **2\. Goals**

* **GOAL-1:** Enable an instructor to create a complete Jigsaw learning activity, including all necessary resources, expert topics, and group tasks.  
* **GOAL-2:** Automate the administrative overhead of the Jigsaw method by handling the creation of "expert" and "jigsaw" groups.  
* **GOAL-3:** Assess student understanding through a post-activity quiz, using the results as evidence for the mastery calculation.  
* **GOAL-4:** Provide students and instructors with a simple, clear visualization of topic mastery (as a percentage) to guide further learning and intervention.

## **3\. User Stories**

### **Instructor Stories**

* **As an instructor, I want to** create a new Jigsaw activity by providing a central resource, a list of expert topics, and specific questions for each phase, **so that I can** structure a complete and effective collaborative learning session.  
* **As an instructor, I want to** define the specific learning objectives for an activity **so that I can** align the activity with my course curriculum and track student progress on key skills.  
* **As an instructor, I want the system to** automatically assign students to expert and jigsaw groups **so that I can** save time on manual administration and focus on teaching.  
* **As an instructor, I want to** create a quiz and link its questions to my learning objectives **so that I can** formally assess student understanding after the collaborative activity.  
* **As an instructor, I want to** view a dashboard showing the calculated mastery percentage for each student on each objective **so that I can** quickly identify students who may be struggling and need additional support.

### **Student Stories**

* **As a student, I want to** easily see which group (expert and jigsaw) I am in and access the specific materials and questions for my assigned expert topic **so that I can** participate effectively in the activity.  
* **As a student, I want to** take a quiz after completing the Jigsaw activity **so that I can** demonstrate my understanding of all the topics discussed.  
* **As a student, I want to** see my mastery score for a learning objective **so that I can** understand my own strengths and weaknesses.

## **4\. Functional Requirements**

### **FR-1: Activity Creation**

* The system must provide a form or wizard for an instructor to create a "Jigsaw Mastery Activity".  
* The creation form must allow the instructor to:  
  * 1.1: Provide a title and instructions for the activity.  
  * 1.2: Upload or link to a central resource (e.g., a PDF, a dataset, a URL) for initial student review.  
  * 1.3: Define a list of "expert topics".  
  * 1.4: Add specific questions/tasks for the "expert groups" to work on for each topic.  
  * 1.5: Add specific questions/tasks for the final "jigsaw groups" to work on.  
  * 1.6: Manually create one or more Learning Objectives for the activity (e.g., "Understands k-Nearest Neighbors," "Can interpret a confusion matrix").

### **FR-2: Group Management (MVP: Automation Only)**

* The system must automatically assign students from the course roster into "expert groups" of roughly equal size, with each group assigned to one expert topic.  
* The system must automatically re-assign students into new "jigsaw groups". Each jigsaw group must contain one member from each of the original expert groups.  
* The student interface must clearly display the student's current group (expert or jigsaw), their assigned topic (if in an expert group), and the names of their group members.

### **FR-3: Assessment & Evidence Collection**

* The system must allow an instructor to create a quiz associated with a Jigsaw activity.  
* The instructor must be able to link each quiz question to one of the Learning Objectives defined in FR-1.6.  
* The system will use the student's performance (correct/incorrect) on this quiz as the sole evidence for the Bayesian calculation.

### **FR-4: Mastery Calculation & Display**

* The system must calculate and store a mastery estimate for each student for each Learning Objective.  
* **Instructor Dashboard:** A dashboard must be available for the instructor to view a table of all students in the class. The table should show each student's name and their calculated mastery estimate as a percentage (e.g., 85%) for each Learning Objective associated with the activity.  
* **Student Dashboard:** A simple view must be available for students to see their own mastery percentage for each objective they have been assessed on.

## **5\. Non-Goals (Out of Scope for v1.0)**

* Using peer assessment, teacher evaluation, or student self-assessment as evidence for the mastery calculation.  
* Automatically suggesting learning objectives from uploaded materials.  
* Displaying the complex Bayesian probability distribution to students or instructors. Only the final percentage will be shown.  
* Allowing manual adjustments to groups by the instructor or students.  
* Providing AI-powered feedback on student work or group discussions.  
* Time-based release of different activity phases.

## **6\. Design Considerations**

* The UI for creating an activity should be clean and step-by-step to prevent overwhelming the instructor.  
* The student view must be extremely simple and clear, focusing only on their current task, group, and materials to avoid confusion.  
* Mastery scores should be displayed using simple progress bars or percentages for easy interpretation.

## **7\. Success Metrics**

* **Adoption:** The number of Jigsaw activities created and launched by instructors per semester.  
* **Engagement:** Percentage of students who complete the full activity loop (both group phases and the final quiz).  
* **Instructor Satisfaction:** Qualitative feedback from instructors on whether the tool saves them time and provides valuable insights into student understanding.

## **8\. Open Questions**

* What are the specific initial parameters for the Bayesian model (e.g., prior beliefs like alpha and beta)?  
* How should the system handle students who are absent for the activity and do not complete the quiz?