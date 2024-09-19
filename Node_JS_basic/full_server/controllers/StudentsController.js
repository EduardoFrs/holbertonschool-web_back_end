const { readDatabase } = require('../utils');

class StudentsController {
    static async getAllStudents(req, res) {
        try {
            const filePath = req.databaseFilePath;
            const studentsData = await readDatabase(filePath);
            let response = 'This is the list of our students\n';
            const fields = Object.keys(studentsData).sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
            fields.forEach(field => {
                const names = studentsData[field].join(', ');
                response += `Number of students in ${field}: ${studentsData[field].length}. List: ${names}\n`;
            });

            res.status(200).send(response);

        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
    static async getAllStudentsByMajor(req, res) {
        const major = req.param.major;

        if (major !== 'CS' && major !== 'SWE') {
            res.status(500).send('Major parameter must be CS or SWE');
            return;
        }

        try {
            const filePath = req.databaseFilePath;
            const studentsData = await readDatabase(filePath);
            const nameList = studentsData[major].join(', ');
            const response = `List: ${nameList}`;
            res.status(200).send(response);

        } catch (error) {
            res.status(500).send('Cannot load the database');
        }
    }
}

module.exports = StudentsController;