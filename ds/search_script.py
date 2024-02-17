import csv
import requests
import json

def get_information_from_google_api(query):
    api_key = 'AIzaSyCiDvZA4z_HvbA9JX1BpeG2bMqT4yvUg9A'
    cx = '05d1d84f4aa4045f2'

    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        items = data.get('items', [])

        information = {}
        for item in items:
            title = item.get('title', '')
            snippet = item.get('snippet', '')
            information[title] = snippet

        print(f"Query: {query}")
        print(f"Information: {information}")
        return information
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return {}

def get_competitors_info(query):
    competitors_info = get_information_from_google_api(query)
    return competitors_info

def get_market_trends(query):
    market_trends_info = get_information_from_google_api(query)
    return market_trends_info

def get_financial_performance(ticker):
    financial_query = f'{ticker} financial performance'
    financial_info = get_information_from_google_api(financial_query)
    return financial_info

def save_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)

        # Write headers
        writer.writerow(["Category", "Information"])

        # Write data in a structured format
        for category, info in data.items():
            writer.writerow([category, str(info)])

def main():
    ticker_symbol = 'GOEV'

    industry_query = 'Canoo industry'
    industry_info = get_information_from_google_api(industry_query)

    competitors_query = 'Canoo competitors'
    competitors_info = get_competitors_info(competitors_query)

    market_trends_query = 'Automotive industry trends'
    market_trends_info = get_market_trends(market_trends_query)

    financial_info = get_financial_performance(ticker_symbol)

    save_to_csv({
        "Industry Information": industry_info,
        "Competitors Information": competitors_info,
        "Market Trends Information": market_trends_info,
        "Financial Performance Information": financial_info
    }, 'canoo_information.csv')

if __name__ == '__main__':
    main()
