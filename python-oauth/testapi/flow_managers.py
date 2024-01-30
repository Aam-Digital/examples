import os
from auth_code_flow import FlowManager
from dotenv import load_dotenv

load_dotenv()

se_flow_manager = FlowManager(
    base_uri=os.getenv("OAUTH_BASE_URI"),
    client_id=os.getenv("OAUTH_CLIENT_ID"),
    client_secret=os.getenv("OAUTH_CLIENT_SECRET"),
    redirect_uri="http://localhost:8000/callback",
    scope="openid",
    access_token_path="/protocol/openid-connect/token",
    authorization_path="/protocol/openid-connect/auth",
)