function limits (values) {
  if (!values.length) {
    return [undefined, undefined];
  }
  let low = values[0];
  let high = values[0];
  for (let v of values) {
    if (v < low) {
        low = v;
    }
    if (v > high) {
        high = v;
    }
  }
  return [low, high]
}

const result = limits([1, -3, 2, 7]);
console.log(result);
