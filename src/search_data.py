class SearchCategory:
    def __init__(self, name, subcategories):
        self.name = name
        self.subcategories = subcategories

    def search(self, query):
        results = []
        for subcategory, descriptions in self.subcategories.items():
            for description in descriptions:
                if query.lower() in description.lower():
                    results.append(f"{subcategory}: {description}")
        return results

search_categories = [
    SearchCategory("Manifesto do Partido Comunista", {


        "Burgueses e proletários": [

            "A história de toda a sociedade até aqui é a história de lutas de classes.",

            "[Homem] livre e escravo, patrício e plebeu, barão e servo [Leibeigener], burgueses de corporação [Zunftbürger] e oficial, em suma, opressores e oprimidos, estiveram em constante oposição uns aos outros, travaram uma luta ininterrupta, ora oculta ora aberta, uma luta que de cada vez acabou por uma reconfiguração revolucionária de toda a sociedade ou pelo declínio comum das classes em luta.",

            "Nas anteriores épocas da história encontramos quase por toda a parte uma articulação completa da sociedade em diversos estados [ou ordens sociais — Stände], uma múltipla gradação das posições sociais. Na Roma antiga temos patrícios, cavaleiros, plebeus, escravos; na Idade Média: senhores feudais, vassalos, burgueses de corporação, oficiais, servos, e ainda por cima, quase em cada uma destas classes, de novo gradações particulares.",

            "A moderna sociedade burguesa, saída do declínio da sociedade feudal, não aboliu as oposições de classes. Apenas pôs novas classes, novas condições de opressão, novas configurações de luta, no lugar das antigas."



            ],
        "Proletários e comunistas": [

            "Em que realção se encontram os comunistas com os proletários em geral?",

            "Os comunistas não são nenhum partido particular face aos outros partidos operários.",

            "Não têm nenhuns interesses separados dos interesses do proletariado todo.",

            "Não estabelecem nenhuns princípios particulares segundo os quais queiram moldar o movimento proletário.",

            "Os comunistas diferienciam-se dos demais partidos proletários apenas pelo facto de que, por um lado, nas diversas lutas nacionais dos proletários eles acentuam e fazem valer os interesses comuns, independentes da nacionalidade, do proletariado todo, e pelo facto de que, por outro lado, nos diversos estádios de desenvolvimento por que a luta entre o proletariado e a burguesia passa, representam sempre o interesse do movimento total.",


            ],
        "Literatura socialista e comunista": [


            "Pela sua posição histórica, as aristocracias francesa e inglesa estavam vocacionadas para escrever panfletos contra a sociedade burguesa moderna. Na revolução francesa de Julho de 1830, no movimento de reforma inglês (42), elas sucumbiram uma vez mais ao odiado arrivista. Não podia mais tratar-se de uma luta política séria. Restava-lhes apenas a luta literária. Mas também no domínio da literatura o velho palavreado do tempo da restauração * tinha-se tornado impossível. Para despertar simpatia, a aristocracia teve de aparentar perder de vista os seus interesses e de formular a sua acusação contra a burguesia apenas no interesse da classe operária explorada. Preparou assim a satisfação de poder cantar cantigas de escárnio sobre o seu novo dominador e sussurrar-lhe ao ouvido profecias mais ou menos prenhes de desgraças.",

            "Desta maneira surgiu o socialismo feudalístico — metade canto lamentoso e metade pasquim, metade eco do passado e metade ameaça do futuro —, por vezes acertando no alvo com um juízo amargo, espirituosamente demolidor, sobre a burguesia, mas sempre operando de modo cómico pela sua total incapacidade de conceber o curso da história moderna.",

            "Por estandarte eles agitavam na mão o proletário alforge de mendigo, para juntarem o povo atrás de si. Mas de todas as vezes que este os seguia divisava-lhes no traseiro os velhos brasões feudais e dispersava com gargalhadas sonoras e irreverentes."


            ],
    }),




    SearchCategory("A Ideologia Alemã", {

        "(Introdução)": [



            "Até agora, os homens formaram sempre idéias falsas sobre si mesmos, sobre aquilo que são ou deveriam ser. Organizaram as suas relações mútuas em função das representações de Deus, do homem normal, etc., que aceitavam. Estes produtos do seu cérebro acabaram por os dominar; apesar de criadores, inclinaram-se perante as suas próprias criações. Libertemo-los portanto das quimeras, das idéias, dos dogmas, dos seres imaginários cujo jugo os faz degenerar. Revoltemo-nos contra o império dessas idéias. Ensinamos os homens a substituir essas ilusões por pensamentos que correspondam à essência do homem, afirma um; a ter perante elas uma atitude crítica, afirma outro; a tirá-las da cabeça, diz um terceiro e a realidade existente desaparecerá.",

            "Estes sonhos inocentes e pueris formam o núcleo da filosofia atual dos Jovens Hegelianos; e, na Alemanha, são não só acolhidas pelo público com um misto de respeito e pavor corno ainda apresentadas pelos próprios heróis filosóficos com a solene convicção de que tais idéias, de uma virulência criminosa, constituem para o inundo um perigo revolucionário. O primeiro volume desta obra propõe-se desmascarar estas ovelhas que se julgam lobos e que são tomadas como lobas mostrando que os seus balidos apenas repetem numa linguagem filosófica as representações dos burgueses alemães e que as suas fanfarronadas se limitam a refletir a pobreza lastimosa da realidade alemã; propõe-se ridicularizar e desacreditar esse combate filosófico contra assombras da realidade que tanto agrada à sonolência sonhadora do povo alemão.",


            "Em tempos, houve quem pensasse que os homens se afogavam apenas por acreditarem na idéia da gravidade. Se tirassem esta idéia da cabeça, declarando por exemplo que não era mais do que uma representação religiosa, supersticiosa, ficariam imediatamente livres de qualquer perigo de afogamento. Durante toda a sua vida, o homem que assim pensou viu-se obrigado a lutar contra rodas as estatísticas que demonstram repetidamente as conseqüências perniciosas de uma tal ilusão. Este homem constituía um exemplo vivo dos atuais filósofos revolucionários alemães"


            ],


        "Oposição entre a concepção materialista e a idealista": [


            "De acordo com certos ideólogos alemães, a Alemanha teria sido nestes últimos anos o teatro de uma revolução sem precedentes. O processo de decomposição do sistema hegeliano, iniciado com Strauss (2) , teria dado origem a uma fermentação universal para a qual teriam sido arrastadas todas as «potências do passado». Nesse caos universal, formaram-se impérios poderosos que depois sofreram uma derrocada imponente, surgiram heróis efêmeros mais tarde derrubados por rivais audazes e mais poderosos. Perante uma tal revolução. a Revolução francesa não foi mais do que uma brincadeira de crianças e os combates dos diádocos (3) parecem-nos mesquinhos. Os princípios foram substituídos, os heróis do pensamento derrubaram-se uns aos outros: de 1842 a 1845, o solo alemão foi mais revolvido do que nos três séculos anteriores.",


            "E tudo isto se teria passado nos domínios do pensamento puro",

            "Trata-se, com efeito, de um acontecimento interessante: o processo de decomposição do espírito absoluto"

            ],


        "Em especial, a filosofia alemã": [


            "As premissas de que partimos não constituem bases arbitrárias, nem dogmas; são antes bases reais de que só é possível abstrair no âmbito da imaginação. As nossas premissas são os indivíduos reais, a sua ação e as suas condições materiais de existência, quer se trate daquelas que encontrou já elaboradas aquando do seu aparecimento quer das que ele próprio criou. Estas bases são portanto verificáveis por vias puramente empíricas."


            ]
    })
]
