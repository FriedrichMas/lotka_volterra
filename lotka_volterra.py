import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Définir les paramètres du modèle
alpha = float(input("Veuillez rentrer alpha: le taux de croissance des proies"))  # Taux de croissance des proies
beta = float(input("veuillez rentrer beta: le taux de prédation"))  # Taux de prédation
delta = float(input("veuillez rentrer delta: le taux de croissance des prédateurs (dépendants des proies")) # Taux de croissance des prédateurs (dépendant des proies)
gamma = float(input("veuillez rentrer gamma: le taux de mortalité des prédateurs")) # Taux de mortalité des prédateurs

# Définir le système d'équations différentielles
def lotka_volterra(t, z):
    x, y = z  # x = population des proies, y = population des prédateurs
    dxdt = alpha * x - beta * x * y
    dydt = delta * x * y - gamma * y
    return [dxdt, dydt]

# Conditions initiales
x0 = int(input("Veuillez rentrer le nombre initial des proies"))  # Population initiale des proies
y0 = int(input("Veuillez rentrer le nombre initial des prédateurs"))   # Population initiale des prédateurs
z0 = [x0, y0]

# Temps de simulation
t_span = (0, 200)  # Intervalle de temps
t_eval = np.linspace(t_span[0], t_span[1], 1000)  # Points où on évalue la solution

# Résolution du système
sol = solve_ivp(lotka_volterra, t_span, z0, t_eval=t_eval)

# Extraire les solutions
t = sol.t
x = sol.y[0]  # Population des proies
y = sol.y[1]  # Population des prédateurs

# Tracer les résultats
plt.figure(figsize=(12, 6))

# Courbes temporelles
plt.subplot(1, 2, 1)
plt.plot(t, x, label="Proies (x)", color="blue")
plt.plot(t, y, label="Prédateurs (y)", color="orange")
plt.xlabel("Temps")
plt.ylabel("Population")
plt.title("Évolution des populations")
plt.legend()

# Diagramme de phase
plt.subplot(1, 2, 2)
plt.plot(x, y, color="green")
plt.xlabel("Proies (x)")
plt.ylabel("Prédateurs (y)")
plt.title("Diagramme de phase")

plt.tight_layout()
plt.show()

