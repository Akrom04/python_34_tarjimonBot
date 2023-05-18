import requests
from pprint import pprint
import json

def suralar_qaytar(sura):
    res=requests.get(url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu/{sura}.json")
    
    
    return res.json()

# res=requests.get(url=f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json")
# malumot=res.json()
# with open("quran1.json","w") as quran2:
#     json.dump(malumot,quran2,indent=3)

