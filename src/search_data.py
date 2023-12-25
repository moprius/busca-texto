# search_data.py

class SearchCategory:
    def __init__(self, name, descriptions):
        self.name = name
        self.descriptions = descriptions

    def search(self, query):
        for description in self.descriptions:
            if query.lower() in description.lower():
                return description
        return None

search_categories = [
    SearchCategory("Manifesto do Partido Comunista", [

        "A presente tradução do Manifesto do Partido Comunista foi feita a partir do texto da edição alemã de 1890, preparada por Friedrich Engels, publicada nas Marx/Engels Werke (doravante MEW), Berlim, Dietz Verlag, 19747, vol. 4, pp. 459-493.",

        "Quanto aos prefácios em língua alemã, foram utilizados os textos constantes das MEW, vol. 4, pp. 573-574 (edição alemã de 1872); pp. 575-576 (edição russa de 1882); p. 577 (edição alemã de 1883); pp. 583-586 (edição alemã de 1890); pp. 587-588 (edição polaca de 1892).",

        "Para o aparato crítico foram tidas em conta as notas das MEW, das edições portuguesas acima citadas (as Notas Complementares de Vasco Magalhães-Vilhena contidas na edição por ele dirigida deverão continuar a ser consultadas para um aprofundamento destas matérias), bem como informação recolhida, designadamente, em Bert Andréas, Le Manifeste Communiste de Marx et Engels. Histoire et bibliographie. 1848-1918, Milano, Feltrinelli, 1963."

        "Anda um espectro pela Europa — o espectro do Comunismo. Todos os poderes da velha Europa se aliaram para uma santa caçada a este espectro, o papa e o tsar, Metternich e Guizot, radicais franceses e polícias alemães.",

        "Onde está o partido de oposição que não tivesse sido vilipendiado pelos seus adversários no governo como comunista, onde está o partido de oposição que não tivesse arremessado de volta, tanto contra os oposicionistas mais progressistas como contra os seus adversários reaccionários, a recriminação estigmatizante do comunismo?"
    ]),
    SearchCategory("A Ideologia Alemã", [

        "Até agora, os homens formaram sempre idéias falsas sobre simesmos, sobre aquilo que são ou deveriam ser. Organizaram as suas relações mútuas em função das representações de Deus, do homem normal, etc., que aceitavam. Estes produtos do seu cérebro acabaram por os dominar; apesar de criadores, inclinaram-se perante as suas próprias criações. Libertemo-los portanto das quimeras, das idéias, dos dogmas, dos seres imaginários cujo jugo os faz degenerar. Revoltemo-nos contra o império dessas idéias. Ensinamos os homens a substituir essas ilusões por pensamentos que correspondam à essência do homem, afirma um; a ter perante elas uma atitude crítica, afirma outro; a tirá-las da cabeça, diz um terceiro e a realidade existente desaparecerá.",

        "Estes sonhos inocentes e pueris formam o núcleo da filosofia atual dos Jovens Hegelianos; e, na Alemanha, são não só acolhidas pelo público com um misto de respeito e pavor corno ainda apresentadas pelos próprios heróis filosóficos com a solene convicção de que tais idéias, de uma virulência criminosa, constituem para o inundo um perigo revolucionário. O primeiro volume desta obra propõe-se desmascarar estas ovelhas que se julgam lobos e que são tomadas como lobas mostrando que os seus balidos apenas repetem numa linguagem filosófica as representações dos burgueses alemães e que as suas fanfarronadas se limitam a refletir a pobreza lastimosa da realidade alemã; propõe-se ridicularizar e desacreditar esse combate filosófico contra assombras da realidade que tanto agrada à sonolência sonhadora do povo alemão.",


        "Em tempos, houve quem pensasse que os homens se afogavam apenas por acreditarem na idéia da gravidade. Se tirassem esta idéia da cabeça, declarando por exemplo que não era mais do que uma representação religiosa, supersticiosa, ficariam imediatamente livres de qualquer perigo de afogamento. Durante toda a sua vida, o homem que assim pensou viu-se obrigado a lutar contra rodas as estatísticas que demonstram repetidamente as conseqüências perniciosas de uma tal ilusão. Este homem constituía um exemplo vivo dos atuais filósofos revolucionários alemães.",


        "E tudo isto se teria passado nos domínios do pensamento puro"
    ])
]
