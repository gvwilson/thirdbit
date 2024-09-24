const fixToc = () => {
  const toc = document.querySelector('ol#toc')
  if (! toc) {
    return
  }
  Array.from(document.querySelectorAll('h2')).forEach((header, i) => {
    const label = `chapter.${i+1}`
    header.id = label
    const text = header.innerHTML
    const item = document.createElement('li')
    item.innerHTML = `<a href="#${label}">${text}</a>`
    toc.appendChild(item)
  })
}

const fixPage = () => {
  fixToc()
}
