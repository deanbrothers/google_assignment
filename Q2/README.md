# google_assignment

#Download Code\
git clone https://github.com/deanbrothers/google_assignment.git

#Demo link: https://agroezy.uc.r.appspot.com/ 


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


#TestCase Run
1. python manage.py test fortune.tests.FortuneCookieTestCase.get_fortune_with_name 
2. python manage.py test fortune.tests.CompanyTestCase.get_company_with_id

