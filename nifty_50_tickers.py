import csv

FILE_PATH = "C:/Users/DELL/Downloads/MW-NIFTY-50-14-Oct-2023.csv"
# FILE_PATH = "C:/Users/DELL/Downloads/MW-NIFTY-TOTAL-MARKET-03-Nov-2023.csv"


tickers = []
with open(FILE_PATH, "r") as csv_file:
    data = csv.reader(csv_file)
	# next(data)
	# # next(data)
    for row in data:

        if len(row) > 6:
            # print(row[0])
            tickers.append(row[0])
      
tickers.pop(0)

print(tickers)


   

