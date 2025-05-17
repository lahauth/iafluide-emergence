import numpy as np

# Loi fluide : stabilité ⇔ (v_abs ≤ seuil) ∧ (ρ < critique) ∧ (d²ρ/dt² ≥ 0)
class PsiAgent:
    def __init__(self, rho, v_abs, d2rho_dt2):
        self.rho = rho
        self.v_abs = v_abs
        self.d2rho_dt2 = d2rho_dt2
        self.seuil_rho = 0.6
        self.seuil_v = 0.8

    def is_stable(self):
        return self.v_abs <= self.seuil_v and self.rho < self.seuil_rho and self.d2rho_dt2 >= 0

    def regulate(self):
        if self.is_stable():
            return "Stable"
        elif self.rho >= self.seuil_rho:
            return "Purge + Répartition"
        elif self.v_abs > self.seuil_v:
            return "Ralenti + Désynchronisation"
        else:
            return "Observation"

if __name__ == "__main__":
    agents = [PsiAgent(rho=np.random.uniform(0.3, 0.9),
                       v_abs=np.random.uniform(0.4, 1.0),
                       d2rho_dt2=np.random.uniform(-0.3, 0.3)) for _ in range(5)]

    for i, agent in enumerate(agents):
        print(f"Ψ-agent {i+1}: {agent.regulate()}")
