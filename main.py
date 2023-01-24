import requests
from bs4 import BeautifulSoup


def BARchart(ticker):
    url = "https://www.barchart.com/stocks/quotes/"+ ticker +"/cheat-sheet"
    url2 = "https://www.barchart.com/stocks/quotes/NVDA/cheat-sheet"
    headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # gets graph of cheat sheet and creates string with data
    cheat_sheet = soup.find_all("div", {"class": "bc-cheat-sheet"})
    cheatString = str(cheat_sheet)
    print(cheatString)

    #
    # Resistance of stock 1, 2, 3
    #
    # resistance 1

    # resistance 3
    resistance3 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 3rd Level Resistance\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(resistance3[1])
    resistanceThird = resistance3[1].split('},', 1)[0]
    print("Resistance Level 3: " + resistanceThird)

    # resistance 2
    resistance2 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 2nd Level Resistance\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(resistance2[1])
    resistanceSecond = resistance2[1].split('},', 1)[0]
    print("Resistance Level 2: " + resistanceSecond)

    # resistance 1
    resistance1 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 1st Resistance Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(resistance1[1])
    resistanceFirst = resistance1[1].split('},', 1)[0]
    print("Resistance Level 1: " + resistanceFirst)

    # #
    # # pivot point
    # #
    # pivot = cheatString.split("\"labelTurningPoints\":\"Pivot Point\",\"category\":\"pivots\",\"class\":\"high pivot-points\",\"rawValue\":")
    # print(len(pivot))
    # if pivot[1]:
    #         pivot = cheatString.split("\"labelTurningPoints\":\"Pivot Point\",\"category\":\"pivots\",\"class\":\"low pivot-points\",\"rawValue\":")
    #         print("Check")
    #
    # pp = pivot[1].split('},', 1)[0]
    #
    # print("Pivot Point: " + pp)

    #
    # Support levels 1, 2 and 3
    #

    # support 1
    support1 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 1st Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support1[1])
    supportFirst = support1[1].split('},', 1)[0]
    print("Support Level 1: " + supportFirst)

    # support 2
    support2 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 2nd Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support2[1])
    supportSecond = support2[1].split('},', 1)[0]
    print("Support Level 2: " + supportSecond)

    # support 3
    support3 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 3rd Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support3[1])
    supportThird = support3[1].split('},', 1)[0]
    print("Support Level 3: " + supportThird)

    #
    # Highs 1 month, 13 weeks and 52 weeks
    #

    # 1 month high
    high1 = cheatString.split("\"labelSupportResistance\":\"1-Month High\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(support1[1])
    highFirst = high1[1].split('},', 1)[0]
    print("1 Month High: " + highFirst)

    # 13-Week high
    high2 = cheatString.split("\"labelSupportResistance\":\"13-Week High\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(support1[1])
    highSecond = high2[1].split('},', 1)[0]
    print("13 Week High: " + highSecond)

    # 52-week high
    high3 = cheatString.split("\"labelSupportResistance\":\"52-Week High\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"high support-resistance\",\"rawValue\":")
    # print(support1[1])
    highThird = high3[1].split('},', 1)[0]
    print("52 Week High: " + highThird)

    #
    # Lows 1 month, 13 weeks and 52 weeks
    #

    # 1 month low
    low1 = cheatString.split("\"labelSupportResistance\":\"1-Month Low\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support1[1])
    lowFirst = low1[1].split('},', 1)[0]
    print("1 Month Low: " + lowFirst)

    # 13-Week low
    low2 = cheatString.split("\"labelSupportResistance\":\"13-Week Low\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support1[1])
    lowSecond = low2[1].split('},', 1)[0]
    print("13 Week Low: " + lowSecond)

    # 52-week low
    low3 = cheatString.split("\"labelSupportResistance\":\"52-Week Low\",\"labelTurningPoints\":\"\",\"category\":\"highsLows\",\"class\":\"low support-resistance\",\"rawValue\":")
    # print(support1[1])
    lowThird = low3[1].split('},', 1)[0]
    print("52 Week Low: " + lowThird)

    # Last Price
    last = cheatString.split("\"labelSupportResistance\":\"Last\",\"labelTurningPoints\":\"Last\",\"category\":\"showAlways\",\"class\":\"current\",\"rawValue\":")
    # print(support1[1])
    last1 = last[1].split('},', 1)[0]
    print("Last Price: " + last1)

if __name__ == "__main__":
    tickers = ["MSFT", "NVDA", "GOOGL", "SPY", "QQQ"]
    for t in tickers:
        print("Stock Ticker: " + t)
        BARchart(t)
        print()
