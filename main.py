import requests
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")
USER_NAME = os.getenv("USER_NAME")
G_ID = os.getenv("G_ID")


pixela_endpoint = "https://pixe.la/v1/users"
user_parm = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json= user_parm)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
graph_config = {
    "id": G_ID,
    "name": "To code",
    "unit": "hr",
    "type": "int",
    "color": "ichou",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = datetime.now()

pixela_post = f"{graph_endpoint}/{G_ID}"
pixela_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "15",
}

# response = requests.post(url=pixela_post, json=pixela_config, headers=headers)
# print(response.text)
update_endpoint = f"{pixela_post}/{pixela_config['date']}"
update_parm = {
    "quantity": "10",
}

# response = requests.put(url=update_endpoint, json=update_parm, headers=headers)
delete_endpoint = update_endpoint
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
