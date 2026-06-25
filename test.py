# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Create a sample dataset
data = pd.DataFrame({
    'Height': [150, 160, 165, 170, 175, 180, 185],
    'Weight': [50, 55, 60, 65, 70, 75, 80],
    'Age Group': ['Teen', 'Teen', 'Young Adult', 'Young Adult', 'Adult', 'Adult', 'Senior']
})

# Create a scatter plot using Seaborn
sns.set(style="dark")  # Set the theme
sns.scatterplot(data=data, x='Height', y='Weight', hue='Age Group', style='Age Group', s=100)

# Add labels and a title
plt.title("Height vs. Weight Scatter Plot")
plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")

# Show the plot
plt.show()
