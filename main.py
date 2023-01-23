import requests
from bs4 import BeautifulSoup

url = "https://www.barchart.com/stocks/quotes/MSFT/cheat-sheet"
url2 = "https://www.barchart.com/stocks/quotes/NVDA/cheat-sheet"
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
response = requests.get(url2, headers=headers)
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

#
# pivot point
#
pivotPoint = cheatString.split("\"labelTurningPoints\":\"Pivot Point\",\"category\":\"pivots\",\"class\":\"low pivot-points\",\"rawValue\":")
pp = pivotPoint[1].split('},', 1)[0]
print("Pivot Point: " + pp)

#
# Support levels 1, 2 and 3
#

# support 1

support1 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 1st Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
#print(support1[1])
supportFirst = support1[1].split('},', 1)[0]
print("Support Level 1: " + supportFirst)

# support 2
support2 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 2nd Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
#print(support2[1])
supportSecond = support2[1].split('},', 1)[0]
print("Support Level 2: " + supportSecond)

# support 3
support3 = cheatString.split("\"labelSupportResistance\":\"Pivot Point 3rd Support Point\",\"labelTurningPoints\":\"\",\"category\":\"pivots\",\"class\":\"low support-resistance\",\"rawValue\":")
#print(support3[1])
supportThird = support3[1].split('},', 1)[0]
print("Support Level 3: " + supportThird)