
# experiment_E_model.py
"""
A simple calculator for Experiment E:
- Fits a cubic polynomial a(t) to the given data points.
- Integrates to produce v(t) and x(t).
- Allows user to input a time t and outputs a(t), v(t), x(t).

Usage:
  1. Make sure you have numpy installed: pip install numpy
  2. Run: python experiment_E_model.py
  3. At the prompt, enter a time (in seconds between 0 and 0.5) to see a(t), v(t), x(t).
"""

import numpy as np

# Given data from PASCO
t_data = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
a_data = np.array([2.704, 2.755, 2.646, 1.721, 0.640, 0.379])

# Fit a cubic polynomial (degree=3) to the (t, a) data
# The returned coefficients are [C3, C2, C1, C0] for C3*t^3 + C2*t^2 + C1*t + C0
coeffs = np.polyfit(t_data, a_data, 3)

# Unpack the coefficients
C3, C2, C1, C0 = coeffs

# Define the acceleration polynomial a(t)
def a_t(t):
    return C3*t**3 + C2*t**2 + C1*t + C0

# Integrate the cubic to get a quartic for v(t), with v(0)=0
# Integral of (C3*t^3) = (C3/4)*t^4, etc.
# So V3 = C3/4, V2 = C2/3, V1 = C1/2, V0 = C0
V4 = C3 / 4
V3 = C2 / 3
V2 = C1 / 2
V1 = C0

def v_t(t):
    return V4*t**4 + V3*t**3 + V2*t**2 + V1*t

# Integrate v(t) to get x(t), with x(0)=0
# Integral of (V4*t^4) = (V4/5)*t^5, etc.
X5 = V4 / 5
X4 = V3 / 4
X3 = V2 / 3
X2 = V1 / 2

def x_t(t):
    return X5*t**5 + X4*t**4 + X3*t**3 + X2*t**2

# Print out the fitted coefficients (rounded)
print("Fitted acceleration coefficients (a(t) = C3*t^3 + C2*t^2 + C1*t + C0):")
print(f"  C3 = {C3:.5f}")
print(f"  C2 = {C2:.5f}")
print(f"  C1 = {C1:.5f}")
print(f"  C0 = {C0:.5f}\n")

print("Derived velocity polynomial v(t) (with v(0)=0):")
print(f"  v(t) = {V4:.5f}*t^4 + {V3:.5f}*t^3 + {V2:.5f}*t^2 + {V1:.5f}*t\n")

print("Derived position polynomial x(t) (with x(0)=0):")
print(f"  x(t) = {X5:.5f}*t^5 + {X4:.5f}*t^4 + {X3:.5f}*t^3 + {X2:.5f}*t^2\n")

# Main loop: prompt the user for a time and print a(t), v(t), x(t)
while True:
    try:
        s = input("Enter a time t (s) between 0 and 0.5, or 'q' to quit: ").strip().lower()
        if s == 'q':
            print("Goodbye!")
            break
        t_val = float(s)
        if not (0 <= t_val <= 0.5):
            print("  -- Please enter a value between 0 and 0.5.")
            continue
        a_val = a_t(t_val)
        v_val = v_t(t_val)
        x_val = x_t(t_val)
        print(f"  a({t_val:.3f}) = {a_val:.5f} m/s^2")
        print(f"  v({t_val:.3f}) = {v_val:.5f} m/s")
        print(f"  x({t_val:.3f}) = {x_val:.5f} m\n")
    except ValueError:
        print("  -- Invalid input. Type a number (e.g. 0.12) or 'q' to quit.")
