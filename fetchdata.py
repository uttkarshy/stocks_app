import requests

# Define API endpoint and parameters
url = "https://query1.finance.yahoo.com/v10/finance/quoteSummary/aapl?modules=earningsHistory"
api_key ="0e113729cf8c198a0479e74b65d8148a8c9af69f682f43aaf3c3f605450e3bdb"
params = {
    "earningsHistory": "History",
    #"limit": "10"  # 5 years of data (365 days/year * 5 years)
}

# Send request to API and get response
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    # Save response content to a file in XML format
    with open(r"C:\Users\uttka\Desktop\stocks\app\fetchdata.json", "wb") as file:
        file.write(response.content)
        print("Data saved successfully.")
else:
    print("Request failed with status code:", response.status_code)
