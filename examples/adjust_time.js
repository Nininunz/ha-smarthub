const lines = msg.payload.split('\n');

// Find the header row that contains "_time"
let headerIndex = lines.findIndex(line => line.includes('_time'));
if (headerIndex === -1) {
    msg.payload = { total_daily_energy_kwh: 0 };
    return [null, msg];  // Send to output 2
}

const headers = lines[headerIndex].split(',');
const timeIndex = headers.indexOf('_time');

// Adjust each row
let adjusted = lines.map((line, index) => {
    if (index <= headerIndex) return line; // Keep header and metadata as-is

    const cols = line.split(',');
    if (cols.length <= timeIndex) return line; // Skip malformed lines

    try {
        const utcDate = new Date(cols[timeIndex]);
        // Apply UTC-5 offset manually
        const offsetMillis = 5 * 60 * 60 * 1000;
        const localDate = new Date(utcDate.getTime() - offsetMillis);

        // Format to readable string (optional)
        cols[timeIndex] = localDate.toISOString().replace('T', ' ').replace('Z', '');
    } catch (e) {
        // Leave line unchanged if error
    }

    return cols.join(',');
});

msg.payload = adjusted.join('\n');
return msg;
