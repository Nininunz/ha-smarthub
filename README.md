# ha-smarthub
Import SmartHub usage dumps into InfluxDB and integrate into HomeAssistant

Build:
```
git clone https://github.com/Nininunz/ha-smarthub.git/
```
```
cd ha-smarthub
```

Download electric-usage-downloader (current latest 2.3.2, future updates may break this script)
```
curl -L -o electric-usage-downloader https://github.com/tedpearson/electric-usage-downloader/releases/download/v2.3.2/electric-usage-downloader-linux-amd64
```
```
git clone https://github.com/Nininunz/ha-smarthub.git/
```

```
docker build -t ha-smarthub .
```

Edit compose file with your shit
```
nano docker-compose.yaml
```
