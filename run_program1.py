from get_history_testEdit import *
from get_roe_testTEST import *
from ticket_list1 import *


def main(tickets):
    viable_list = []
    for item in tickets:
        try:
            if get_ROE(item) is True and get_QEG(item) is True and get_DER(item) is True and get_history(item) is True:
                print("added")
                viable_list.append(item)
            else:
                print("not added")
        except:
            pass
    print("The following stocks are good investments based on the following metrics: 1) Stock appears on Fortune 500 list.  2) R.O.E. > 15%.  3) Quarterly Earnings Growth > 0%.  4) Debt/Equity Ratio < 75.  5) Stock has 5 year net increase.")
    print(viable_list)

main(ticket_list)
