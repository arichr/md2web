"""Flask server for Markdown rendering."""
import os
from pathlib import Path

import markdown
from flask import Flask, render_template
from flask_caching import Cache

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

root_path = Path(os.environ.get('MD_ROOT', 'content')).resolve(strict=True)
cache_timeout = int(os.environ.get('MD_CACHE_TIMEOUT', 600))

md = markdown.Markdown(
    extensions=(
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.def_list',
        'markdown.extensions.fenced_code',
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.tables',
        'markdown.extensions.toc',
        'markdown.extensions.sane_lists',
        'mdx_headdown',
    ),
    extension_configs={
        'markdown.extensions.codehilite': {
            'linenums': False,
            'css_class': 'highlight',
        },
    },
    output_format='html',
)


@app.route('/<path:path>')
@cache.cached(timeout=cache_timeout)
def render_md(path: str):
    """Render a requested Markdown file.

    Args:
        path (str): Relative path to a file

    Returns:
        str: Rendered HTML
    """
    requested_path = (root_path / path).resolve()

    if requested_path.is_relative_to(root_path):
        if requested_path.is_dir():
            requested_path = requested_path / 'index.md'

        if requested_path.is_file():
            html = md.convert(requested_path.read_text('UTF-8'))
            title = md.Meta.get('title', [requested_path.name])[-1]  # pylint: disable=no-member
            return render_template('markdown.html', title=title, markdown=html)

    return (
        render_template('markdown.html', title='404', error='Unable to find the requested file.'),
        404,
    )


@app.route('/')
def index():
    """Render `index.md`.

    Returns:
        str: Rendered HTML
    """
    return render_md('index.md')


if __name__ == '__main__':
    app.run()
