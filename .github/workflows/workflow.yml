import requests

def get_adblock_list():
    try:
        r = requests.get("https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt")
        adblock_list = r.text.split("\n")
        adblock_list = [line.replace("||", "").replace("^", "") for line in adblock_list if not line.startswith('!')]
        adblock_list = ["  - DOMAIN, " + domain for domain in adblock_list if domain]
        adblock_list.insert(0, "payload:")
        return adblock_list
    except Exception as e:
        print(e)
        return None

adblock_list = get_adblock_list()
if adblock_list:
    with open("easylist_adservers.yaml", "w", encoding='utf-8') as f:
        f.write("\n".join(adblock_list))
