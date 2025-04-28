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
  - **electric-usage-downloader:** Configure your settings as explained [here](https://github.com/tedpearson/electric-usage-downloader#config) under config.
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


## Data Usage

At this point, you can view the data directly using an InfluxDB graphical interface.
Alternatively, you can integrate the data into Home Assistant either:
  - Via REST APIs (for advanced users), or
  - Through Node-RED, which is more modular and widely used in Home Assistant setups.

Using Node-RED is recommended for flexibility and easier future adjustments.




## Limitations: 
PEC aggregates usage data in 15-minute intervals, which becomes available the following day; _this could vary depending on your provider_. The data, covering the full period from 00:00 to 23:59 of the previous day, is uploaded all at once and typically updated sometime after 06:00. This script is scheduled to run daily at 08:00 to allow sufficient time for data availability and successful scraping.

Home Assistant’s InfluxDB integration is designed primarily for exporting data to the database, not importing from it. As a result, a different method is needed to bring external data into Home Assistant.

Currently, Home Assistant does not support backdating imported data to align with the original timestamps. This means the Energy dashboard will display an entire day's usage as a single block at the time the data is received, rather than spreading it across the day by hour.

Effectively, you will only be able to view daily total usage, not detailed hourly breakdowns. Additionally, because the data is delayed by one day, the usage shown for a given day will actually correspond to the previous day’s consumption.
