"""Flask server for Markdown rendering."""
from pathlib import Path

import markdown
from flask import Flask, render_template
from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})
app = Flask(__name__)
cache.init_app(app)

content_dir = Path('content')
md = markdown.Markdown(
    extensions=[
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
    ],
    extension_configs={
        'markdown.extensions.codehilite': {
            'linenums': False,
            'css_class': 'highlight',
        },
    },
    output_format='html',
)


@app.route('/')
@cache.cached(timeout=600)
def index():
    """Show index.md for /.

    Returns:
        The contents of index.md, styled by using Jinja2.
    """
    return show_md('index.md')


@app.route('/<path:path>')
@cache.cached(timeout=600)
def show_md(path: str):
    """Render a requested Markdown file.

    Args:
        path (str): Relative path to a file

    Returns:
        str: Rendered HTML
    """
    path_obj = content_dir / Path(path)
    if path.endswith('.md') and path_obj.is_relative_to(content_dir):
        if path_obj.exists():
            html = md.convert(path_obj.read_text('UTF-8'))
            title = md.Meta.get('title', [path_obj.name])[-1]
            return render_template('markdown.html', title=title, markdown=html)

    return render_template(
        'markdown.html',
        title='zZz...',
        error='Too lazy to read. <a href="/">Home page is better.</a>',
    )


if __name__ == '__main__':
    app.run()
