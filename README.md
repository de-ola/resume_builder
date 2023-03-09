Server Instructions

Install all required packages => "python -m pip install -r requirements.txt" / "python3 -m pip install -r requirements.txt"
Create superuser => "python manage.py createsuperuser"
Run server => "python manage.py runserver"

Endpoints and functions

'api/accounts/profile/' => this shows the user details
'api/accounts/register/' => this helps create a new user
'api/accounts/login/' => this authenticates already existing user
'api/accounts/change_password/<int:pk>/' => this endpoint is in charge of changing user passwords
'api/accounts/update_profile/<int:pk>/' => this edits your profile
'api/accounts/login/refresh/'  => this authenticates already existing user

'api/bio/create/' => this created the user bio
'api/bio/edit/<int:pk>/' => this edits the user's bio
'api/projects/add/' => this created a new project
'api/projects/edit/<int:pk>/' => edits already created projects
'api/resume/' => this shows the complete resume data of the current loggrd in user
'api/resume/list/' => this gives a list of resumés of different users