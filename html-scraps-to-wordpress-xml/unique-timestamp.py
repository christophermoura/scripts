#!/usr/bin/env python
# coding: utf-8
# 2011-11-02 http://aurelio.net
#
# Script complementar ao recados2wordpress.sh.
# Veja instruções no cabeçalho dele.
#
# Este script transforma:
#   <wp:comment_date>2000-12-31 12:00:00</wp:comment_date>
#   <wp:comment_date>2000-12-31 12:00:00</wp:comment_date>
#   <wp:comment_date>2000-12-31 12:00:00</wp:comment_date>
# em:
#   <wp:comment_date>2000-12-31 12:00:03</wp:comment_date>
#   <wp:comment_date>2000-12-31 12:00:02</wp:comment_date>
#   <wp:comment_date>2000-12-31 12:00:01</wp:comment_date>
#
# Para manter a ordem original dos comentários feitos no mesmo dia.

import sys
import re

text = sys.stdin.read()

# Count duplicates in a list and return a (count, item) list
def countDups(l):
   unique = set(l)
   return [(l.count(x), x) for x in unique if l.count(x) > 1]

# Extract all dates and find those with multiple comments (>1)
multiple = countDups(re.findall(r'<wp:comment_date>....-..-.. 12:00:00</wp:comment_date>', text))
#
# Example:
#
# multiple = [
#   (2, "<wp:comment_date>2011-04-10 12:00:00</wp:comment_date>"),
#   (5, "<wp:comment_date>2009-09-22 12:00:00</wp:comment_date>")
# ]


# Change the seconds for each pattern, decreasing (03, 02, 01)
for count,pattern in multiple:
    while count > 0:
        text = text.replace(
                pattern,
                pattern.replace('12:00:00', '12:00:' + ('%02d' % count), 1),
                1)
        count -= 1

sys.stdout.write(text)
