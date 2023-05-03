## This project is a simple scheduler server created using Flask.

### HOW TO USE
```bash
virtualenv ./venv
source ./venv/bin/activate
pip install -r requirements.txt

# run server
cd server
python ./app.py
```

```bash
# test using shell scripts
cd client/test_scripts
post.sh
get.sh
```

```bash
# test using python scripts
cd client
python ./client.py http://localhost:9000 [GET,POST] ...
```
