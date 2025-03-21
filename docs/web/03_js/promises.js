const middle = Deno.readTextFile('middle.txt');
console.log(`middle is ${middle}`);
middle.then(value => {
    console.log(`middle.then is ${value}`);
});
