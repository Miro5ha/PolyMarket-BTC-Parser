import os
import time
import requests
import pandas as pd
import fake_useragent
from bs4 import BeautifulSoup
from datetime import datetime


def bet_parser():
    user = fake_useragent.UserAgent().random
    header = {"user-agent": user}
    link = "https://polymarket.com/event/what-price-will-bitcoin-hit-before-2027"

    response = requests.get(link, headers=header).text
    soup = BeautifulSoup(response, "lxml")

    bets_block = soup.find("div", class_="border-t border-border")
    all_values = bets_block.find_all(
        "p", class_="font-semibold text-heading-2xl text-[28px] text-text-primary"
    )
    all_strikes = bets_block.find_all(
        "p",
        class_="overflow-hidden whitespace-nowrap text-ellipsis font-semibold text-heading-lg max-w-[400px] min-[1024px]:max-[1050px]:max-w-[170px] min-[1050px]:max-[1080px]:max-w-[200px] min-[1080px]:max-[1140px]:max-w-[230px] min-[1140px]:max-[1220px]:max-w-[320px]",
    )

    bet_value = []
    bet_strike = []

    for value in all_values:
        bet_value.append(value.text)

    for strike in all_strikes:
        bet_strike.append(strike.text)

    now = datetime.now()
    data = {"date": [now.strftime("%d.%m.%Y")], "time": [now.strftime("%H:%M:%S")]}

    for i in range(len(bet_strike)):
        column_name = bet_strike[i]
        value = bet_value[i]
        data[column_name] = [value]

    bet_df = pd.DataFrame(data)
    file_path = "BETS.csv"
    file_exists = os.path.isfile(file_path)
    bet_csv = bet_df.to_csv(
        file_path,
        sep=";",
        index=False,
        mode="a",
        encoding="utf-8",
        header=not file_exists,
    )
    print(bet_csv)


if __name__ == "__main__":
    while True:
        bet_parser()
        time.sleep(3600)