## **Developer Task List: Jigsaw & Bayesian Mastery System**

This task list is derived from PRD v1.0. The goal is to build the Minimum Viable Product (MVP) for the system using a Python backend and a standard HTML, CSS, and JavaScript frontend.

### **Tasks**

* \[ \] **1.0 Backend: Data Models & Core Logic (Python)**  
  * \[ \] 1.1 Using an ORM like SQLAlchemy, define the data models for: User, Course, Activity, LearningObjective, ExpertTopic, Quiz, Question, StudentSubmission, and MasteryScore.  
  * \[ \] 1.2 Implement the core Bayesian mastery calculation function in a Python module. This function should accept a student's prior mastery state (e.g., alpha/beta values) and new evidence (quiz results) to produce an updated mastery percentage.  
  * \[ \] 1.3 Create the basic API structure using a web framework like Flask or FastAPI. Implement placeholder routes and controller functions for the primary models (Activity, Quiz, User).  
* \[ \] **2.0 Frontend: Instructor Creation Workflow (HTML/JS/CSS)**  
  * \[ \] 2.1 Build the create-activity.html page, containing a form with fields for title, instructions, and resource links. Style it with styles.css.  
  * \[ \] 2.2 In create-activity.js, write the JavaScript logic to allow instructors to dynamically add, edit, and delete input fields for "Expert Topics" and their associated questions.  
  * \[ \] 2.3 Add functionality to the same JavaScript file for instructors to dynamically add, edit, and delete input fields for "Learning Objectives".  
  * \[ \] 2.4 Build the create-quiz.html page and its associated JavaScript file (create-quiz.js). It should allow an instructor to add multiple-choice question blocks.  
  * \[ \] 2.5 In create-quiz.js, ensure that when a new question is added, a dropdown menu is populated with the Learning Objectives defined for the associated activity.  
  * \[ \] 2.6 Implement the client-side fetch logic to send the completed Activity and Quiz data from the forms to the Python backend API endpoints.  
* \[ \] **3.0 Backend: Group & Session Management (Python)**  
  * \[ \] 3.1 Implement the business logic for fetching a class roster associated with a specific activity from the database.  
  * \[ \] 3.2 Create the assign\_expert\_groups function that takes a class roster and a list of expert topics, then assigns students into "expert groups".  
  * \[ \] 3.3 Create the assign\_jigsaw\_groups function that takes the output of the expert groups and re-distributes students into "jigsaw groups".  
  * \[ \] 3.4 Create an API endpoint (e.g., POST /api/activities/\<id\>/start) that calls the group assignment functions and saves the group structures to the database.  
* \[ \] **4.0 Frontend: Live Activity & Assessment Views (HTML/JS/CSS)**  
  * \[ \] 4.1 Develop the student-activity.html page. Use JavaScript to fetch and display the student's current group (expert or jigsaw), their assigned materials, and the names of their group members.  
  * \[ \] 4.2 Develop the student-quiz.html page. JavaScript will fetch the quiz questions and send the final answers to the backend.  
  * \[ \] 4.3 Create a simple instructor-monitoring.html page. Its associated JavaScript will fetch and display the generated expert and jigsaw groups for a live activity.  
* \[ \] **5.0 Frontend: Mastery Dashboards (HTML/JS/CSS)**  
  * \[ \] 5.1 On quiz submission, ensure the backend processes the submission, triggers the Bayesian calculation from step 1.2, and updates the MasteryScore model in the database.  
  * \[ \] 5.2 Build the student-dashboard.html page. Use JavaScript to fetch the logged-in student's mastery percentages and display them, perhaps using simple CSS bars for a progress-bar-like feel.  
  * \[ \] 5.3 Build the instructor-dashboard.html page. Use JavaScript to fetch the mastery data for all students and dynamically build an HTML table, with rows for students and columns for learning objectives.

### **Relevant Files (Potential)**

* **Backend (Python/Flask Example)**  
  * app.py: Main application file.  
  * models.py: Contains all SQLAlchemy model definitions.  
  * services/:  
    * bayesian\_calculator.py  
    * group\_allocator.py  
  * routes/:  
    * activity\_routes.py  
    * quiz\_routes.py  
    * user\_routes.py  
* **Frontend (HTML/JS/CSS)**  
  * html/:  
    * create-activity.html  
    * create-quiz.html  
    * student-activity.html  
    * student-quiz.html  
    * dashboard.html  
  * css/:  
    * styles.css  
  * js/:  
    * main.js (for shared logic)  
    * activity-builder.js  
    * quiz-taker.js  
    * dashboard-loader.js  
* **Tests (pytest Example)**  
  * tests/test\_bayesian\_calculator.py  
  * tests/test\_group\_allocator.py