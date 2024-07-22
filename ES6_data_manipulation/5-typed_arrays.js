export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const Int8 = new Int8Array(buffer);

  if (position < length) {
    Int8[position] = value;
  }
  else {
    throw new Error("Position outside range");
  }
  return buffer;
}
