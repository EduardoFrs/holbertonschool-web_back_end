export default function getListStudentIds(arrayStudents) {
  if (!Array.isArray(arrayStudents)) {
    return [];
  }
  return arrayStudents.map((arrayStudents) => arrayStudents.id);
}
