import requests

url = "https://api.extremecloudiq.com/devices***/"

payload="[\"show run\"]"
headers = {
  'accept': '***'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
