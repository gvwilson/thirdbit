const values = [0, 1, '', 'text', undefined, null, [], [2, 3]];
for (const val of values) {
    const type = typeof val;
    if (val) {
        console.log(`val '${val}' of type ${type} seems true`);
    } else {
        console.log(`val '${val}' of type ${type} seems false`);
    }
}
