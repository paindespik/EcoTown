from Question import Question
ScoreQuiz = 0

question_prompts = [
     "Quel type d'énergie utiliser ?(a)Solaire (b)Charbon",
     "Avec quoi construire sa maison ?(a)Matériel/produit en masse (b)Bambou",
     "Que faire des déchets ?(a)Les jeters (b)Les recycler",
     "Comment voyager ? (a)A pied ou en vélo (b)Seul en voiture",
]

questions = [
     Question(question_prompts[0], "a", "Lorsque le charbon est brûlé, il libère un certain nombre de toxines et de polluants en suspension dans l'air. Comme le mercure, le plomb, les oxydes d'azote, les particules et divers autres métaux lourds. Les effets sur la santé peuvent aller de l'asthme et des difficultés respiratoires, aux problèmes cardiaques, au cancer, aux troubles neurologiques et même à la mort. Tandis que Le soleil fournit plus qu’assez d’énergie pour répondre aux besoins énergétiques du monde entier et, contrairement aux combustibles fossiles, il ne s’épuisera pas de si tôt. En tant que source d'énergie renouvelable, la seule limitation de l'énergie solaire est notre capacité à bien la transformer en électricité. Aucune émission de gaz à effet de serre n'est libérée dans l'atmosphère lorsque vous utilisez des panneaux solaires pour produire de l'électricité. Le carburant n’est pas nécessaire, l’énergie solaire est directement transformée en électricité, de sorte qu’aucun stockage supplémentaire n’est nécessaire, ce qui signifie que l’énergie solaire peut créer de grandes quantités d’électricité sans l’incertitude et les frais liés à la sécurisation d’une source."),
     Question(question_prompts[1], "b", "Avec du bois produits en masse comme les produits en bois pressé, tels que les panneaux de contreplaqué vous êtes le plus susceptible de trouver du formaldéhyde. Les émissions de formaldéhyde peuvent rendre vos yeux larmoyants ou vous donner la nausée. Cela a également été lié au cancer. Pour réduire les risques, recherchez des produits en bois qui utilisent autre chose que de la résines d'urée comme du bambou qui est facile a manipuler est qui est en fait une herbe qui repousse très vite."),
     Question(question_prompts[2], "b", "Des produits chimiques nocifs et des gaz à effet de serre sont libérés des ordures dans les décharges. Le recyclage contribue à réduire la pollution causée par les déchets. La destruction de l'habitat et le réchauffement climatique sont quelques-uns des effets causés par la déforestation. Le recyclage réduit le besoin de matières premières afin de préserver les forêts tropicales. D'énormes quantités d'énergie sont utilisées lors de la fabrication de produits à partir de matières premières. Le recyclage nécessite beaucoup moins d'énergie et contribue donc à préserver les ressources naturelles."),
     Question(question_prompts[3], "a", "Les bénéfices environnementaux de la marche sont nombreux. Outre l'émission évidente de gaz à effet de serre, plus de conduite signifie plus de pollution de l'air, ce qui contribue à son tour à des problèmes respiratoires tels que l'asthme. Chaque voiture sur la route peut entraîner une augmentation des accidents et des décès liés à la voiture, sans parler des déplacements ou des déplacements à l'épicerie plus frustrants. Compte tenu de la récente flambée des prix de l'essence, sans fin en vue, la marche, ainsi que les transports en commun, deviennent une option plus attrayante. En tenant compte des avantages pour la santé, la marche est encore plus belle. La marche peut réduire le risque de nombreuses maladies, notamment les crises cardiaques, les accidents vasculaires cérébraux et le glaucome. Il aide à gérer le poids, à contrôler la tension artérielle et à se protéger contre les fractures de la hanche. La diminution de l'exposition à la circulation dense et aux longs trajets réduit également le stress, ce qui au fil du temps augmente le risque de maladies comme les maladies cardiaques. Les autres avantages fréquemment cités comprennent la prévention de la dépression, le soulagement de l'arthrite, des os et des articulations plus solides et une durée de vie plus longue."),
]

def Prompt(questioninput):
          switcher = {
             0: question_prompts[0],
             1: question_prompts[1],
             2: question_prompts[2],
             3: question_prompts[3],
             }
          return switcher.get(questioninput,"Aucune question pour ce chiffre")


def QuestionVerifier(numQuestion, answer):
     if questions[numQuestion].answer == answer:
          return questions[numQuestion].explanation
     else:
         return 'faux'


def Score(score):
     global ScoreQuiz
     ScoreQuiz += score
     return ScoreQuiz