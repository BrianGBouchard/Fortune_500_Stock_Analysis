import requests
from bs4 import BeautifulSoup
import time

def get_history(ticket):
    current_unix = round(time.time())
    prev_unix = current_unix - 157700000
    prev_unix1 = current_unix - 157959200
    current_unix1 = current_unix - 259200
    current_unix = str(current_unix)
    current_unix1 = str(current_unix1)
    prev_unix = str(prev_unix)
    prev_unix1 = str(prev_unix1)
    url = "https://finance.yahoo.com/quote/" + ticket + "/history?period1=" + prev_unix1 + "&period2=" + prev_unix + "&interval=1d&filter=history&frequency=1d"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    soup_list = soup.find_all("td")
    url1 = "https://finance.yahoo.com/quote/" + ticket + "/history?period1=" + current_unix1 + "&period2=" + current_unix + "&interval=1d&filter=history&frequency=1d"
    r1 = requests.get(url1)
    soup1 = BeautifulSoup(r1.content, "html.parser")
    soup_list1 = soup1.find_all("td")
    try:
        recent_price = (soup_list1[4].text)
        old_price = (soup_list[4].text)
    except:
        return
    try:
        if "," in recent_price:
            recent_price = recent_price.replace(",", "")
        else:
            pass
    except:
        pass
    try:
        if "," in str(old_price):
            old_price = old_price.replace(",", "")
        else:
            pass
    except:
        pass
    try:
        if (float(recent_price) - float(old_price) > 0):
            return True
        else:
            return False
    except:
        pass


