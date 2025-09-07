from die import Die

die = Die()
results = []
for row_num in range(100):
    s = die.row()
    results.append(s)

print(results)
