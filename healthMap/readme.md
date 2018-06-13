Os passos para o scraper do healthmap seriam mais ou menos assim:

Com o Healthmap aberto e com a visão de lista mostrando todos os elementos;
Recuperar do HTML a tabela que contém as notícias;
Data:
Recuperar o segundo elemento de cada linha da tabela;
Link da noticia:
De cada linha da tabela, pegar a terceira entrada, que é a que contém um link;
abir esse link(popup);
do popup recuperar a section com id `alert`.
de `alert` recuperar o link contido em `article`.
exemplo:
````html
<section id="alert">
    <h1>
        Experts commend India for maintaining polio-free status - Clipper28 (satire) (press release) (blog) - <img class="f" src="./images/feeds/g.png" title="Google News" alt="Google News"> - 06/13/2018    </h1>
                <aside>
        Summary
        </aside>
        <article>
            <p>Experts commend India for maintaining polio-free status   Eleven cases have been registered in 2018 in only two countries – Afghanistan and Pakistan. “The experts appreciate the example that India sets for the rest of the world. By eliminating polio in India, the country has demonstrated that global polio ... <a href="ln.php?5853956" target="_blank">view full article</a></p>
            <div id="translated_text"></div>
            <p class="aside">India | Polio | Humans<br></p>
        </article>

</section>
````
Título da notícia:
Recuperar o h1 depois de acessar a notícia
Doença:
Recuperar o quarto elemento de cada linha da tabela

Local:
Recuperar o quinto elemento de cada linha da tabela