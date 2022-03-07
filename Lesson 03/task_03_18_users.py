# author

import requests
import json

# put your id and secret here
client_id = '...'
client_secret = '...'

resp = requests.post("https://api.artsy.net/api/tokens/xapp_token";, data={"client_id" : client_id, "client_secret" : client_secret}).text
token = json.loads(resp)["token"]

def get_json(url):
    headers = {"X-Xapp-Token" : token}
    resp = requests.get(url, headers=headers).text
    return json.loads(resp)

ans = []

with open("input.txt") as inp:
    for id in inp:
        id = id.rstrip()
        js = get_json("https://api.artsy.net/api/artists/"; + id)
        ans.append((js["birthday"], js["sortable_name"]))

ans.sort(key=lambda x: (int(x[0]), x[1]))
print("\n".join(map(lambda x: x[1], ans)))




res = []
with open('dataset_24476_4.txt', 'r') as f, open('result.txt', 'w', encoding='utf-8') as w:
    for i in f:
        req_str = 'https://api.artsy.net/api/artists/' + i.rstrip()
        j = requests.get(req_str, headers=headers).json()
        res.append(j['birthday']+j['sortable_name'])
    for i in sorted(res):
        w.write(i[4:]+'\n')


import requests
import json

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": "...",
                      "client_secret": "..."
                  })
headers = {"X-Xapp-Token": json.loads(r.text)["token"]}
db = []
with open("sample.txt") as f:
    for a in f:
        r = json.loads(requests.get("https://api.artsy.net/api/artists/{}".format(a.strip()), headers=headers).content.decode())
        db.append((r["birthday"], r["sortable_name"]))
print(*(d[1] for d in sorted(db)), sep="\n")

