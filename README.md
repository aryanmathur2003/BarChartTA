# BarChartTA

## Background

BarChart consists of stock data for traders to view resistance and support data. The data is updated in real time constantly with a minimal delay for last price. Using this data can be vital in making trade decisions and help in understanding the next plays and levels to watch for each of the listed stocks.
[BarChart](https://www.barchart.com/) provides ample data that is updated for us to use when looking for stock data. This code takes a list of stock tickers that we watch which you can edit in main by changing the tickers list and displays the data for resistance, support, highs, lows and last price. These levels are important to keep a watch on when making any plays on the stock. 

## Setup
This code is built entirely python. 

Make sure you have python 3 and later. Install the dependencies.


Install the requests library to load the webpages
```console
$ pip3 install requests
```

Install the bs4 library to get Beatiful Soup to parse HTML elements.
```console
$ pip3 install bs4
```

## Run

You have all the dependencies installed. Now, you just need to run the file. Use the following command
```console
$ python3 main.py>>output.txt
```
This will run the file and redirect the output to a file named output.txt. If you run this code multiple times, the output will keep getting appended to the end of the output file. Delete or clear the contents of the file if you run the code multiple times.
