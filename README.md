# Time-Tracking APP

## Objective
The objective of this project is to allow a team to track their time efficiently with minimal clicks and a user-friendly interface.

## Features
- Users can sign up and log in.
- Users can add a time entry with the number of hours, task description, and project. Projects are pre-filled from a static list. The current date and time are automatically recorded.
- Users can view their work for the week and totals for each project.

## Project Progress

### Journal
- **02/21/2024**: Spent 3 hours developing the backend.
- **02/22/2024**: Spent 4 hours finalizing the backend, integrating, and initializing the frontend. Also spent 1 hour on testing and documentation.

### Frontend Accomplishments
- Successfully integrated the backend with the frontend.
- Created 5 components for the frontend: main component, Createproject, CreateTask, DeleteProject, DeleteTasks.
- Implemented user authentication.

### Frontend Limitations
- Got too ambitious in terms of features.
- Unable to test frontend components properly.
- Missing a backend API endpoint to tag users based on a project.

### Backend Accomplishments
- Implemented several API endpoints.
- Created tests and validation tests.
- Registered APIs on the admin panel.

### Docker
Both frontend and backend have been dockerized.

## How to Run the App

### Using Docker
1. Run `docker-compose up --build` to build and run the containers.
2. Alternatively, run `docker-compose up` if the containers have been built previously.

### Using Virtual Environment (Windows)
1. Create a virtual environment in the project's root directory: `python -m venv venv`.
2. Activate the virtual environment: `venv/Scripts/activate`.
3. Open two terminals, one in the `frontend/` directory and one in the `time_tracker_project` directory.
4. In the frontend directory, install dependencies: `npm install` and start the frontend: `npm start`.
5. In the `time_tracker_project` (backend) directory, install dependencies: `pip install -r requirements.txt`, and run the backend server: `python manage.py runserver`.
6. To run backend tests, use: `python manage.py test`.

## Features Based on URLs (Most of it are WIP)

1. **User Authentication**:
   - `/register/`: Allows users to register with the system.
   - `/login/`: Allows registered users to log in.
   - `/logout/`: Allows logged-in users to log out.
   - `/user/`: Retrieves information about the currently logged-in user.

2. **Projects**:
   - `/projects/`: Allows users to retrieve all projects or create a new project.
   - `/projects/<int:pk>/`: Allows users to retrieve, update, or delete a specific project identified by its primary key (`<int:pk>`).

3. **Time Entries**:
   - `/time-entries/`: Allows users to retrieve all time entries or create a new time entry.
   - `/time-entries/<int:pk>/`: Allows users to retrieve, update, or delete a specific time entry identified by its primary key (`<int:pk>`).

4. **Task Descriptions**:
   - `/task-descriptions/`: Allows users to retrieve all task descriptions or create a new task description.
   - `/task-descriptions/<int:pk>/`: Allows users to retrieve, update, or delete a specific task description identified by its primary key (`<int:pk>`).

5. **Lacking Feature**:
   - `/projects/<int:pk>/users`: This URL is missing but should allow users to tag other users on a project. This feature is currently not implemented, as mentioned in the comments.
