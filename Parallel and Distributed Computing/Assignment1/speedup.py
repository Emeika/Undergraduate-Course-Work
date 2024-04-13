T_seq = 142.44

# Parallel program execution time
T_par = 16.80

P = T_seq / (T_seq + (T_par))

# Calculate Speedup using Amdahl's Law
S = 1 / ((1 - P) + (P / (T_seq / T_par)))


print(f"The speedup factor is {S:.2f}")
