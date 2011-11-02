

Converte os comentários do script http://aurelio.net/bin/php/scraps.phps para o formato do WordPress (WXR).

De:

    <dt>23/05/2005 <b title="verde (a) aurelio net">Aurélio Marinho Jargas</b> (Curitiba - PR)</dt><dd>
    Valeu o toque Zé, coloquei uma observação e uns links da Wikipedia sobre o assunto também. Falou!</dd>

Para:

    <wp:comment>
    <wp:comment_id>1</wp:comment_id>
    <wp:comment_author><![CDATA[Aurélio Marinho Jargas (Curitiba - PR)]]></wp:comment_author>
    <wp:comment_author_email>verde@aurelio.net</wp:comment_author_email>
    <wp:comment_author_url></wp:comment_author_url>
    <wp:comment_author_IP></wp:comment_author_IP>
    <wp:comment_date>2005-05-23 12:00:00</wp:comment_date>
    <wp:comment_approved>1</wp:comment_approved>
    <wp:comment_type></wp:comment_type>
    <wp:comment_parent>0</wp:comment_parent>
    <wp:comment_content><![CDATA[Valeu o toque Zé, coloquei uma observação e uns links da Wikipedia sobre o assunto também. Falou!]]></wp:comment_content>
    </wp:comment>

Uso:

    cat arquivo.html | ./recados2wordpress-meta.sh | ./insert-id.py | ./unique-timestamp.py > arquivo.xml

Leia mais informações no cabeçalho do script principal: recados2wordpress-meta.sh

# insert-id.py 

Script auxiliar para numerar cada comentário no XML final.

# unique-timestamp.py 

Script auxiliar para garantir uma data/hora exclusiva para cada comentário, mantendo assim a ordem original dos comentários.

# recados2wordpress.sh 

Script original, que converte para o formato do WorPress. Porém, coloca a cidade e estado da pessoa junto com o campo Nome, exemplo:

    <wp:comment_author>
    	<![CDATA[Fulano da Silva (Curitiba - PR)]]>
    </wp:comment_author>

Evite usar este script, prefira o recados2wordpress**-meta**.sh.

# recados2wordpress-meta.sh 

Script principal, que converte para o formato do WorPress. Ele funciona com a versão mais recente do plugin de Import do WordPress e cria campos especiais (meta) para a Cidade e Estado dentro da tag <wp:commentmeta>, exemplo:

    <wp:commentmeta>
    	<wp:meta_key>zzcidade</wp:meta_key>
    	<wp:meta_value><![CDATA[Curitiba]]></wp:meta_value>
    </wp:commentmeta>
    <wp:commentmeta>
    	<wp:meta_key>zzestado</wp:meta_key>
    	<wp:meta_value><![CDATA[PR]]></wp:meta_value>
    </wp:commentmeta>

# cidades.sh 

Ferramenta meramente informativa. Compõe uma lista com as cidades e estados dos comentários do arquivo XML, ficando fácil encontrar erros de digitação. Exemplo:

    Abaetetuba                              PA
    Acrelandia                              AC
    Agua boa                                MT
    Aguas lindas                            GO
    Alto Araguaia                           MT
    Alvorada                                RS

Veja mais detalhes sobre o funcionamento deste script neste vídeo: http://aurelio.net/blog/2011/04/19/o-jeito-shell-script-de-resolver-problemas/

