export default function getStudentIdsSum(students) {
  const sum = students.reduce((accumulator, studends) => accumulator + studends.id, 0);
  return sum;
}
