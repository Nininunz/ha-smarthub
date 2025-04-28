const lines = msg.payload.trim().split('\n');
const headers = lines.shift().split(',').map(h => h.trim());

const valueIndex = headers.indexOf('_value');
if (valueIndex === -1) {
    node.error(`Missing "_value" column in headers: [${headers.join(', ')}]`);
    return null;
}

// Calculate sum
const sum = lines.reduce((total, line) => {
    const cols = line.split(',').map(c => c.trim());
    const value = parseFloat(cols[valueIndex]);
    return total + (isNaN(value) ? 0 : value);
}, 0);

// Convert watts to kilowatt-hours over 15-minute intervals
// (watts * 15 minutes) ÷ 60 (minutes per hour) ÷ 1000 (watts per kilowatt)
const total_kwh = (sum * 15) / 60 / 1000;

msg.payload = {
    total_daily_energy_kwh: parseFloat(total_kwh.toFixed(3))
};

return msg;
