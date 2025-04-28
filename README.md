# ha-smarthub
Import SmartHub usage dumps into InfluxDB and integrate into HomeAssistant

## Build Instructions
Clone the repository
```
git clone https://github.com/Nininunz/ha-smarthub.git/
```
```
cd ha-smarthub
```
Build the Docker image:
```
docker build -t ha-smarthub .
```



## Configuration

Edit docker-compose.yml to match your environment:
  - **electric-usage-downloader:** Configure your settings as explained [here](https://github.com/tedpearson/electric-usage-downloader#config) under config
  - **mqtt:** Enter your MQTT broker address, username, and password.
  - **ha-smarthub:** Customize MQTT topic names and status messages. Defaults are safe if you're unsure.
  - **advanced:** Fine-tune scraping intervals and retry behavior. Defaults are conservatively set for reliability.


Edit the compose file:
```
nano docker-compose.yaml
```

Create and start the container:
```
docker compose -f docker-compose.yml up -d
```




you can stop here and just view the data in influxdb graphical interface. you can also integrate the data via rest rather than continuing with node-red. although i think more will be comfortable with node-red since its already a key part of many peoples installs. not to mention its added modularity and ease of chnging course

Limitations: 
PEC aggregates usage data in 15-minute intervals, which becomes available the following day. The data, covering the full period from 00:00 to 23:59 of the previous day, is uploaded all at once and typically updated sometime after 06:00. This script is scheduled to run daily at 08:00 to allow sufficient time for data availability and successful scraping.
