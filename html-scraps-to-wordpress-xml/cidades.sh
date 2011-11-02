#!/bin/bash
# 2011-11-02 http://aurelio.net
#
# Uso: cat arquivo.xml | ./cidades.sh
#
# Compõe uma lista com as cidades e estados dos comentários do arquivo XML
#
# Veja mais detalhes sobre o funcionamento deste script neste vídeo:
# http://aurelio.net/blog/2011/04/19/o-jeito-shell-script-de-resolver-problemas/
#
# Exemplo:
#     Abaetetuba                              PA
#     Acrelandia                              AC
#     Agua boa                                MT
#     Aguas lindas                            GO
#     Alto Araguaia                           MT
#     Alvorada                                RS

grep meta_value |
	sed 's/.*\[// ; s/\]\].*//' |
	sed 'N; s/\n/	/' |
	sort -f |
	uniq |
	expand -t 40
