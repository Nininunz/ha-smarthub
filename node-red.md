# Node-RED

## Node-RED Flow Example
<img width="908" alt="Screenshot 2025-04-28 at 3 04 35 PM" src="https://github.com/user-attachments/assets/e63de26b-a10d-4a42-98b7-bb0531fac7de" />
<br />
<br />

**Manual Trigger (Inject Node)**
* Lets you manually start the flow anytime for testing.

**Downloader/Status (MQTT In Node)**
* Listens for MQTT messages on the topic downloader/status to automatically trigger the flow.

**Fail/Success Split (Switch Node)**
* If message payload is success → continue the process.
* If message payload is fail → trigger failure handling.

**Build Flux Query (Function Node)** [Example](https://github.com/Nininunz/ha-smarthub/blob/main/examples/build_query.js)
* Builds a Flux query dynamically to fetch yesterday's adjusted UTC to today's adjusted UTC data from InfluxDB.

**InfluxDB Fail (Home Assistant Service Call Node)**
* Sends a push notification if a failure is detected before or during querying InfluxDB.

**Send to InfluxDB (HTTP Request Node)**
* Executes the Flux query against InfluxDB to retrieve the raw 15-minute interval data.

**Adjust Local Time (Function Node)** [Example](https://github.com/Nininunz/ha-smarthub/blob/main/examples/adjust_time.js)
* Adjusts timestamps from UTC to local time.

* Checks if the data is populated for the expected window.

* If data is missing, triggers the Yesterday Fail notification.

**Yesterday Fail (Home Assistant Service Call Node)**
* Sends a push notification that no usable data was found for yesterday.

**Strip (_start) & (_stop) (Function Node)**
* Removes unnecessary metadata fields (_start, _stop) from the InfluxDB response to simplify the dataset.

**Sum Daily Energy Usage (Function Node)**
* Sums all 15-minute interval watt readings.
* Converts the total into daily kWh usage.

**MQTT Publish (Function Node)**
* Prepares the payload and topic to publish the daily energy usage back over MQTT (for Home Assistant sensors).

**Success (Home Assistant Service Call Node)**
* Sends a push notification confirming that the daily usage was calculated and uploaded successfully.

**MQTT Out (MQTT Out Node)**
* Publishes the final daily kWh energy usage to MQTT, allowing Home Assistant (or any subscriber) to receive the data.

**Debug (Debug Node)**
* Outputs useful debug information to the Node-RED sidebar for troubleshooting during development.

