# Python example for OAuth flow

## Usage
To start the development server you need to first initialize the missing variables in the `.env` file.
You should be able to get the required information e.g. from you Keycloak confidential client.

Then install the required dependencies:
> pip install -r requirements.txt

Finally, the application can be started

> python manage.py runserver 

Visit `http://localhost:8000` and click the link to authenticate.
This should forward you to you OAuth login page where you can log in.
Once this succeeds the application can request an access token on behalf of the logged-in user.
