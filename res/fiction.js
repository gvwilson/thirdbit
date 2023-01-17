const fixToc = () => {
  const toc = document.querySelector('ol#toc')
  Array.from(document.querySelectorAll('h2')).forEach((header, i) => {
    const label = `chapter.${i+1}`
    header.id = label
    const text = header.innerHTML
    const item = document.createElement('li')
    item.innerHTML = `<a href="#${label}">${text}</a>`
    toc.appendChild(item)
  })
}

const fixFootnotes = () => {
  Array.from(document.querySelectorAll('section')).forEach((section, i) => {
    const list = document.createElement('ol')
    Array.from(section.querySelectorAll('sup')).forEach((sup, j) => {
      backref = `backref.${i+1}.${j+1}`
      footnote = `footnote.${i+1}.${j+1}`
      const text = sup.innerHTML
      sup.id = backref
      sup.innerHTML = `<a href="#${footnote}">${j+1}</a>`
      const item = document.createElement('li')
      item.id = footnote
      item.innerHTML = `${text} <a href="#${backref}">&#x21F1;</a>`
      list.appendChild(item)
    })
    section.appendChild(list)
  })
}

const fixPage = () => {
  fixToc()
  fixFootnotes()
}
