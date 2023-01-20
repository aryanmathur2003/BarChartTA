import requests

url = "https://www.barchart.com/stocks/quotes/MSFT/cheat-sheet"

payload = ""
# headers = {"cookie": "market=eyJpdiI6Ik5GUjZPUi9HNkFBanp3UmcyL0dpd3c9PSIsInZhbHVlIjoiS0RMSFRxRWRaOGN3QkU3VzRRbE1RZjlvMlQ1SFI1UHB3Wk1MclhDR0twSGZ3VTJJYS8zMVBpeFR6Z21HM2JnaiIsIm1hYyI6IjlhMTE1OWFiNDI5YzY5NWYwY2JiZDAzMzVmYTdmYTI0ODNjM2YyMmIxYmQ5OGZiYThjM2U0YTI5NGM2MzJlMzgifQ%253D%253D"}
headers = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'}
response = requests.get(url, headers=headers)

print(response.text)