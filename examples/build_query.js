// Calculate yesterday 5am UTC to today 5am UTC
let now = new Date();

// Set anchor time at 5:00 AM UTC
const ANCHOR_UTC_HOUR = 5;

let endTime = new Date(Date.UTC(
    now.getUTCFullYear(),
    now.getUTCMonth(),
    now.getUTCDate(),
    ANCHOR_UTC_HOUR,
    0,
    0
));

let startTime = new Date(endTime);
startTime.setUTCDate(startTime.getUTCDate() - 1);

// Format as ISO strings
let startISO = startTime.toISOString();
let endISO = endTime.toISOString();

// Construct Flux query
msg.payload = `
option startTime = time(v: "${startISO}")
option endTime = time(v: "${endISO}")

from(bucket: "pec_meter")
  |> range(start: -7d)
  |> filter(fn: (r) => r._measurement == "electric" and r._field == "watts")
  |> filter(fn: (r) => r._time >= startTime and r._time < endTime)
  |> aggregateWindow(every: 15m, fn: mean, createEmpty: false)
  |> yield(name: "mean")
`;

return msg;
