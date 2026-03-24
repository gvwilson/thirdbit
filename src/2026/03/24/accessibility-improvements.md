---
title: "Accessibility Improvements"
date: 2026-03-24
---

I've made some improvements to the accessibility of
[*Distributed Systems Design by Example*][dsdx]
and the [JavaScript][sdxjs] and [Python][sdxpy] version of
*Software Design by Example*:

Link color contrast
:   Unvisited (`#0066ff`) and visited (`#0000ff`) link colors were nearly identical, and hover was the same as visited, giving users no visual feedback on link state.<br> Changed `--color-link-visited` to `#6600cc` (purple) — the conventional color for visited links — and added `text-decoration: underline` on hover.

Keyboard focus indicator
:   No `:focus` styles existed anywhere in the stylesheet, leaving keyboard and switch-device users with no visible indicator of the focused element.<br> Added `:focus-visible { outline: 2px solid var(--color-link-unvisited); outline-offset: 2px; }`.

Dark mode support
:   The entire color palette was hardcoded for light mode, giving users with a dark-mode OS preference a jarring white background.<br> Added a `@media (prefers-color-scheme: dark)` block overriding `--color-page`, `--color-highlight`, `--color-decorate`, `--color-text`, and both link colors. Also added two `<meta name="theme-color">` tags to the template for browser chrome tinting.

Active page indicator in nav
:   The nav dropdown had no visual indication of the current page.<br> Added `.dropdown-content a.active { font-weight: bold; text-decoration: underline; }`. The template and build context were updated to emit `class="active"` on the matching nav link (see template and build sections below).

Keyboard-inaccessible dropdowns
:   Nav dropdowns only opened on `:hover`, making them unreachable by keyboard.<br> Added `.dropdown:focus-within .dropdown-content { display: block; }` so dropdowns open when any descendant receives focus.

Justified table text
:   `table { text-align: justify; }` creates uneven word spacing harmful to readers with dyslexia (WCAG 1.4.8).<br> Changed to `text-align: left`.

Blockquote visual differentiation
:   The blockquote left border used color alone to convey meaning (WCAG 1.4.1). Padding was also absent top and bottom.<br> Added `padding-top`/`padding-bottom: var(--len-half)` and `font-style: italic` to provide a second non-color cue.

Callout/syllabus visual differentiation
:   `div.callout` and `div.syllabus` used only a background color to distinguish them from prose; background color alone fails WCAG 1.4.1.<br> Added `border-left: solid var(--len-thick) var(--color-decorate)` to both.

Figure caption alignment
:   `figure { text-align: center; }` cascaded to captions, making long caption text hard to read.<br> Added `figcaption { text-align: left; max-width: 90%; margin: 0 auto; }`.

Images overflow on narrow viewports
:   No base `max-width` rule on `img` meant images could overflow their containers on narrow screens.<br> Added `img { max-width: 100%; height: auto; }`.

Decorative border contrast
:   `--color-decorate: #808080` on `--color-page: #f8f8f8` gives ~3.9:1 contrast — marginal for WCAG 1.4.11 (UI components require 3:1, but the margin was uncomfortably thin).<br> Darkened `--color-decorate` to `#606060` in light mode (~5.7:1 against `#f8f8f8`).

Table caption placement
:   `caption-side: bottom` placed captions after the table visually but before it in DOM order, creating a mismatch between visual and screen-reader reading order.<br> Changed to `caption-side: top; text-align: left`.

List indentation too narrow
:   `padding-left: 1rem` (~16 px) left almost no visual separation between bullets and surrounding text, harming readability for users with cognitive disabilities.<br> Increased to `padding-left: 1.5rem` for both `ol` and `ul`.

Weak focus ring on scrollable code blocks
:   The generic `:focus-visible` rule gives a 2 px outline which can be hard to see against the `--color-highlight` background of `<pre>` elements that also have `tabindex="0"`.<br> Added `pre:focus-visible { outline: 3px solid var(--color-link-unvisited); outline-offset: 2px; }`.

Glossary link label visible to all users
:   The `a.gl-ref::after` rule emitting "(glossary)" was visible to sighted users, cluttering inline text.<br> Applied the standard visually-hidden pattern (`position: absolute; width/height: 1px; clip: rect(0,0,0,0); clip-path: inset(50%); overflow: hidden; white-space: nowrap`) so the label is present in the accessibility tree but not rendered visually.

Italic cascades into blockquote headings
:   `blockquote { font-style: italic }` cascaded to any `<h1>`–`<h3>` inside a blockquote, producing oddly-styled italic headings.<br> Added `blockquote h1, blockquote h2, blockquote h3 { font-style: normal; }`.

Definition list (`<dd>`) has no spacing
:   `<dd>` elements had no left indent or bottom margin, making definition lists read as a wall of text.<br> Added `dd { margin-left: 1.5rem; margin-bottom: var(--len-half); }`.

Empty `section.exercises` rule removed
:   The rule existed with no declarations, and `<section>` landmark elements had no accessible name.<br> Removed the empty rule. Section labelling is now handled in the build pipeline (see build section below).

Dark mode text color hardcoded
:   `body { color: #e8e8e8 }` was set directly in the dark-mode media query rather than via a variable, making the color system inconsistent and hard to override.<br> Added `--color-text: #1a1a1a` to the light-mode `:root` block, overridden to `#e8e8e8` in the dark-mode block. `body` now uses `color: var(--color-text)`.

Skip-to-main-content link
:   Keyboard users had to tab through all navigation links on every page before reaching content.<br> Added `<a class="skip-link" href="#main-content">Skip to main content</a>` as the first element in `<body>`, and `id="main-content"` on `<main>`. The `.skip-link` is visually hidden until focused, at which point it slides into view.

Page title and active nav
:   `<title></title>` was always empty. Nav links had no indication of the current page.<br>
- Title: `<title>{% if title %}{{ title }} · {% endif %}{{ book_title }}</title>`
- Active nav: loop variable renamed from `slug` to `s`; `class="active"` emitted when `s == current_slug`. Both `build.py` and the template were updated.

`<nav>` landmark label
:   The `<nav>` element had no `aria-label`, making it indistinguishable from other nav regions in assistive technology landmark navigation.<br> Added `aria-label="Site navigation"`.

Nav separator read aloud
:   `&middot;` separators between nav items were read as "middle dot" by screen readers.<br> Wrapped each in `<span aria-hidden="true">`.

Footer arrow decorations read aloud
:   `&#8656;` (⇐) and `&#8658;` (⇒) in the footer prev/next links were read as "leftwards double arrow" / "rightwards double arrow".<br> Wrapped each in `<span aria-hidden="true">`.

Dropdown triggers are links, not buttons
:   `<a href="#">` navigates to the page top if activated (wrong semantic); buttons trigger actions. There was also no `aria-haspopup` hint.<br> Changed both dropdown triggers to `<button aria-haspopup="true">`. CSS was updated to reset button appearance and apply the same styles as the former `<a>` triggers.

Language attribute hardcoded
:   `<html lang="en">` was a literal string, making it impossible to publish a non-English book without manually editing the template.<br> Changed to `<html lang="{{ lang|default('en') }}">`. `build.py` now passes `lang` from `config.get("lang", "en")`.

Footer landmark has no label
:   `<footer>` had no `aria-label`, giving screen reader users no context when navigating landmarks.<br> Added `aria-label="Page navigation"`.

Syllabus block has no semantic role
:   `<div class="syllabus">` held learning objectives but had no ARIA role or label.<br> Added `role="note" aria-label="Learning objectives"`.

Missing meta description
:   No `<meta name="description">` meant search engines and browser extensions had no page summary.<br> Added `<meta name="description" content="{{ description|default(book_title) }}">`. `build.py` passes `description` from page frontmatter, falling back to `book_title`.

No theme-color for mobile browsers
:   Without `theme-color`, Android/iOS browser chrome used browser defaults, clashing with both light and dark mode page backgrounds.<br> Added two `<meta name="theme-color">` tags with `media` attributes for light (`#f8f8f8`) and dark (`#1a1a1a`) modes.

Current page slug in template context
:   `_make_context` now includes `"current_slug": slug` so the template can mark the active nav link.

Language code in template context
:   `_make_context` now includes `"lang": config.get("lang", "en")`.

Page description in template context
:   `_make_context` now includes `"description"`, sourced from page frontmatter and falling back to `book_title`.

Scrollable code blocks need keyboard focus
:   Added `_patch_pre_accessibility`: sets `tabindex="0"` on every `<pre>` element so keyboard users can scroll wide code blocks, and sets `data-lang` from the element's language class (e.g. `language-python` → `data-lang="python"`) so the CSS language label is displayed.

Table headers missing `scope`
:   Added `_patch_th_scope`: sets `scope="col"` on `<th>` elements inside `<thead>` and `scope="row"` on `<th>` elements inside `<tbody>`, enabling screen readers to correctly associate headers with data cells.

Exercise section landmark labels
:   Added `_patch_exercise_labels`: sets `aria-label="Exercises"` on every `<section class="exercises">` element so screen reader landmark navigation can find exercise blocks by name.

Inline `<code>` has no visual background
:   `code { font-size: 0.9em }` was the only styling on inline code elements. The 10% size reduction alone does not reliably distinguish code from surrounding prose, particularly for readers with dyslexia or low vision.<br> Added `background-color: var(--color-highlight); padding: 0.1em 0.3em; border-radius: 3px` to `code`. Added a `pre code` override to strip these styles back off inside code blocks, where they would double-apply.

Dropdown nav uses `<span>` not `<ul><li>`
:   `<span class="dropdown-content">` holding bare `<a>` elements gave no list semantics. Screen readers could not announce the item count or allow list-navigation shortcuts. This is a WCAG 1.3.1 Level A failure.<br> Changed both dropdown containers from `<span>` to `<ul role="list">`, each link wrapped in `<li>`. Added `ul.dropdown-content { list-style: none; padding-left: 0; margin-top: 0; }` to CSS to reset the default list styling.

Dropdown link touch targets too small
:   `.dropdown-content a` had `padding-left/right: 4px` and no vertical padding, producing touch targets well below the WCAG 2.5.8 minimum of 24×24px.<br> Changed to `padding: var(--len-half) var(--len-one)` (8px top/bottom, 16px left/right).

Dropdown buttons missing `aria-controls`
:   `<button aria-haspopup="true">` declared the existence of a popup but did not reference it, so assistive technology could not programmatically navigate to the controlled element.<br> Added `aria-controls="nav-lessons"` and `aria-controls="nav-appendices"` to the respective buttons.

`h2`/`h3` top margin was 4px
:   `margin-top: var(--len-thick)` = 4px gave almost no visual separation between sections, making the page difficult to scan — a particular barrier for users with cognitive disabilities (WCAG 1.4.8).<br> Changed to `margin-top: 1.5rem`.

## WCAG References

| Fix | WCAG criterion |
|-----|----------------|
| Blockquote / callout / syllabus borders | 1.4.1 Use of Color |
| Dark mode / text color variable | 1.4.3 Contrast (Minimum) |
| Dropdown `aria-controls` | 4.1.2 Name, Role, Value |
| Dropdown button semantics | 4.1.2 Name, Role, Value |
| Dropdown keyboard access | 2.1.1 Keyboard |
| Dropdown nav list semantics | 1.3.1 Info and Relationships |
| Dropdown touch targets | 2.5.8 Target Size (Minimum) |
| Exercise section label | 1.3.6 Identify Purpose |
| Focus indicators | 2.4.7 Focus Visible, 2.4.11 Focus Appearance |
| Footer landmark label | 1.3.6 Identify Purpose |
| Glossary link label | 2.4.6 Headings and Labels |
| Image overflow | 1.4.10 Reflow |
| Inline code background | 1.4.1 Use of Color |
| Justified text | 1.4.8 Visual Presentation |
| Language attribute | 3.1.1 Language of Page |
| Link colors | 1.4.1 Use of Color, 1.4.3 Contrast (Minimum) |
| List indentation | 1.4.8 Visual Presentation |
| Nav landmark label | 1.3.6 Identify Purpose, 4.1.2 Name, Role, Value |
| Nav separators / footer arrows hidden | 1.3.3 Sensory Characteristics |
| Page title | 2.4.2 Page Titled |
| Scrollable `<pre>` keyboard focus | 2.1.1 Keyboard |
| Section heading margin | 1.4.8 Visual Presentation |
| Skip link | 2.4.1 Bypass Blocks |
| Table `scope` attributes | 1.3.1 Info and Relationships |
| Table caption placement | 1.3.2 Meaningful Sequence |
| Theme color | (Mobile UX best practice) |
| `<meta description>` | (SEO / best practice, not strictly WCAG) |


[dsdx]: @root/dsdx/
[sdxjs]: @root/sdxjs/
[sdxpy]: @root/sdxpy/
