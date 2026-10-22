// SKILLS7: run the page's own ZIP code on the page's own data and print the ZIP as base64.
// Usage: node verify_zip.js <skill>/index.html
// The page may embed its own template as a file, so the real code is the LAST ZIP block.
'use strict';
const fs = require('fs');
const html = fs.readFileSync(process.argv[2], 'utf8');
const data = html.match(/<script type="application\/json" id="skill-data">([\s\S]*?)<\/script>/);
const start = html.lastIndexOf('/*ZIP:start*/'), end = html.lastIndexOf('/*ZIP:end*/');
if (!data || start < 0 || end < start) { console.error('markers not found'); process.exit(2); }
const D = JSON.parse(data[1]);
const z = new Function(html.slice(start + 13, end) + '\nreturn {makeZip, zipEntries};')();
const bytes = z.makeZip(z.zipEntries(D));
if (bytes.length !== D.zip.bytes) { console.error('ZIP size ' + bytes.length + ' != declared ' + D.zip.bytes); process.exit(3); }
process.stdout.write(Buffer.from(bytes).toString('base64'));
