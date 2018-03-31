from ubiome import *
import matplotlib.pyplot as plt

new = UbiomeSample("ubiome/testdata/ubiome-export-data-2018-03-03.json")
old = UbiomeSample("ubiome/testdata/ubiome-export-data-2018-01-23.json")

x = UbiomeMultiSample(old)
x.merge(new)    # Merge sample

samples = x.originalSampleObjects   # produce UBiomeSample objects of merged items
diversity = [sample.diversity() for sample in samples]  # Store diversity values (Simpson's)
dates = [sample.date for sample in samples]     # Store sample dates

# Set date tick labels for matplotlib
date_labels = [i.strftime('%B %d, %Y') for i in dates]

# Begin plotting
plt.style.use('ggplot')
plt.plot(dates, diversity, 'o-')
plt.xticks(dates, date_labels, rotation=30)
plt.title("Sample diversity over time")
plt.tight_layout()
plt.show()
