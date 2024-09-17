const fs = require('fs/promises');

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');

    const lines = data.split('\n').filter(line => line.trim() !== '');

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
    let result = `Number of students: ${totalStudents}\n`;

    for (const field in studentsByField) {
      const studentList = studentsByField[field];
      result += `Number of students in ${field}: ${studentList.length}. List: ${studentList.join(', ')}\n`;
    }
    console.log(result);
    return result;

  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
