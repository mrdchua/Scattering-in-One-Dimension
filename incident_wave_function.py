import numpy as np
import matplotlib.pyplot as plt

domain_x = (-1.0, 1.0)
domain_t = (0.0, np.pi/2.0)
size = 100

x = np.linspace(domain_x[0], domain_x[1], size)
t = np.linspace(domain_t[0], domain_t[1], size)

X, T = np.meshgrid(x, t)

plt.scatter(T, X)
plt.xlabel("T")
plt.ylabel("X")
plt.show()

x_flat = X.flatten()
t_flat = T.flatten()

plt.scatter(t_flat, x_flat)
plt.xlabel("t")
plt.ylabel("x")
plt.show()

def incident_wave(x, t):
    A = 1.0
    E = 1.0
    k = 1.0
    h_bar = 1.0

    psi_real = A*np.cos(k*x)*np.cos(E*t/h_bar) + A*np.sin(k*x)*np.sin(E*t/h_bar)
    psi_imag = A*np.cos(E*t/h_bar)*np.sin(k*x) - A*np.cos(k*x)*np.sin(E*t/h_bar)
    psi = psi_real**2.0 + psi_imag**2.0
    return psi_real, psi_imag, psi

psi_inc_real, psi_inc_imag, psi_inc = incident_wave(X, T)

plt.contourf(T, X, psi_inc, 100, cmap="rainbow")
plt.xlabel("t")
plt.ylabel("x")
plt.title("$/\psi(x,t)/^2$")
plt.show()


t_chosen_values = [0.0, 0.79, 0.98]

fig, axes = plt.subplots(1, 3, figsize=(15,3))
for i, t_specific in enumerate(t_chosen_values):
    t_plot = np.full_like(x_flat, t_specific)
    psi_inc_real, psi_inc_imag, psi_inc = incident_wave(x_flat, t_plot)

    axes[i].plot(x_flat, psi_inc, label=f"$|\psi(x,t={t_specific})|^2$")
    axes[i].set_xlabel('x')
    axes[i].set_ylabel('$/\psi(x,t)/^2$')
    axes[i].set_title(f"$|\psi(x,t={t_specific})|^2$")
    axes[i].legend()

plt.tight_layout()
plt.show()