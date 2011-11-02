#!/usr/bin/env python
# coding: utf-8
# 2011-03-30 http://aurelio.net
#
# Script complementar ao recados2wordpress.sh.
# Veja instruções no cabeçalho dele.
#
# Este script transforma:
#   <wp:comment_id></wp:comment_id>
#   <wp:comment_id></wp:comment_id>
#   <wp:comment_id></wp:comment_id>
# em:
#   <wp:comment_id>1</wp:comment_id>
#   <wp:comment_id>2</wp:comment_id>
#   <wp:comment_id>3</wp:comment_id>
#

import sys
import re

# Recent comments come first?
reverse = True

text = sys.stdin.read()
regex = re.compile(r'(\n<wp:comment_id)>(</wp:comment_id>\n)')

if reverse:
    count = len(regex.findall(text))  # how many occurences?
else:
    count = 1

# Replace every occurence, one by one, increasing/decresing count
while regex.search(text):
    text = regex.sub(r'\1>' + str(count) + r'\2', text, 1)
    if reverse:
        count -= 1
    else:
        count += 1

sys.stdout.write(text)

