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

Edit docker-compose.yaml with your variables:

  For electric-usage-downloader section: better explained [here](https://github.com/tedpearson/electric-usage-downloader#config) under config
  For ha-smarthub section, it's pretty self explanatory. Just enter your mqtt host credentials.

```
nano docker-compose.yaml
```

Create and run container
```
docker compose -f docker-compose.yml up -d
```

you can stop here and just view the data in influxdb graphical interface. you can also integrate the data via rest rather than continuing with node-red. although i think more will be comfortable with node-red since its already a key part of many peoples installs. not to mention its added modularity and ease of chnging course
