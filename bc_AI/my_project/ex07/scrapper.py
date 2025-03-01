import requests
from bs4 import BeautifulSoup

url = "https://data.1337ai.org/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

fd = open("data.csv", "w")

for j in soup.find_all("th"):
    fd.write(j.text)
for row in soup.find_all("tr"):
    line = ""
    for td in row.find_all("td"):
        line += td.text.strip() + ","
    fd.write(line.rstrip(",") + "\n")

              
                        
