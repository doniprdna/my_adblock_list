# adblock
trial automatic update rule adblock openclash


Untuk menggunakan, edit config.yaml pada /etc/openclash/config/config.yaml seperti ini:

rule-providers:
  easylist_adservers:
    type: http
    behavior: classical
    path: "./rule_provider/easylist_adservers.yaml"
    url: https://raw.githubusercontent.com/doniprdna/my_adblock_list/main/easylist_adservers.yaml
    interval: 86400 # Update rules every 24 hours
    
rules:
- RULE-SET,easylist_adservers,REJECT
