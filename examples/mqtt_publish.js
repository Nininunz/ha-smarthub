msg.topic = "homeassistant/sensor/daily_grid_energy/state";
msg.payload = msg.payload.total_daily_energy_kwh;
msg.qos = 0;
msg.retain = true;  // important for energy sensors

return msg;
