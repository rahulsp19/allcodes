import matplotlib.pyplot as plt

# Sample data
categories = ['Group A', 'Group B', 'Group C', 'Group D']
means = [25, 40, 30, 55]
errors = [2.5, 4.0, 3.2, 5.1]

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(8, 6))

# Generate the bar plot with error bars (yerr) and caps on the error lines (capsize)
bars = ax.bar(categories, means, yerr=errors, capsize=5, 
              color='lightblue', edgecolor='black')

# Attach text labels above each bar
# padding=5 ensures the label clears the top of the error bar
ax.bar_label(bars, padding=5, fmt='%.1f')

# Format the chart
ax.set_xlabel('Categories')
ax.set_ylabel('Values')
ax.set_title('Sample Data: Bar Plot with Error Bars')

# Adjust layout to prevent clipping of the top labels
plt.ylim(0, 65) 
plt.tight_layout()

# Render the plot
plt.show()
