const values = [1, -3, 5, -7];

const is_positive = values.map(v => v >= 0);
console.log(`is_positive: ${is_positive}`);

const keep_positive = values.filter(v => v >= 0);
console.log(`keep_positive: ${keep_positive}`);

const print_positive = values.forEach(v => {
    if (v >= 0) {
        console.log(v);
    }
});
