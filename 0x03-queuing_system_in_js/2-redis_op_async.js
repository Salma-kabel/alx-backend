import redis from 'redis';
import util from 'util';
const client = redis.createClient();
client.on('error', (err) => console.log(`Redis client not connected to the server: ${err}`));
client.on('connect', () => {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

async function setNewSchool(schoolName, value) {
    try {
        await util.promisify(client.set).bind(client)(schoolName, value);
        console.log('Reply: OK');
    } catch (err) {
        console.error('Error setting value:', err);
    }
}

async function displaySchoolValue(schoolName) {
    const getAsync = util.promisify(client.get).bind(client);
    console.log(await getAsync(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
