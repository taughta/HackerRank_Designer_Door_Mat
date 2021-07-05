size = input()
n, m = size.split(' ')
n = int(n)
m = int(m)

assert 5 < n < 101
assert n % 2 == 1
assert 15 < m < 303
assert 3 * n == m

mat_text = 'WELCOME'
design_pattern = '.|.'
final_mat = ''

for y in range(n // 2):
    line_design = design_pattern * (y + y + 1)

    final_mat += (line_design).center(m, '-') + '\n'

final_mat += '{}\n'.format(mat_text.center(m, '-'))

for z in reversed(range(n // 2)):
    line_design = design_pattern * (z + z + 1)

    final_mat += (line_design).center(m, '-') + '\n'

print(final_mat)
