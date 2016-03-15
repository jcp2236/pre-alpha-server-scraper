import requests
from lxml import html

username = "arcgisadmin"
password = "C@s3yTr33s"

login_url = 'http://64.197.172.212/arcgis/rest/login?redirect=http%3A//64.197.172.212/arcgis/rest/services/mobile_app_all/combined_services/FeatureServer/replicas'
url = 'http://64.197.172.212/arcgis/rest/services/mobile_app_all/combined_services/FeatureServer/replicas'

session_requests = requests.session()

payload = {
    "username": username,
    "password": password
}

#perform login
result = session_requests.post(login_url, data = payload, headers = dict(referer=login_url))

#scrape URL
result = session_requests.get(url, headers = dict(refereer = url))
tree = html.fromstring(result.content)
replicas = tree.findall("div[@class='rbody']")
replica_names = [replica.text_content().strip for replica in replicas]

print replicas
print replica_names
