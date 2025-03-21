const largest = (left, right) => {
    if (left < right) {
        return left;
    } else {
        return right;
    }
}

console.log(`largest(3, 5) is ${largest(3, 5)}`);
