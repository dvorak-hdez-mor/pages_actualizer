from bs4 import BeautifulSoup
import requests
import schedule

def botSendText(message):
    bot_Token = "1581914396:AAFNlQ2z5NFelnufBXXFSnE2aOQo3zL19aI"
    bot_Id = "911719849"
    sendText = "https://api.telegram.org/bot" + bot_Token + "/sendMessage?chat_id=" + bot_Id + "&parse_mode=Markdown&text=" + message

    response = requests.get(sendText)

    return response

def btcScraping():
    url = requests.get("https://cinenivel.blogspot.com/2020/10/ver-madre-madre-madeo-2009.html?m=1")
    soup = BeautifulSoup(url.content, "html.parser")
    result = soup.find('h3', {'class': 'post-title entry-title'})
    format_result = result.text

    return format_result

testBot = botSendText(btcScraping())
