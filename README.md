
# MODELE PROIE-PREDATEUR (LOTKA-VOLTERRA)

Ce mini projet a pour but de modéliser et analyser la dynamique proie-prédateur dans un ecosystème où ils coéxistent et sont interdépendants sans influence d'une troisième partie. Nous allons faire un script python pour voir, grâce aux graphes, les résultats de la modélisation et d'analyse.  


## Modélisation et analyse de la dynamique

1. Modélisation 

Nous nous plaçons dans un écosystème où les prédateurs se nourrissent exclusivement des proies donc sans ces dernières, ils seront voués à la disparution et les proies n'ont qu'une seule espèce de prédateurs. 

Alors nous constantons qu'en absence des prédateurs, les poies auront une évolution exponentielle (modèle de Malthus) et en l'absence des proies, les prédateurs s'éteindront également de façon exponentielle. 

Donc la prédation a ainsi un impact significatif sur la population de proies et de prédateurs dans ce système fermé. 

De cela, nous avons le système d'équation suivant :

$$
\frac{dx}{dt} = ax - bxy
$$

$$
\frac{dy}{dt} = -by + dxy
$$

où: 
* x(t) représente la population de proies
* y(t) représente la population de prédateurs
* a > 0 est le taux de croissance des proies en l'absence des prédateurs
* b > 0 est le taux de prédation (effet des prédateurs sur les proies)
* c > 0 est le taux de mortalité des prédateurs en l'absence des proies
* d > 0 est le d'accroissement des prédateurs grâce aux proies consommées


2. Analyse

a) Points d'équilibres

Les points d'équilibres, nous permettent de comprendre le comportement du système d'évolution à long terme, sont obtenus en calculant $\frac{dx}{dt}$ = 0 et  $\frac{dy}{dt}$ = 0

Après un calcul direct simple, on a: 

1°. E_0 = (0,0) : extinction ou absence de deux population 
2°. E_1 = (c/d , a/b) : équilibre non trivial, où les deux populmations coexistent. 

b) Stabilité des points d'équilibres

* Point E_0 = (0,0) : ce point est trivial et instable car il n'y a pas d'individus dans le système et toute perturbation initiale entraîne une déviation du système. 
* PointE_1 = (c/d, a/b) : la stabilité dépend des oscillations autour de cet équilmibre. 

Pour analyser la stabilité, on calcule le déterminant de la matrice jacobienne aux point E_0 et E_1. 
Au point E_0 on a zéro et au point E_1, on a $\frac{abcd}{bd}$

c) La périodicité des oscillations

Les solutions de ce système sont généralement des trajectoires fermées autour de E_1, ce qui traduit des cycles de populations périodiques:

* Lorsque les proies augmentent, les prédateurs augmentent avec un décalage temporel.
* Une augmentation excessives des prédateurs diminue les proies, ce qui entraîne une chute des prédateurs, permettant aux proies de se retablir et ainsi de suite. 




## A propos du code

1. Pour ce script, nous n'avons pas fait appel aux librairies complexes ou installations particulières. Nous avons juste utilisé Numpy, Matplotlib.pyplot et Scipy. 

2. Le programme, grâce à la fonction python input, demandera à l'utilisateur de fournir les taux des croissances et de prédation, ainsi que les le nombre initial d'individus dans chaque groupe.

3. La fonction lotka_volterra qui prend en compte toutes les données fournies par l'utilisateur et l'intervalle de temps ( t_span = (0, 200), fixé dans le code) modélise le problème selon l'équation du modèle explicitée ci-haut. 

4. Le problème est résolu grâce à solve_ivp venant de scipy puis une extraction des valeurs de x, y et t.

5. Enfin, deux graphes sont tracés. Celui des courbes d'évolution temporelles des deux groupes et celui du diagramme des phases. 


## Exemple

Dans le but d'essayer le code, vous pouvez utiliser les données suivantes : 
* alpha = 0.1  #Taux de croissance des proies
* beta = 0.02  #Taux de prédation
* gamma =0.1  #Taux de mortalité des prédateurs
* delta = 0.01  #Taux de croissance des prédateurs
* x0 = 40  #population initiale de proies
* y0 = 9  #population initiale de prédateurs
