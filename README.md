# md2web
Flask server to render Markdown files.
# Why?
I need a small server to serve my Markdown files, but using frameworks is too complicated for this task.
# Features
 * Light
 * Easy to use
 * Caches results (see [Flask-Caching docs](https://flask-caching.readthedocs.io/en/latest/index.html))
 * Built on top of [python-markdown](https://python-markdown.github.io)
# Enabled extensions
External:

* [Automatic header demoting](https://github.com/SaschaCowley/Markdown-Headdown)

Internal:

* [Admonitions](https://python-markdown.github.io/extensions/admonition/)
* [CodeHilite (Code highlighting)](https://python-markdown.github.io/extensions/code_hilite/)
* [Definition list](https://python-markdown.github.io/extensions/definition_lists/)
* [Fenced code blocks](https://python-markdown.github.io/extensions/fenced_code_blocks/)
* [Meta-Data](https://python-markdown.github.io/extensions/meta_data/)
* [New Line to Break](https://python-markdown.github.io/extensions/nl2br/)
* [Tables](https://python-markdown.github.io/extensions/tables/)
* [TOC (Table of Contents)](https://python-markdown.github.io/extensions/toc/)
* [Sane lists](https://python-markdown.github.io/extensions/sane_lists/)
