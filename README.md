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
```
nano docker-compose.yaml
```

Create and run container
```
docker compose -f docker-compose.yml up -d
```
