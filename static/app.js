'use strict'
const themeToggle = document.getElementById('theme-toggle')
const annotationListEls = Array.from(document.querySelectorAll('div.highlight + ol > li'))

themeToggle.addEventListener('click', () => {
    themeToggle.classList.toggle('animate')
    document.body.classList.toggle('dark')
    document.body.classList.toggle('light')
    setTimeout(() => {
        themeToggle.classList.toggle('animate')
    }, 210)
})

for (const listEl of annotationListEls) {
    const annotationID = annotationListEls.indexOf(listEl) + 1
    const codeEl = listEl.parentElement.previousElementSibling

    for (const commentEl of codeEl.querySelectorAll('.c, .c1, .cm')) {
        const annotationText = `(${annotationID})`

        if (commentEl.innerHTML.includes(annotationText)) {
            listEl.id = `codenate-${annotationID}`
            listEl.classList.remove('hidden')

            commentEl.innerHTML = commentEl.innerHTML.replaceAll(
                annotationText,
                `<a class="codenate-handler" href="#codenate-${annotationID}">${annotationID}</a>`
            )
        } else {
            listEl.classList.add('hidden')
        }
    }
}
