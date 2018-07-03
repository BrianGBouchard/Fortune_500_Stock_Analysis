from bs4 import BeautifulSoup
import requests

def get_ROE(ticket):
    url = ("https://finance.yahoo.com/quote/" + ticket + "/key-statistics")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    table_stats = soup.find_all("td")
    try:
        ROE = table_stats[29].text
    except:
        return
    try:
        if "%" in ROE:
            ROE = ROE.replace("%","")
        else:
            pass
        if "," in ROE:
            ROE = ROE.replace(",", "")
        else:
            pass
    except:
        return
    try:
        ROE = float(ROE)
        if ROE > 15:
            return True
        else:
            return False
    except:
        return

def get_QEG(ticket):
    url = ("https://finance.yahoo.com/quote/" + ticket + "/key-statistics")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    table_stats = soup.find_all("td")
    try:
        QEG = table_stats[45].text
    except:
        return
    try:
        if "%" in QEG:
            QEG = QEG.replace("%","")
        else:
            pass
        if "," in QEG:
            QEG = QEG.replace(",", "")
        else:
            pass
    except:
        return
    try:
        QEG = float(QEG)
        if QEG > 0:
            return True
        else:
            return False
    except:
        return

def get_DER(ticket):
    url = ("https://finance.yahoo.com/quote/" + ticket + "/key-statistics")
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    table_stats = soup.find_all("td")
    try:
        DER = table_stats[53].text
    except:
        return
    try:
        if "%" in DER:
            DER = DER.replace("%","")
        else:
            pass
        if "," in DER:
            DER = DER.replace(",", "")
        else:
            pass
    except:
        return
    try:
        DER = float(DER)
        if DER < 75:
            return True
        else:
            return False
    except:
        return
