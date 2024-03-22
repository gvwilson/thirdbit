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
    if (list.childElementCount > 0) {
      section.appendChild(list)
    }
  })
}

const fixSidenotes = () => {
  Array.from(document.querySelectorAll('section')).forEach((section, i) => {
    Array.from(section.querySelectorAll('span.sidenote')).forEach((span, j) => {
      counter = document.createElement("span")
      counter.textContent = `${j+1}) `
      span.insertBefore(counter, span.firstChild)
      const marker = document.createElement("sup")
      marker.textContent = `${j+1}`
      span.parentNode.insertBefore(marker, span)
    })
  })
}

const fixPage = () => {
  fixToc()
  fixFootnotes()
  fixSidenotes()
}
