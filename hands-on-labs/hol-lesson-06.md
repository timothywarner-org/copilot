# Hands-on Lab: Analyze and Visualize Data using GitHub Copilot

![GitHub Copilot Badge](https://img.shields.io/badge/GitHub-Copilot-blue?style=flat-square&logo=github)

## Overview
In this hands-on lab, you'll learn how to leverage GitHub Copilot for data analysis and visualization tasks using Python. You'll work with real-world datasets and use Copilot to generate analysis code, create visualizations, and interpret results.

**Duration**: 20-25 minutes

## Prerequisites
- VS Code with GitHub Copilot and Copilot Chat extensions
- Python 3.8+ installed
- Required packages: pandas, matplotlib, seaborn, numpy
- Basic understanding of data analysis concepts

## Exercise 1: Setting Up Your Analysis Environment (5 min)

1. Create a new Jupyter notebook:
```python
@workspace /newNotebook
# Create a data analysis environment with pandas, matplotlib, and seaborn imports
```

2. Install required packages using terminal:
```bash
@terminal pip install pandas matplotlib seaborn numpy
```

## Exercise 2: Loading and Exploring Data (5 min)

1. Load the sample dataset:
```python
# @dataset Load and display first few rows of the Titanic dataset
```

2. Generate basic exploratory analysis:
```python
# Create descriptive statistics and initial data exploration for the dataset
```

## Exercise 3: Data Visualization (5 min)

1. Create basic visualizations:
```python
# @vis Create a bar chart showing survival rates by passenger class
```

2. Generate advanced plots:
```python
# @vis Create a correlation heatmap for numeric columns with custom styling
```

## Exercise 4: Statistical Analysis (5 min)

1. Perform statistical tests:
```python
# @stats Run chi-square test for independence between survival and gender
```

## Challenge Exercises

1. Use Copilot to:
   - Generate a machine learning model prediction
   - Create custom visualizations with different color palettes
   - Generate a PDF report summarizing findings

## Tips for Success

- Use descriptive comments to guide Copilot
- Leverage @workspace commands for context
- Try @vis for visualization-specific suggestions
- Use @stats for statistical analysis help
- Experiment with @dataset for recommendations

## Next Steps

- Explore different datasets
- Try advanced visualization libraries
- Create custom analysis functions
- Share your visualizations

## Additional Resources

- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Seaborn gallery](https://seaborn.pydata.org/examples/index.html)

