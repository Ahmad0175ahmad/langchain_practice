from langchain_community.document_loaders import WebBaseLoader

url="https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7x4hn-a/p/itmdc5308fa78421?pid=COMH64PY76CJKBYU&lid=LSTCOMH64PY76CJKBYUOL7TOK&marketplace=FLIPKART&q=macbook&store=6bo%2Fb5g&spotlightTagId=default_BestsellerId_6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=76963fd8-67dc-44b1-a3aa-d94b18e8adb5.COMH64PY76CJKBYU.SEARCH&ppt=sp&ppn=sp&ssid=gnlxl3un1c0000001772796501823&qH=864faee128623e2f&ov_redirect=true"

loader= WebBaseLoader(url)

docs =loader.load()

print(len(docs))

print(docs[0].page_content)



