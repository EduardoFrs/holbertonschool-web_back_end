const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');

    const lines = data.split('\n').filter(line => line.trim() !== '');

    if (lines.length <= 1) {
        return;
    }

    const studentsByField = {};

    lines.shift();

    lines.forEach(line => {
      const student = line.split(',');
      const field = student[3];
      const firstname = student[0];

      if (!studentsByField[field]) {
        studentsByField[field] = [];
      }
      studentsByField[field].push(firstname);
    });

    const totalStudents = Object.values(studentsByField).flat().length;
    console.log(`Number of students: ${totalStudents}`);

    for (const field in studentsByField) {
      const studentList = studentsByField[field];
      console.log(`Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}`);
    }
  } catch (err) {
    console.error('Cannot load the database');
  }
}

module.exports = countStudents;
