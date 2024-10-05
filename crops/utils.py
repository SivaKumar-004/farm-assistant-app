import requests

def get_disaster_alerts():
    response = requests.get('https://api.disaster-alerts.com/v1/alerts')  # Replace with the actual API URL
    if response.status_code == 200:
        alerts = response.json()
        return alerts
    else:
        return {'error': 'Failed to fetch data'}
