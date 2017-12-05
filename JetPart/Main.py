from JetConstruction import collision
from JetReconstruction import reconstruct
from Graph import histo3d
from Mass import SimpleMass

# Values for R and n for reconstruction algorithm
Rs = [0.01, 0.05, 0.1, 0.5, 1.0]
ns = [-1, 0, 1]

# Making collision, so that each reconstruction has the same collison to reconstruct
col = collision()

# Calculating a SimpleMass of the Jet
print(SimpleMass(col))

# ans contains reconstructions of jets for all combinations of R's and n's,
# with ans[i][0] containing a number of partons in i-th reconstruction,
# and ans[i][1] collection of parton (already reconstructed) in i-th reconstruction
ans = []

# Variables for sanity checks
rvals = []
nvals = []
freq = []

# Running algorithm through all combinations of R and n values
for R in Rs:
    for n in ns:
        rec = reconstruct(col, R, n)
        rvals.append(R)
        nvals.append(n)
        freq.append(rec[0])
        ans.append(rec)
        print("done R " + str(R) + "  n " + str(n) + "  # " + str(rec[0]))
print("done")
print("")
print("")

# Graphing 3d histogram with respect to R and n
histo3d(rvals, nvals, freq)

# Sanity checks for energy and momentum
energy_check = []
p_check = []
for i in ans:
    s = sum(i[1])
    energy_check.append(round(s[0], 7))
    p_check.append([round(s[1], 7), round(s[2], 7), round(s[3], 7)])
for i in range(len(energy_check)):
    for j in p_check[i]:
        print(i) if not j == 0 else " "

    for j in range(i, len(energy_check)-1):
        if not energy_check[i] == energy_check[j]:
            print("i:" + str(i) + "    " + str(energy_check[i]) + "  j:" + str(j) + "   " + str(energy_check[j]))
