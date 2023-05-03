from flask import Flask, jsonify, request
from datastore import ScheduleFileDataStore
import os

SCHEDULE_ROOT = os.environ.get('SCHEDULE_ROOT', './data')
SCHEDULE_PORT = os.environ.get('SCHEDULE_PORT', 9000)

app = Flask(__name__)
data_store = ScheduleFileDataStore(SCHEDULE_ROOT)


@app.route('/schedule', methods=['POST'])
def add_schedule():
    data = request.get_json()
    date_str = data['date']
    title = data['title']
    schedule = data['schedule']
    data_store.save_schedule(date_str, title, schedule)
    return 'Schedule saved successfully\n'

@app.route('/schedule', methods=['GET'])
def get_schedule():
    try:
        start_str = request.args.get('start')
        end_str = request.args.get('end')
        if start_str and end_str:
            result = data_store.get_schedule(start_str, end_str)
            return jsonify(result)
        else:
            return 'Please provide start and end dates\n'
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SCHEDULE_PORT)
