"""
Visualizing Ohio's unemployment rate from 1976 todate 
by: Yalalem Tegenie
Unemployment rate dataset is downloaded from online sources, and  graphed the unemployment rates against years
8 August 2025
"""

import matplotlib.pyplot as plt
from pathlib import Path
import csv
from datetime import datetime
import math
from collections import defaultdict
path = Path("OHUR.csv")
lines = path.read_text(encoding= 'utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

year_data = defaultdict(list)

for row in reader:
      try:
          current_year = datetime.strptime(row[0], "%Y-%m-%d").year
          unet_rate = float(row[1])
          year_data[current_year].append(unet_rate)
      except ValueError as e:
           continue
years = sorted(year_data.keys())
avg_unemployment_rate = []
for y in years:
     avg_rate = sum(year_data[y])/ len(year_data[y])
     avg_unemployment_rate.append(avg_rate)
#Graph the data 

plt.style.use('ggplot')

fig, graph = plt.subplots(figsize = (12, 8))

graph.plot(years, avg_unemployment_rate,  color = 'red')

graph.set_title (f"Ohio Average Unemployment Rate ({years[0]} - {years[-1]})", color = "green", fontsize = 14)
graph.set_xlabel("Years", fontsize = 12, color = "green")
graph.set_ylabel("Unemployment Rate", fontsize = 12, color = "green")
graph.set_xticks(years[::2])
plt.xticks(rotation = 45)
graph

plt.show()
