#!/usr/bin/env python3
"""
Convert safe HTML tags to Markdown in blog posts under src/.
Only converts patterns where the visual appearance won't change.

Safe conversions:
  <em>text</em>        -> *text*
  <strong>text</strong> -> **text**
  <code>text</code>     -> `text`
  <a href="url">text</a> -> [text](url)       (only if no other attributes)
  <img src="url" alt="text"> -> ![text](url)
  <br> / <br/>         -> hard line break
  <hr/>                -> ---
  <p>text</p>          -> text                (only if no attributes)
  <ul><li>...</li></ul> -> - ...              (only flat, no nested ul/ol)
  <ol><li>...</li></ol> -> 1. ...             (only flat, no nested ul/ol)
  <blockquote>...</blockquote> -> > text      (recursively converts inner content)

Preserved as-is:
  - <table>, <tr>, <td>, <th>
  - <div> with attributes
  - <p>, <li>, <a>, <blockquote> with attributes
  - Nested <ul>/<ol> inside <li>
  - <pre>
  - <h1>-<h6>
"""

import re
import sys
import os


def convert_html_to_md(content):
    """Convert safe HTML to Markdown. Returns (converted_content, was_changed)."""
    original = content

    # Split frontmatter from body
    parts = content.split('---', 2)
    if len(parts) >= 3 and parts[0].strip() == '':
        frontmatter = parts[1].strip()
        body = parts[2].strip()
        has_frontmatter = True
    else:
        frontmatter = ''
        body = content
        has_frontmatter = False

    def convert_inline(text):
        """Convert inline HTML elements to Markdown."""
        # <em>text</em> -> *text*
        text = re.sub(r'<em>(.*?)</em>', r'*\1*', text, flags=re.DOTALL)
        # <strong>text</strong> -> **text**
        text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text, flags=re.DOTALL)
        # <code>text</code> -> `text`
        text = re.sub(r'<code>(.*?)</code>', r'`\1`', text, flags=re.DOTALL)
        # <br> / <br/> -> hard line break
        text = re.sub(r'<br\s*/?>', '  \n', text)
        # <hr/> -> ---
        text = re.sub(r'<hr\s*/?>', '\n---\n', text)

        # <img src="url" alt="text"> -> ![text](url)
        def img_replace(m):
            src_match = re.search(r'src="([^"]*)"', m.group(0))
            alt_match = re.search(r'alt="([^"]*)"', m.group(0))
            src = src_match.group(1) if src_match else ''
            alt = alt_match.group(1) if alt_match else ''
            return f'![{alt}]({src})'
        text = re.sub(r'<img[^>]*/?>', img_replace, text)

        # <a href="url">text</a> -> [text](url) (only when href is sole attribute)
        def link_replace(m):
            attrs_str = m.group(1)
            inner_text = m.group(2)
            href_match = re.search(r'href="([^"]*)"', attrs_str)
            other_attrs = re.sub(r'href="[^"]*"', '', attrs_str).strip()
            if href_match and not other_attrs:
                return f'[{inner_text}]({href_match.group(1)})'
            return m.group(0)
        text = re.sub(r'<a\b([^>]*)>(.*?)</a>', link_replace, text, flags=re.DOTALL)

        return text

    def convert_lists(text):
        """Convert flat <ul>/<ol> lists to Markdown. Skip nested lists."""
        def ul_replace(m):
            inner = m.group(1)
            # Skip if contains nested ul/ol
            if re.search(r'<(ul|ol)\b', inner):
                return m.group(0)
            items = re.findall(r'<li>(.*?)</li>', inner, re.DOTALL)
            result = []
            for item in items:
                result.append('- ' + item.strip())
            return '\n'.join(result) + '\n'

        def ol_replace(m):
            inner = m.group(1)
            if re.search(r'<(ul|ol)\b', inner):
                return m.group(0)
            items = re.findall(r'<li>(.*?)</li>', inner, re.DOTALL)
            result = []
            for i, item in enumerate(items, 1):
                result.append(f'{i}. ' + item.strip())
            return '\n'.join(result) + '\n'

        text = re.sub(r'<ul>\s*(.*?)\s*</ul>', ul_replace, text, flags=re.DOTALL)
        text = re.sub(r'<ol>\s*(.*?)\s*</ol>', ol_replace, text, flags=re.DOTALL)
        return text

    def convert_paragraphs(text):
        """Convert plain <p> tags (no attributes) to paragraph text."""
        def p_replace(m):
            content = m.group(1).strip()
            lines = [line.strip() for line in content.split('\n')]
            return '\n'.join(lines) + '\n\n'
        text = re.sub(r'<p>(.*?)</p>', p_replace, text, flags=re.DOTALL)
        return text

    def convert_blockquotes(text):
        """Convert <blockquote>, recursively converting inner content first."""
        def replace_bq(m):
            inner = m.group(1).strip()
            inner = convert_inline(inner)
            inner = convert_paragraphs(inner)
            inner = convert_lists(inner)
            lines = inner.split('\n')
            result = []
            for line in lines:
                stripped = line.strip()
                if stripped:
                    result.append('> ' + stripped)
                else:
                    result.append('>')
            # Collapse consecutive empty blockquote lines to a single empty line
            joined = '\n'.join(result)
            joined = re.sub(r'(>\n)+(?=>)', '>\n', joined)
            return joined

        text = re.sub(r'<blockquote>\s*(.*?)\s*</blockquote>',
                      replace_bq, text, flags=re.DOTALL)
        return text

    # Convert in order: inline -> blockquotes (recursive) -> lists -> paragraphs
    body = convert_inline(body)
    body = convert_blockquotes(body)
    body = convert_lists(body)
    body = convert_paragraphs(body)

    # Clean up whitespace
    body = re.sub(r'\n{3,}', '\n\n', body)
    body = re.sub(r'[ \t]+$', '', body, flags=re.MULTILINE)
    body = body.strip() + '\n'

    if has_frontmatter:
        result = f'---\n{frontmatter}\n---\n{body}'
    else:
        result = body

    return result, result != original


def process_file(filepath):
    """Process a single file. Returns True if changed."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    result, changed = convert_html_to_md(content)

    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)

    return changed


def main(md_files):
    total = len(md_files)
    changed = 0
    errors = 0

    for i, filepath in enumerate(sorted(md_files)):
        try:
            if process_file(filepath):
                changed += 1
        except Exception as e:
            errors += 1
            print(f'  Error: {filepath}: {e}', file=sys.stderr)


if __name__ == '__main__':
    main(sys.argv[1:])
