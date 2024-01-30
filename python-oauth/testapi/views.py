from uuid import uuid4
from django.http import HttpResponse
from .flow_managers import se_flow_manager

# See https://pypi.org/project/auth-code-flow/
def index(request):
    state = str(uuid4())
    # you'll probably store the state in the database against the
    # logged-in user, so that you can always find out who the state
    # was created for

    # get the authorization url
    se_auth_url = se_flow_manager.get_authorization_endpoint(state)
    # display it on the web page for the user
    html_content = f"""
    <html>
        <head>
            <title>Connect your account</title>
        </head>
        <body>
            <p>Please select any of the links below to connect your account to the provider</p>
            <p><a href="{se_auth_url}">Connect to Aam Digital</a></p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

def callback(request):
    state = request.GET.get('state');
    code = request.GET.get('code');
    # check that the returned state was created by
    # you for the logged-in user
    # if the state checks out, fetch the SE access token for the user
    # note that SE requires posting the parameters to the access
    # token retrieval endpoint as form data -- application/x-www-form-urlencoded
    resp = se_flow_manager.fetch_access_token(code, state, post_form_data=True)
    resp_json = resp.json()

    # you now have an access token to SE services for the SE user
    # you'll probably save it to the database against the
    # logged-in user...
    # but we'll just display it on a HTML page
    html_content = f"""
    <html>
        <head>
            <title>Connected to Aam Digital</title>
        </head>
        <body>
            <h3>Yayyyyyy</h3>
            <p>We've successfully obtained your Aam Digital access token!</p>
            <p>{resp_json}</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)