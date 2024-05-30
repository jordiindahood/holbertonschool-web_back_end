export default function cleanSet(set, Str) {
  if (Str === '' || typeof Str !== 'string') {
    return '';
  }
  const result = [];
  set.forEach((value) => {
    if (value.startsWith(Str)) {
      result.push(value.slice(Str.length));
    }
  });
  return result.join('-');
}
