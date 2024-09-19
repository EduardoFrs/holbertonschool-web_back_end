const fs = require('fs/promises');
const path = require('path');

async function readDatabase(filePath) {
    try {
        const data = await fs.readFile(filePath, 'utf-8')
        const parsedData = JSON.parse(data);
        const result = {};
        parsedData.forEach(student => {
            if (!result[student.field]) {
                result[student.field] = [];
            }
            result[student.field].push(student.firstname);
        });

        return result;
    } catch (error) {
        return Promise.reject(error);
    }
}

module.exports = { readDatabase };