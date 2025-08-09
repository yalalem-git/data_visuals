import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime
import math

path = Path("OHUR.csv")
lines = path.read_text(encoding= 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

years = []

unemployment_rate = [] 

for row in reader:
      try:

          unet_rate = float(row[1])
          current_year = datetime.strptime(row[0], "%Y-%m-%d").year
          unemployment_rate.append(unet_rate)
          years.append(current_year)
      except ValueError as e:
           print(current_year)

#Graph the data

plt.style.use('ggplot')

fig, graph = plt.subplots(figsize = (12, 8))

graph.plot(years, unemployment_rate,  color = 'red')

graph.set_title (f"Ohio Unemployment Rate ({min(years)} - {max(years)})", color = "green", fontsize = 14)
graph.set_xlabel("Years", fontsize = 12, color = "green")
graph.set_ylabel("Unemployment Rate", fontsize = 12, color = "green")
plt.show()
