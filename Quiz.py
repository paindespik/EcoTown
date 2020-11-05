from Question import Question
ScoreQuiz = 0

question_prompts = [
     "Quel type d'énergie utiliser ?(a)Solaire (b)Charbon",
     "Avec quoi construire sa maison ?(a)Matériel/produit en masse (b)Bambou",
     "Que faire des déchets ?(a)Les jeters (b)Les recycler",
     "Comment voyager ? (a)A pied ou en vélo (b)Seul en voiture",
]

questions = [
     Question(question_prompts[0], "a", "Lorsque le charbon est brûlé, il libère un certain nombre de toxines et de polluants en suspension dans l'air. Comme le mercure, le plomb, les oxydes d'azote, les particules et divers autres métaux lourds. Les effets sur la santé peuvent aller de l'asthme et des difficultés respiratoires, aux problèmes cardiaques, au cancer, aux troubles neurologiques et même à la mort."),
     Question(question_prompts[1], "b", "Avec du bois produits en masse comme les produits en bois pressé, tels que les panneaux de contreplaqué vous êtes le plus susceptible de trouver du formaldéhyde. Les émissions de formaldéhyde peuvent rendre vos yeux larmoyants ou vous donner la nausée. Cela a également été lié au cancer."),
     Question(question_prompts[2], "b", "Des produits chimiques nocifs et des gaz à effet de serre sont libérés des ordures dans les décharges. Le recyclage contribue à réduire la pollution causée par les déchets. La destruction de l'habitat et le réchauffement climatique sont quelques-uns des effets causés par la déforestation."),
     Question(question_prompts[3], "a", "Les bénéfices environnementaux de la marche sont nombreux. Outre l'émission évidente de gaz à effet de serre, plus de conduite signifie plus de pollution de l'air, ce qui contribue à son tour à des problèmes respiratoires tels que l'asthme. "),
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