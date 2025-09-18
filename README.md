# TaskFlow - Task Management System

TaskFlow is a comprehensive task management web application designed to help users organize their tasks efficiently. It features user authentication, full CRUD (Create, Read, Update, Delete) operations for tasks, advanced filtering and sorting capabilities, and a responsive user interface.

## ✨ Features

- **User Authentication**: Secure registration, login, and logout with JWT.
- **Task Management**: Create, view, edit, and delete tasks.
- **Task Status**: Mark tasks as completed or pending.
- **Task Prioritization**: Assign low, medium, or high priority to tasks.
- **Due Dates**: Set and track deadlines for tasks.
- **Search & Filter**: Easily find tasks by title/description, status, or priority.
- **Sorting**: Organize tasks by creation date, title, priority, or due date.
- **Dashboard Statistics**: Overview of task progress and priority breakdown.
- **Responsive Design**: Optimized for various devices (desktop, tablet, mobile).

## 🛠 Technology Stack

### Frontend
- **React 18**: JavaScript library for building user interfaces.
- **Vite**: Fast frontend build tool.
- **Tailwind CSS**: Utility-first CSS framework for rapid UI development.
- **shadcn/ui**: Reusable UI components built with Radix UI and Tailwind CSS.
- **Lucide Icons**: A collection of beautiful and customizable SVG icons.

### Backend
- **Flask**: A lightweight Python web framework.
- **SQLAlchemy**: Python SQL toolkit and Object-Relational Mapper (ORM).
- **SQLite**: A self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine.
- **Flask-JWT-Extended**: Adds JWT (JSON Web Token) support to Flask.
- **Flask-Bcrypt**: Provides bcrypt hashing utilities for Flask.
- **Flask-CORS**: A Flask extension for handling Cross-Origin Resource Sharing (CORS).

## 🚀 Getting Started

Follow these instructions to set up and run the TaskFlow application on your local machine.

### Prerequisites

Before you begin, ensure you have the following installed:
- **Node.js** (LTS version recommended, includes npm/pnpm)
- **Python 3.9+**
- **Git**

### 1. Clone the Repository

```bash
git clone <repository_url> # Replace with your repository URL
cd task-manager-backend
```

### 2. Backend Setup

Navigate to the `task-manager-backend` directory, create a virtual environment, install dependencies, and run the Flask application.

```bash
cd task-manager-backend
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
python src/main.py
```

The backend server will start on `http://localhost:5000`.

### 3. Frontend Setup

Open a new terminal, navigate to the `task-manager-frontend` directory, install dependencies, and start the React development server.

```bash
cd task-manager-frontend
pnpm install # Or npm install / yarn install
pnpm run dev
```

The frontend development server will start on `http://localhost:5173`.

### 4. Access the Application

Open your web browser and navigate to `http://localhost:5173`.

- **Register**: Create a new user account.
- **Login**: Use your registered credentials to access the dashboard.
- **Manage Tasks**: Start creating, updating, and deleting your tasks!

## 📂 Project Structure

```
.
├── task-manager-backend/
│   ├── venv/                   # Python virtual environment
│   ├── src/
│   │   ├── models/             # Database models (User, Task)
│   │   ├── routes/             # API routes (auth, task, user)
│   │   ├── static/             # Frontend build files will be copied here for deployment
│   │   ├── main.py             # Flask application entry point
│   │   └── database/
│   │       └── app.db          # SQLite database file
│   └── requirements.txt        # Python dependencies
├── task-manager-frontend/
│   ├── public/
│   ├── src/
│   │   ├── assets/             # Static assets
│   │   ├── components/         # React components (Login, Dashboard, UI components)
│   │   ├── contexts/           # React context for authentication
│   │   ├── App.css             # Global CSS for React app
│   │   ├── App.jsx             # Main React application component
│   │   └── main.jsx            # React entry point
│   ├── index.html              # HTML entry file
│   ├── package.json            # Node.js dependencies and scripts
│   └── vite.config.js          # Vite configuration
└── TaskFlow_Documentation.md   # Detailed application documentation
```

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

