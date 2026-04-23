# Sentinella

Sentinella is a comprehensive surveillance, security, and monitoring dashboard built with Django. It provides a web-based interface for managing incidents, viewing live camera feeds, tracking heatmaps, managing staff, and configuring system settings.

## Features

- **Dashboard**: High-level overview of system status and activities.
- **User Authentication**: Secure user registration and login functionality.
- **Live Monitor & Camera**: Interfaces for real-time video feeds and camera management.
- **Incidents**: Tracking and managing security incidents.
- **Heatmap & Floor Maps**: Spatial analytics and facility mapping.
- **Reports & History**: Detailed reporting and historical data logs.
- **Staff Portal & Accounts**: User and staff management interfaces.
- **System Configuration & Privacy Logs**: Administrative settings and audit trails.

## Tech Stack

- **Backend**: Python, Django
- **Database**: SQLite (default, can be configured for others like PostgreSQL/MySQL)
- **Frontend**: HTML/CSS/JS (integrated via Django templates)

## Project Structure

- `sentinella_project/`: Main Django project configuration folder (settings, urls).
- `sentinella_app/`: Main Django application containing views, models, and logic.
  - `templates/`: Contains all HTML files for the dashboard views.
  - `models.py`: Database schema definitions (e.g., User Registration).
  - `views.py`: Application logic and route handlers.
- `sentinella_env/`: Python virtual environment (if active).

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Installation

1. **Navigate to the project directory**:
   ```bash
   cd "Sentinella"
   ```

2. **Activate the virtual environment** (if not already active):
   ```bash
   # On Windows:
   sentinella_env\Scripts\activate
   # On macOS/Linux:
   source sentinella_env/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install django
   ```
   *(Note: If a `requirements.txt` file is added in the future, run `pip install -r requirements.txt`)*

4. **Apply database migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

- Start at the landing page and register a new user account.
- Log in to access the main dashboard.
- Navigate through the sidebar menu to access features like Live Monitor, Incidents, Heatmaps, and System Config.
