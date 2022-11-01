# Data Project 1
#### **This code was written and tested using Windows 10**
## Required Libraries 
Below are a couple of libraries you'll need to make this program work well. 
```bash
pip pip install beautifulsoup4
pip install lxml
pip install requests
pip install pandas
pip install urllib
```
## Getting started
Once you downloaded the required libraries all you need to do is run arxiv_api_tools.py
```bash
cd Data_Project_1
python arxiv_api_tools.py
```

This program uses the arxiv api to select n many papers of x topic. If there are no papers on your input topic you'll get an empty list. Otherwise you'll be able ot see the saved results locally. 

You'll be able to save your results as a Json, CSV, or SQLite Database. 

### Sample input
```text
What topic do you want to search? machine learning
How many results do you want? 10
What do you want as an output? type: sql, csv, or json) json
This json file is 10 by 7: 
```
You'll then see a file called machine_learning.json