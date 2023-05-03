import requests
import argparse
import json

parser = argparse.ArgumentParser(description='Schedule server client')
parser.add_argument('url', type=str, help='Server URL')
parser.add_argument('method', type=str, help='HTTP method')
parser.add_argument('--json', type=str, help='JSON data file path')
parser.add_argument('--start', type=str, help='Start date for GET method')
parser.add_argument('--end', type=str, help='End date for GET method')
args = parser.parse_args()

url = args.url
method = args.method
json_file_path = args.json
start_date = args.start
end_date = args.end

if method not in ['GET', 'POST']:
    print(f'Invalid method type: {method}')
    exit(1)

if method == 'POST' and not json_file_path:
    print('JSON file path is required for POST method')
    exit(1)

if method == 'GET' and not (start_date and end_date):
    print('Start and end dates are required for GET method')
    exit(1)

if method == 'POST':
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    res = requests.post(url+"/schedule", json=data)
    print(res.text)
else:
    params = {'start': start_date, 'end': end_date}
    res = requests.get(url+"/schedule", params=params)
    print(res.json())
