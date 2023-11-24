from dotenv import load_dotenv

import os
from typing import Dict, NamedTuple

load_dotenv()


class FirebaseCreds(NamedTuple):
    type: str = os.environ.get("FIREBASE_TYPE")
    project_id: str = os.environ.get("FIREBASE_PROJECT_ID")
    private_key_id: str = os.environ.get("FIREBASE_PRIVATE_KEY_ID")
    private_key: str = os.environ.get("FIREBASE_PRIVATE_KEY")
    client_email: str = os.environ.get("FIREBASE_CLIENT_EMAIL")
    client_id: str = os.environ.get("FIREBASE_CLIENT_ID")
    auth_uri: str = os.environ.get("FIREBASE_AUTH_URI")
    token_uri: str = os.environ.get("FIREBASE_TOKEN_URI")
    auth_provider_x509_cert_url: str = os.environ.get(
        "FIREBASE_AUTH_PROVIDER_X509_CERT_URL"
    )
    client_x509_cert_url: str = os.environ.get("FIREBASE_CLIENT_X509_CERT_URL")
    universe_domain: str = os.environ.get("FIREBASE_UNIVERSE_DOMAIN")

    def to_json(self) -> Dict[str, str]:
        var = [
            i
            for i in vars(FirebaseCreds).keys()
            if not i.startswith("_") and i != "to_json"
        ]
        return {i: getattr(self, i) for i in var}
