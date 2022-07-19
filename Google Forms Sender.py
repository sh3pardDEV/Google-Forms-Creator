import requests;
requestsSend = 0
DocsURL = "https://docs.google.com/forms/d/e/1FAIpQLSdocbCFAVO11dsiPJ9knKgAx3_fc5zvpUqQc6WB4MF3QtR9XA"
send = 0
urlResponse = DocsURL+"/formResponse"
urlReferer = DocsURL+"/viewform"
requestsValue = int(input("Укажите количество анкет, которых нужно заполнить: "))
if requestsValue >= 400:
    print("Ошибка. Такое количество анкет нельзя указать (могут быть ограничения от Google)")
else:
    print("OK.")
while send != requestsValue:
    send+=1
    requestsSend-=1
    form_data = {'entry.119283706': 'test request'}
    print(f"Отправлено {send} запросов")
    user_agent = {'Referer':urlReferer,'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    r = requests.post(urlResponse, data=form_data, headers=user_agent) 
