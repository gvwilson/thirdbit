const fs = require('fs')
const acorn = require('acorn')

const recurse = (accum, node) => {
  if (node && (typeof node === 'object') && ('type' in node)) {
    if (! accum.get(node.type)) {
      accum.set(node.type, 0)
    }
    accum.set(node.type, accum.get(node.type) + 1)

    for (const key in node) {
      if (Array.isArray(node[key])) {
	node[key].forEach(child => recurse(accum, child))
      } else if (typeof node[key] === 'object') {
        recurse(accum, node[key])
      }
    }
  }
}

const handle = (accum, filename) => {
  try {
    const text = fs.readFileSync(filename, 'utf8')
    const ast = acorn.parse(text, {sourceType: 'module'})
    recurse(accum, ast)
  }
  catch (e) {
  }
}

const result = new Map()
process.argv.slice(2).forEach(f => handle(result, f))

let total = 0
for (const [key, value] of result) {
  total += value
}

console.log(`kind,count,percentage`)
for (const [key, value] of result) {
  console.log(`${key},${value},${100*value/total}`)
}
