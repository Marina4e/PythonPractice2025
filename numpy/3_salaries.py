import numpy as np

salaries = np.array([50, 23, 45, 67, 45, 64, 25, 44])

mean_salary = np.mean(salaries)
print(f"Average salary: {mean_salary}K$")
print(np.min(salaries))

above_min = salaries[salaries > mean_salary]
print(f"Above mean: {above_min}")