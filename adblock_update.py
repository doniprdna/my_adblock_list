import requests

def get_adblock_list():
    try:
        r = requests.get("https://easylist.to/easylist/easylist.txt")
        adblock_list = r.text.split("\n")
        adblock_list = ["DOMAIN, " + domain for domain in adblock_list if domain]
        return adblock_list
    except Exception as e:
        print(e)
        return None

adblock_list = get_adblock_list()
if adblock_list:
    with open("adblock_list.yaml", "w", encoding='utf-8') as f:
        f.write("\n".join(adblock_list))
