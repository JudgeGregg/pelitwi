#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = "Gregg Judge"
SITENAME = "Test Pelican"
SITEURL = "https://judgegregg.github.io/pelitwi"

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Twisted Customisation
DISPLAY_PAGES_ON_MENU = False

PREV_PAGE_TEMPLATE = """
<h4>Previous topic</h4>
<p class="topless">
<a href={}>{}</a>
</p>"""
NEXT_PAGE_TEMPLATE = """
<h4>Next topic</h4>
<p class="topless">
<a href={}>{}</a>
</p>"""
NAVBAR_LINK_TEMPLATE = """
<li><a href="{}">{}</a></li>
"""


def get_relative_pages(pages, page):
    prev_page = next_page = None
    pages_dict = {}
    for elem in pages:
        pages_dict[elem.slug] = elem

    if hasattr(page, "prev_page_slug"):
        prev_page = pages_dict[page.prev_page_slug]
    if hasattr(page, "next_page_slug"):
        next_page = pages_dict[page.next_page_slug]
    if prev_page:
        prev_page = PREV_PAGE_TEMPLATE.format(
            SITEURL + "/" + prev_page.url, prev_page.title
        )
    if next_page:
        next_page = NEXT_PAGE_TEMPLATE.format(
            SITEURL + "/" + next_page.url, next_page.title
        )
    result = ""
    if prev_page:
        result = result + prev_page
    if next_page:
        result = result + next_page
    return result


def get_navbar_link(pages, page):
    page_dict = {}
    for elem in pages:
        page_dict[elem.slug] = elem
    page_to_link = page_dict.get(page.navbar_link)
    if page_to_link:
        return NAVBAR_LINK_TEMPLATE.format(
            SITEURL + "/" + page_to_link.url, page_to_link.title
        )


JINJA_FILTERS = {
    "get_relative_pages": get_relative_pages,
    "get_navbar_link": get_navbar_link,
}
PLUGINS = ["extract_toc"]

# Dev conf FIXME
# SITEURL = "http://localhost:8000"
