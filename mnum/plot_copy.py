# x = [-2, -1, 0, 1, 2]
# y = [5, -2, 4, -7, 2]

print('Wprowadz liczbe: ')
val = float(input())

print('Interpolacja Lagrange\'a:%10s %.2f => y: %.4f' %
      ('x:', val, mnum.lagrange_interpolation(val, x, y)))
print('Interpolacja Newton\'a:%12s %.2f => y: %.4f' %
      ('x:', val, mnum.newton_interpolation(val, x, y)))
print('Interpolacja NumPy:%15s %.2f => y: %.4f' %
      ('x:', val, np.interp(val, x, y)))


xvals = np.linspace(-5, 5, 100)
yinterp = mnum.lagrange_interpolation(xvals, x, y)
yinterp2 = mnum.newton_interpolation(xvals, x, y)

x = np.array(x)
y = np.array(y)

plt.title('Wykresy funkcji f(x)=(1 + x^2)^-1')
plt.plot(x, y, 'o')
plt.plot(xvals, yinterp, '-x')
plt.plot(xvals, yinterp2, '-x')
plt.plot(np.linspace(-5, 5, 100), np.power(1+np.power(xvals, 2), -1), c="r")
plt.show()
