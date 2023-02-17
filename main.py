# FOR MORE DETAILS CHECK PIXELA DOC

import requests
from datetime import datetime

USERNAME = "{Create Your User Id}"
TOKEN = "{Create Your Token}"
GRAPH_ID = "{ Create Your Graph Id}"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Studying Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora",
}
# go to https://pixe.la/v1/users/{your user name}/graphs/{your graph id}.html to check the graph and pixel

headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_date_format = today.strftime("%Y%m%d")

pixel_config = {
    "date": today_date_format,
    "quantity": input("How many hours did you studied? "),
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


# FOR UPDATING PIXELS
pixel_updating_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date_format}"

pixel_update_config = {
    "quantity": "3"
}

# response = requests.put(url=pixel_updating_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)


# FOR DELETING PIXELS

delete_end_point = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date_format}"

# response = requests.delete(url=delete_end_point, headers=headers)
# print(response.text)
