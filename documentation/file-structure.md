/jigsaw-mastery-app/
│
├── 📁 backend/
│   │
│   ├── 📁 app/
│   │   │
│   │   ├── __init__.py         # Initializes the Flask app, makes 'app' a package
│   │   │
│   │   ├── routes.py           # Defines all API endpoints (e.g., /api/activities)
│   │   │
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── bayesian_calculator.py  # Core mastery calculation logic
│   │       └── group_allocator.py      # Logic for assigning groups
│   │
│   ├── app.py                  # The main script to start the Flask server
│   └── requirements.txt        # Lists Python dependencies (Flask, requests, etc.)
│
├── 📁 frontend/
│   │
│   ├── 📄 ructor-workflow.htinstml # The main creation page
│   ├── 📄 student-activity.html    # View for a student during an activity
│   ├── 📄 student-dashboard.html   # Student's view of their mastery
│   ├── 📄 instructor-dashboard.html # Instructor's view of class mastery
│   │
│   ├── 📁 assets/
│   │   ├── 📁 css/
│   │   │   └── styles.css        # Main stylesheet
│   │   │
│   │   └── 📁 js/
│   │       ├── main.js             # Shared JS functions
│   │       ├── activity-builder.js # JS for instructor-workflow.html
│   │       └── dashboard-loader.js # JS for the dashboard pages
│
├── 📁 tests/
│   │
│   ├── test_bayesian_calculator.py # Unit tests for the calculation logic
│   └── test_group_allocator.py     # Unit tests for the group assignment logic
│
└── 📄 README.md                 # Project overview, setup, and run instructions