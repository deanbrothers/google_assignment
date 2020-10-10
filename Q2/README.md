#Title
CountrySide Food 

#Download File


#Installation
Step1: Install python
        sudo apt-get install python3.7
Step2: Install pip
        sudo apt-get install python3-pip
Step3: Install virtualenv
        sudo apt-get install python3.7-venv
        python venv countryenv
Step4: Activate virtualenv
        source countryenv/bin/activate
Step5: Install requirements
        python -m pip install -r requirements.txt
Step6: Migrate DB
        python manage.py migrate
Step6: Run Program
        python manage.py runserver