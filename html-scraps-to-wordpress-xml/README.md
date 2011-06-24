html-scraps-to-wordpress-xml README


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
    <wp:comment_date_gmt>2005-05-23 12:00:00</wp:comment_date_gmt>
    <wp:comment_approved>1</wp:comment_approved>
    <wp:comment_type></wp:comment_type>
    <wp:comment_parent>0</wp:comment_parent>
    <wp:comment_content><![CDATA[Valeu o toque Zé, coloquei uma observação e uns links da Wikipedia sobre o assunto também. Falou!]]></wp:comment_content>
    </wp:comment>

Uso:

    cat arquivo.html | ./recados2wordpress.sh | ./insert-id.py > arquivo.xml

# insert-id.py 

Script auxiliar para numerar cada comentário no XML final.

# recados2wordpress.sh 

Script principal, veja instruções no cabeçalho. Coloca os campos Cidade e Estado junto com o campo Nome, exemplo:

    <wp:comment_author>
    	<![CDATA[Fulano da Silva (Curitiba - PR)]]>
    </wp:comment_author>

# recados2wordpress-meta.sh 

Script principal modificado para colocar Cidade e Estado em campos especiais zzcidade e zzestado dentro da tag <wp:comment_meta>, exemplo:

    <wp:comment_meta>
    	<wp:c_meta_key>zzcidade</wp:c_meta_key>
    	<wp:c_meta_value><![CDATA[Curitiba]]></wp:c_meta_value>
    </wp:comment_meta>
    <wp:comment_meta>
    	<wp:c_meta_key>zzestado</wp:c_meta_key>
    	<wp:c_meta_value><![CDATA[PR]]></wp:c_meta_value>
    </wp:comment_meta>

