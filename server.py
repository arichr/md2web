"""Flask server for Markdown rendering."""
import os
from pathlib import Path

import markdown
from flask import Flask, render_template
from flask_caching import Cache
from pymdownx.emoji import twemoji

app = Flask(__name__)

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
cache.init_app(app)

root_path = Path(os.environ.get('MD_ROOT', 'content')).resolve(strict=True)
cache_timeout = int(os.environ.get('MD_CACHE_TIMEOUT', 600))

md = markdown.Markdown(
    extensions=(
        'markdown.extensions.meta',
        'markdown.extensions.toc',
        'pymdownx.extra',
        'pymdownx.inlinehilite',
        'pymdownx.superfences',
        'pymdownx.magiclink',
        'pymdownx.keys',
        'pymdownx.emoji',
        'pymdownx.tasklist',
        'pymdownx.details',
        'pymdownx.tabbed',
        'pymdownx.highlight',
    ),
    extension_configs={
        'pymdownx.emoji': {'emoji_index': twemoji},
        'pymdownx.tabbed': {'alternate_style': True},
        'pymdownx.highlight': {'anchor_linenums': True, 'pygments_lang_class': True},
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
        # An iterable of path parts to the parent
        raw_path = requested_path.relative_to(root_path).parts[:-1]
        title = requested_path.name

        if requested_path.is_dir():
            requested_path = requested_path / 'index.md'

        if requested_path.is_file():
            md.reset()
            html = md.convert(requested_path.read_text('UTF-8'))
            if 'title' in md.Meta:  # pylint: disable=no-member
                title = md.Meta['title'][0]  # pylint: disable=no-member

            return render_template(
                'markdown.html',
                raw_path=raw_path,
                path=tuple(enumerate(raw_path)),
                title=title,
                toc=md.toc,  # pylint: disable=no-member
                markdown=html,
            )

    return render_template('markdown.html', error='Unable to find the requested file.'), 404


@app.route('/')
def index():
    """Render `index.md`.

    Returns:
        str: Rendered HTML
    """
    return render_md('index.md')


if __name__ == '__main__':
    app.run()
