import yaml
import requests
from bs4 import BeautifulSoup as bs
with open('config.yml', "r") as cfg:
    config = yaml.safe_load(cfg)
payload = config["form_input"]
k_main = config["koha_main"]
k_file =  config["koha_file"]
headers = {'User-Agent': 'Mozilla/5.0'}
with open(config["destination"], 'wb') as f:
    s = requests.session()
    resp = s.get(k_main, headers=headers)
    c = requests.utils.cookiejar_from_dict(
        requests.utils.dict_from_cookiejar(s.cookies)
    )
    s.post(k_main, data = payload, cookies = c)
    w = s.get(k_file)
    soup = bs(w.content,features="html.parser")
    for link in soup.findAll('a', href=True, text='borrowers.db'):
        target = config["koha_base"] + link["href"]
    print(target)
    t = s.get(target)
    f.write(t.content)