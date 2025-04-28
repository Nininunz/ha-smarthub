const lines = msg.payload.split('\n');

// Find the header line with field names
let headerIndex = lines.findIndex(line => line.includes('_start') && line.includes('_stop'));
if (headerIndex === -1) {
    node.error("Could not find header with _start and _stop");
    return null;
}

const headers = lines[headerIndex].split(',');

// Find the indexes of _start and _stop
const startIndex = headers.indexOf('_start');
const stopIndex = headers.indexOf('_stop');

// Sort and reverse so we can splice safely
const removeIndexes = [startIndex, stopIndex].filter(i => i !== -1).sort((a, b) => b - a);

// Remove the columns from all rows
const cleaned = lines.map((line, index) => {
    const cols = line.split(',');

    removeIndexes.forEach(i => {
        if (i < cols.length) cols.splice(i, 1);
    });

    return cols.join(',');
});

msg.payload = cleaned.join('\n');
return msg;
