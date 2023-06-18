<p align="center">
    <h1 align="center">Markdown to Web</h1>
    <p align="center">
        <a href="https://codeclimate.com/github/arichr/md2web/maintainability"><img src="https://api.codeclimate.com/v1/badges/f54cb532f29a1392899b/maintainability" alt="CodeClimate maintainability" /></a>
        <br />
        Flask server for rendering Markdown files.
    </p>
</p>

**Features:**

* Light
* Easy to use
* Caches results via [flask-caching](https://github.com/pallets-eco/flask-caching)

## Getting started

```bash
python server.py
```

| Environment variable | Type | Description |
|----------------------|:----:|-------------|
| `MD_ROOT`            | Path | Absolute or relative path to a root folder |
| `MD_CACHE_TIMEOUT`   | Seconds (Positive integer) | Cache expiry timeout. "Disable" cache - `1`. |

## Enabled extensions

**External:**

* [Automatic header demoting](https://github.com/SaschaCowley/Markdown-Headdown)

**Built-in:**

* [Admonitions](https://python-markdown.github.io/extensions/admonition/)
* [CodeHilite (Code highlighting)](https://python-markdown.github.io/extensions/code_hilite/)
* [Definition list](https://python-markdown.github.io/extensions/definition_lists/)
* [Fenced code blocks](https://python-markdown.github.io/extensions/fenced_code_blocks/)
* [Meta-Data](https://python-markdown.github.io/extensions/meta_data/)
* [New Line to Break](https://python-markdown.github.io/extensions/nl2br/)
* [Tables](https://python-markdown.github.io/extensions/tables/)
* [TOC (Table of Contents)](https://python-markdown.github.io/extensions/toc/)
* [Sane lists](https://python-markdown.github.io/extensions/sane_lists/)
