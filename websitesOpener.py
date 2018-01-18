#! python3
# websitesOpener.py - Opens for us our most viewed websites and files automatically.

import requests, sys, webbrowser, bs4, os, time

start_time = time.time()

files_list = [
"C:\\Users\\Daniel\\Downloads\\BUDŻET DOMOWY 2018.xlsx",
"C:\\Users\\Daniel\\Downloads\\12-tygodni-Szablon.xlsx",
"C:\\Users\\Daniel\\Downloads\\Inwestycje w kryptowaluty.xlsx"
]

try:
	print('Openning list of files...')
	for file in files_list:
		file = os.startfile(file)
except Exception as exc:
	print('There was a problem: %s' % (exc))

link_list = [
"https://mail.google.com/mail/u/0/#inbox", 
"https://www.facebook.com/",
"https://www.instagram.com/",
"https://twitter.com/",
"https://www.youtube.com/feed/subscriptions",
"https://coin.fyi/",
"https://coinmarketcap.com/",
"https://www.binance.com/userCenter/tradeHistory.html",
"https://www.kucoin.com/#/user/account/deal-orders",
"https://www.cryptopia.co.nz/TradeHistory"
]

print('Openning list of websites...')
for link in link_list:
	webpage = webbrowser.open(link) 

end_time = time.time()
print("\n--- %s seconds ---" % round((end_time - start_time),2))
