# Teste de WR

```bash
$ git clone https://github.com/marcus-campos/python-vs-mongodb-rw
$ docker-compose up -d
$ docker exec -it mongo0 mongo
$ config={"_id":"rs0","members":[{"_id":0,"host":"mongo0:27017"},{"_id":1,"host":"mongo1:27017"},{"_id":2,"host":"mongo2:27017"},{"_id":3,"host":"mongo3:27017"}]}
$ rs.status() # Check primary
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ rs.initiate(config)
$ python startup.py