# pylint: disable=C0103,C0114,C0301,W0622

html_title = project = "Гайд по PrimLand"
copyright = "2023, stngularity"
author = "stngularity"

# -- General configuration ---------------------------------------------------
extensions = ["sphinxawesome_theme", "sphinx_design", "myst_parser"]
myst_enable_extensions = ["colon_fence", "attrs_block", "attrs_inline"]

templates_path = ["templates"]
exclude_patterns = []
source_suffix = [".md"]
master_doc = "index"

language = "ru"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinxawesome_theme"
pygments_style = "one-dark"
html_static_path = ["static"]

html_theme_options = {
    "show_prev_next": True,
    "extra_header_link_icons": {
        "Websites": {
            "icon": "<svg fill='currentColor' xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'><path d='M12 2C6.486 2 2 6.486 2 12s4.486 10 10 10 10-4.486 10-10S17.514 2 12 2zm7.931 9h-2.764a14.67 14.67 0 0 0-1.792-6.243A8.013 8.013 0 0 1 19.931 11zM12.53 4.027c1.035 1.364 2.427 3.78 2.627 6.973H9.03c.139-2.596.994-5.028 2.451-6.974.172-.01.344-.026.519-.026.179 0 .354.016.53.027zm-3.842.7C7.704 6.618 7.136 8.762 7.03 11H4.069a8.013 8.013 0 0 1 4.619-6.273zM4.069 13h2.974c.136 2.379.665 4.478 1.556 6.23A8.01 8.01 0 0 1 4.069 13zm7.381 6.973C10.049 18.275 9.222 15.896 9.041 13h6.113c-.208 2.773-1.117 5.196-2.603 6.972-.182.012-.364.028-.551.028-.186 0-.367-.016-.55-.027zm4.011-.772c.955-1.794 1.538-3.901 1.691-6.201h2.778a8.005 8.005 0 0 1-4.469 6.201z'></path></svg>",
            "link": "https://primland.fun"
        }
    },
    "main_nav_links": {
        "Сайт": "https://primland.fun",
        "Магазин": "https://shop.primland.fun"
    },
    "awesome_external_links": True
}

html_css_files = ["css/main.css"]
html_favicon = "static/images/favicon.png"
html_sidebars = {"**": ["sidebar_main_nav_links.html", "sidebar_toc.html"]}
