# Disaster-connect

Disaster Connect (Crowdsourced Emergency Web Platform) An open-source, web-based platform enabling users to report live disaster incidents (with geo-tagged photos or videos) and view them in real-time. Users can set a notification radius (e.g., 50 km) to receive updates only about nearby incidents—keeping alerts relevant and manageable.

🔧 Step-by-Step Setup

    Create Root Folder
    mkdir DisasterConnect
    cd DisasterConnect

# Create virtual env & activate

python -m venv env
source env/bin/activate # Windows: env\Scripts\activate

# Install Django

pip install django

# Start project & app

django-admin startproject disasterconnect .
python manage.py startapp disasterapp
