# CSS audit

Audit of the stylesheets that will be consolidated into one `mccole.css`.
The end state is a single `mccole.css`, byte-identical across all projects, so
sdxjs and sdxpy (and ark, change, closure) share identical layout. Decisions
already made: drop Chota (hand-roll the base framework) and keep `pygments.css`
(smaller and simpler than `tango.css`).

## 1. File inventory, grouped by identical content

27 CSS files were found across `docs/` and the external repositories. Files
with identical bytes are grouped; each group is one logical stylesheet that is
duplicated.

| Logical stylesheet | Copies | Bytes | Where |
|---|---|---|---|
| `chota.css` | 5 | 18,366 | `docs/files/`, `docs/sdxjs/_static/`, `docs/sdxpy/_static/`, `~/sdxjs/_static/`, `~/sdxpy/_static/` |
| `pygments.css` | 4 | 4,054 | `docs/sdxjs/_static/`, `docs/sdxpy/_static/`, `~/sdxjs/_static/`, `~/sdxpy/_static/` |
| `book.css` | 3 | 110 | `docs/mccole/`, `~/change/mccole/`, `~/closure/mccole/` |
| `mccole.css` (sdxjs variant) | 2 | 7,569 | `docs/sdxjs/_static/`, `~/sdxjs/_static/` |
| `mccole.css` (sdxpy variant) | 2 | 12,155 | `docs/sdxpy/_static/`, `~/sdxpy/_static/` |
| `slides.css` (mccole variant) | 2 | 3,633 | `docs/mccole/`, `~/closure/mccole/` |
| `slides.css` (sdxpy variant) | 2 | 2,191 | `docs/sdxpy/_static/`, `~/sdxpy/_static/` |

Unique files (not duplicated):

| File | Bytes | Notes |
|---|---|---|
| `docs/files/mccole.css` | 6,145 | the ark copy of mccole.css, diverged from the other two |
| `docs/files/tango.css` | 5,010 | ark's syntax theme (to be dropped) |
| `docs/files/slides.css` | 6,138 | ark's slides theme, diverged |
| `docs/files/page.css` | 138 | one-off body/change rule |
| `docs/files/fiction.css` | 31 | one-off body rule |
| `docs/files/thirdbit.css` | 1,104 | ark site-specific rules |
| `~/change/mccole/slides.css` | (varies) | change's slides, not byte-identical to closure's |

## 2. mccole.css: three divergent variants

There are three distinct `mccole.css` files (same name, different content):

| Variant | Rules | Selectors | Bytes |
|---|---|---|---|
| ark (`docs/files/mccole.css`) | 59 | 53 | 6,145 |
| sdxjs (`docs/sdxjs/_static/mccole.css`) | 71 | 65 | 7,569 |
| sdxpy (`docs/sdxpy/_static/mccole.css`) | 139 | 110 | 12,155 |

The relationship is a superset chain, not three independent files:

- **Common core (all three):** 53 selectors. This is the shared base: the
  `:root` variables, headings, body, code, tables, lists, figures, footer,
  dropdown menu, callout/syllabus, glossary refs, and collapsible explanations.
- **sdxjs adds over ark** (+12 selectors): code-inclusion markup
  (`.inc-path`, `div[data-inc]`), collapsible `details`/`summary`,
  `table.two-col`, and `.nav .brand`.
- **sdxpy adds over sdxjs** (+45 selectors): a large `@media print` block
  (roughly 45 selectors covering `body`, headings, code, tables, callouts,
  `details`, figures, and nav for print).

So the merge is mostly additive: ark is a subset, sdxjs layers code-inclusion
and details on top, sdxpy layers print rules on top. The open questions are
whether the code-inclusion and print rules belong in the shared `mccole.css` or
stay project-specific.

## 3. slides.css: three variants

Three divergent slide stylesheets:

| Variant | Lines | Selectors |
|---|---|---|
| ark (`docs/files/slides.css`) | 331 | 72 |
| mccole (`docs/mccole/slides.css`) | 170 | 37 |
| sdxpy (`docs/sdxpy/_static/slides.css`) | 105 | 17 |

These are three separate slide themes, not a superset chain. They need to be
reconciled or replaced with one slide theme.

## 4. Syntax highlighting: tango vs pygments

Decision: keep `pygments.css`, drop `tango.css`.

| | tango.css | pygments.css |
|---|---|---|
| Bytes | 5,010 | 4,054 |
| Lines | 77 | 74 |
| Selector style | `.highlight .c` (needs a wrapper `<div>`) | bare `.c` (Pygments default) |
| Extra | `.g .l .n .x .p` generic tokens | 5 `linenos` rules |

`pygments.css` is smaller, simpler, and is the default Pygments output. The
four copies (sdxjs/sdxpy, source and published) are byte-identical.

## 5. One-off files

Small files to fold into `mccole.css` or drop:

- `page.css` — `body` (margin/max-width) and `div.change`.
- `fiction.css` — `body` (max-width 70rem).
- `book.css` — `.center`, `dt`, `dd` (110 bytes; change/closure use this).
- `thirdbit.css` — ark site-specific: heading backgrounds, `img.centered`,
  `img.footer-icon`, `img.image`, `div.bibliography`, `p.disclaimer`,
  `h3.card-title`, `.card.beta`, `div.change`, `table.fullwidth`.

## 6. Structural markup (grid, callouts, cards)

Two overlapping systems for the same things, which is what makes the CSS large.

### Multi-column grid

Chota's grid, with inconsistent spellings in the templates:

- `row` (97 uses) with `col-6` (94), `col-3` (84), `col-4` (6), `col-8` (6),
  `col-12` (1), `col-9` (1), `col-2` (1), and bare `col` (5).
- `collapse` / `collapse-horizontal` (31 each) — a second, Bootstrap-style grid
  from a legacy project (outside the six, per the brief, but worth noting).
- `column` / `columns` (2 each) — generic spellings.

### Callouts

Two different callout mechanisms:

- `div.callout` and `div.syllabus` — the simple custom callout in `mccole.css`
  (used by ark, sdxjs, sdxpy).
- Quarto's callout system — `callout-note`, `callout-header`, `callout-body`,
  `callout-icon`, `callout-title-container`, `callout-style-default`,
  `callout-style-simple`, `callout-titled`, `callout-none` (98 `callout*` uses
  total), generated by the Quarto build used by change/closure.

### Cards

- `card`, `card-title`, `.card.beta` (ark's card markup in `thirdbit.css`).

## 7. What the merge must decide

1. **Grid:** pick one spelling (`row` + `col-*`) and update the templates to
   use only that, then style only that in `mccole.css`.
2. **Callouts:** reconcile `div.callout` with Quarto's `callout-*` classes.
   Either teach change/closure to emit `div.callout`, or teach mccole.css to
   style Quarto's classes. One mechanism, not two.
3. **Code inclusion and print rules:** since the end state is one identical
   file, sdxjs's `.inc-path`/`details`/`table.two-col` and sdxpy's `@media
   print` block either go into the shared `mccole.css` for everyone or are
   dropped — there is no project-local CSS to fall back to. This is also the
   main lever for getting under 100 selectors (the 45-selector print block is
   the largest single chunk).
4. **Slides:** collapse three slide themes into one.
5. **One-offs:** fold `page.css`, `fiction.css`, `book.css`, and `thirdbit.css`
   into `mccole.css`, or delete the unused ones.

## 8. External repositories: build systems and template changes

The six projects are built by three systems, so the changes are not confined to
this repo.

### Build systems

- `src/` (this repo) is built by ark; templates at
  `lib/thirdbit/templates/*.jinja`.
- `sdxjs` and `sdxpy` are built by the `mccole` pip package
  (`mccole build --src . --dst docs`). Its templates are at
  `mccole/data/_templates/page.html` (plus `slides.html`, `single_page.html`)
  and its CSS at `mccole/data/_static/` (`mccole.css`, `chota.css`,
  `pygments.css`, `slides.css`). Their published `_static/*.css` is a build
  artifact copied from this package.
- `change` and `closure` are built by Quarto (`quarto render`) plus the mccole
  Lua tool (`mccole/publish.lua`); content is `.qmd` files (14 in change, 26 in
  closure).

### Changes needed in the external repositories

1. **mccole package** (`data/_templates/page.html`): the template already uses
   the Chota `row` + `col-3`/`col-6` grid and `div.callout`/`div.syllabus`
   markup. Since Chota is dropped, that grid markup must be restyled by the
   hand-rolled base (or simplified). Replace `data/_static/mccole.css` with the
   consolidated file, delete `data/_static/chota.css`, keep `pygments.css`, and
   reconcile `data/_static/slides.css`.

2. **change and closure** (`.qmd` files): callouts are inconsistent — most use
   Quarto's `:::{.callout-note}` fenced div (which emits the `callout-note` /
   `callout-header` / `callout-body` / `callout-icon` classes), but a few use
   raw `<div class="callout">` (e.g. `starting/index.qmd`). Multi-column uses
   Quarto's `:::{.columns}` + `:::{.column width="…"}`. Both must be made to
   emit one markup: `div.callout` for callouts, and the same grid as the other
   projects. (The `.qmd` files are source, so editing them is allowed; the
   "no hand-editing HTML" rule applies to generated `docs/` output only.)

3. **change and closure** (`mccole/publish.lua`): change the CSS-path rewrite so
   the copied pages link `./docs/files/mccole.css`, and stop emitting the
   Quarto `site_libs` CSS if it is no longer needed.

4. **sdxjs and sdxpy**: no source changes of their own — their `_static/` CSS is
   copied from the mccole package, so they rebuild once the package is updated.

Note: the step that copies each external project's built `docs/` into this
repo's `docs/` (sdxjs, sdxpy, change, closure) is the **mccole publish step**,
which is not yet fully automated. For change/closure the CSS-path rewrite lives
in `publish.lua`; the equivalent for sdxjs/sdxpy still has to be built, and is
where their copied pages would be pointed at `./docs/files/mccole.css`.

