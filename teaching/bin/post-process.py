#!/usr/bin/env python

import sys
import re

sub_ref = re.compile(r'\\href{([^.]+)\.html\\#([^}]+)}{([^}]+)}', re.DOTALL)
chap_ref = re.compile(r'\\href{([^.]+)\.html}{([^}]+)}', re.DOTALL)
chap_lbl = re.compile(r'\\chapter{([^}]+)}\\label{[^}]+}\s+\\label{([^}]+)}', re.DOTALL)

def sub_ref_repl(m):
    filename = m.group(1)
    label = m.group(2)
    text = m.group(3)
    if (filename == 'biblio'):
        return text
    elif (filename == 'gloss'):
        return text
    else:
        return text + ' (\\S\\ref{' + label + '})'

def chap_ref_repl(m):
    filename = m.group(1)
    text = m.group(2)
    return text + ' (\\S\\ref{' + filename + '})'

def chap_lbl_repl(m):
    text = m.group(1)
    keep = m.group(2)
    sys.stderr.write('chap_lbl_replace {} {}\n'.format(text, keep))
    return '\\chapter{' + text + '}\\label{' + keep + '}'

data = sys.stdin.read()
for (pat, func) in ((sub_ref, sub_ref_repl),
                    (chap_ref, chap_ref_repl),
                    (chap_lbl, chap_lbl_repl)):
    data = pat.sub(func, data)
data = data.replace(r'\subsection{', r'\subsection*{')
sys.stdout.write(data)
