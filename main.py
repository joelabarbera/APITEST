import requests

API_KEY = 'xZRKCzf1nXn7QhhNSJs7WgAT8piOtjvp'

def prev_day_info(ticker):
    agg_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={API_KEY}'
    agg_response = requests.get(agg_url)

    if agg_response.status_code == 200:
        agg_data = agg_response.json()
        result = agg_data['results'][0]
        info = (f"\nPrevious Close Data for {ticker}:\n"
                f"Open: {result['o']}\n"
                f"High: {result['h']}\n"
                f"Low: {result['l']}\n"
                f"Close: {result['c']}\n"
                f"Volume: {result['v']}\n")
        return info
    else:
        return f"Error fetching aggregates: {agg_response.status_code} {agg_response.text}"

def daily_returns(ticker):
    agg_url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/prev?adjusted=true&apiKey={API_KEY}'
    agg_response = requests.get(agg_url)

    if agg_response.status_code == 200:
        agg_data = agg_response.json()
        result = agg_data['results'][0]
        if result['o'] > result['h']:
            change = result['o'] - result['h']
            return f"Daily Change: -${change:.2f}"
        else:
            change = result['h'] - result['o']
            return f"Daily Change: +${change:.2f}"
    else:
        return f"Error fetching returns: 
