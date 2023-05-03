#/bin/bash

PORT=9000

curl -X POST -H "Content-Type: application/json" \
    -d '{"date": "2023-06-01", "title": "test title1", "schedule": "test schedule1"}' \
    http://localhost:$PORT/schedule


curl -X POST -H "Content-Type: application/json" \
    -d '{"date": "2023-06-01", "title": "test title2", "schedule": "test schedule2"}' \
    http://localhost:$PORT/schedule


curl -X POST -H "Content-Type: application/json" \
    -d '{"date": "2023-06-02", "title": "test title1", "schedule": "test schedule1"}' \
    http://localhost:$PORT/schedule