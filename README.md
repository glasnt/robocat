# robocat

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)

A simple wrapper around [robohash](https://github.com/e1ven/Robohash), in cat mode. 

Provides an interface to generate an [Identicon](https://en.wikipedia.org/wiki/Identicon), except it's a cat. 

### local testing


```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

```
open http://localhost:8080/robocat
```
![cat](testingcat.png)
