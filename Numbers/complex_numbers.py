import cmath

# Eulers Identity

print('Eulers identity: e^pi(i) + 1 = 0: ', cmath.exp(cmath.pi*1j) + 1)

print('Using isclose: ', cmath.isclose(cmath.exp(cmath.pi * 1j) + 1, 0, abs_tol=0.0001))

a = 1 + 1j
print('Angle (phase) of 1 + 1j: ', cmath.phase(a))
print('Magnitude of 1+1j: ', abs(a))