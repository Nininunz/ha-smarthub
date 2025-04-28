# ha-smarthub
Import SmartHub usage dumps into InfluxDB and integrate into HomeAssistant

Build:
```
git clone https://github.com/Nininunz/ha-smarthub.git/
```
```
cd ha-smarthub
```

Build image
```
docker build -t ha-smarthub .
```

Edit compose file with your shit
better explained here https://github.com/tedpearson/electric-usage-downloader#Config

EXTRACT_DAYS=10 # number of days to retrieve data

SMARTHUB_API_URL=https://api.smarthub.coop # provider specific url for smarthub portal
SMARTHUB_USERNAME=myusername # username used to sign into smarthub portal
SMARTHUB_PASSWORD=mypassword # password used to sign into smarthub portal
SMARTHUB_ACCOUNT=123456 # account number found on portal and top of bill
SMARTHUB_SERVICE_LOCATION=12345678 # must be retrieved from browser
SMARTHUB_TIMEZONE=America/Chicago # must match utility provider
INFLUXDB_HOST=influxdb.local # ip of your influxdb instance
INFLUXDB_AUTH_TOKEN=mytoken # influxdb token
INFLUXDB_ORG=myorg # influxdb org
INFLUXDB_DATABASE=power_meter # influxdb bucket
INFLUXDB_INSECURE=false # allows connecting to server with certificate issues
```
nano docker-compose.yaml
```

Create and run container
```
docker compose -f docker-compose.yml up -d
```

you can stop here and just view the data in influxdb graphical interface. you can also integrate the data via rest rather than continuing with node-red. although i think more will be comfortable with node-red since its already a key part of many peoples installs. not to mention its added modularity and ease of chnging course
