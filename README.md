# google_assignment

#Download Code\
git clone https://github.com/deanbrothers/google_assignment.git

#Project Details
1. Q1: This folder contains the solution of <b>The Maximachine challenge</b>
2. Q2: This folder contains the food website which gives the fortune cookie.\
#Demo link: https://agroezy.uc.r.appspot.com/ 
3. Q3: This folder contains the database schema for carpet distributor company.


#Installation\
Step1: Install python\
	sudo apt-get install python3.7\
Step2: Install pip\
        sudo apt-get install python3-pip\
Step3: Install virtualenv\
        sudo apt-get install python3.7-venv\
        python venv countryenv\
Step4: Activate virtualenv\
        source countryenv/bin/activate\
Step5: Install requirements\
	cd google_assignment/Q2/\
        python -m pip install -r requirements.txt\
Step6: Migrate DB\
        python manage.py migrate\
Step6: Run Program\
        python manage.py runserver
