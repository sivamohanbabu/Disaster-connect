# Disaster-connect

Disaster Connect (Crowdsourced Emergency Web Platform) An open-source, web-based platform enabling users to report live disaster incidents (with geo-tagged photos or videos) and view them in real-time. Users can set a notification radius (e.g., 50 km) to receive updates only about nearby incidents—keeping alerts relevant and manageable.

🔧 Step-by-Step Setup

1.  Create Root Folder
    mkdir DisasterConnect
    cd DisasterConnect

2.  Create Backend (Django)

# Create and activate virtual environment

python -m venv env
source env/bin/activate # or `env\Scripts\activate` on Windows

# Install Django and DRF

pip install django djangorestframework

# Start Django project

django-admin startproject disasterconnect backend
cd backend

# Start Django app

python manage.py startapp api
