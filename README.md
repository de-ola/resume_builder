Server Instructions

Install all required packages => "python -m pip install -r requirements.txt" / "python3 -m pip install -r requirements.txt"
Create superuser => "python manage.py createsuperuser"
Run server => "python manage.py runserver"

Endpoints and functions

'accounts/profile/' => this shows the user details
'accounts/register/' => this helps create a new user
'accounts/login/' => this authenticates already existing user
'accounts/change_password/<int:pk>/' => this endpoint is in charge of changing user passwords
'accounts/update_profile/<int:pk>/' => this edits your profile
'accounts/login/refresh/'  => this authenticates already existing user