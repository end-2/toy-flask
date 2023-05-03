import os
import json
from datetime import datetime, timedelta

class ScheduleFileDataStore:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        if not os.path.exists(self.root_dir):
            os.makedirs(self.root_dir)

    def save_schedule(self, date_str, title, schedule):
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        filename = os.path.join(self.root_dir, f'{date_str}.json')
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                json.dump({}, f)
        with open(filename, 'r') as f:
            existing_data = json.load(f)
        existing_data[title] = schedule
        with open(filename, 'w') as f:
            json.dump(existing_data, f)

    def get_schedule(self, start_str, end_str):
        start = datetime.strptime(start_str, '%Y-%m-%d').date()
        end = datetime.strptime(end_str, '%Y-%m-%d').date()
        result = {}
        for date in self.daterange(start, end):
            filename = os.path.join(self.root_dir, f'{date.strftime("%Y-%m-%d")}.json')
            if not os.path.exists(filename):
                continue
            with open(filename, 'r') as f:
                data = json.load(f)
            for key in data:
                if key not in result:
                    result[key] = {}
                result[key][str(date)] = data[key]
        return result

    @staticmethod
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days) + 1):
            yield start_date + timedelta(n)