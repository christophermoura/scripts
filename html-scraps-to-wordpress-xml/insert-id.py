#!/usr/bin/env python
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

text = sys.stdin.read()

count = 1
while re.search(r'(?s)\n<wp:comment_id></wp:comment_id>\n', text):
    text = re.sub(r'(?s)^(.*?\n<wp:comment_id)>(</wp:comment_id>\n)', r'\1>'+str(count)+r'\2', text)
    count += 1

sys.stdout.write(text)

