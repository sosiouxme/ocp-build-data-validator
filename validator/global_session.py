import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

request_session = None

retry_strategy = Retry(
    total=3,
    status_forcelist=[404, 429, 500, 502, 503, 504],
    method_whitelist=["HEAD", "GET", "OPTIONS"]
)
adapter = HTTPAdapter(max_retries=retry_strategy)


def set_global_session():
    global request_session
    if not request_session:
        request_session = requests.Session()
        request_session.mount("https://", adapter)
        request_session.mount("http://", adapter)
