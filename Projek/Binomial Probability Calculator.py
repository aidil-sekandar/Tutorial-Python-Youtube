# modules
import math

# input
n = int(input("n: "))
p = float(input("p: "))
q = 1 - p
r = int(input("r: "))
x = int(input("""
[1] P(X = r)
[2] P(X > r)
[3] P(X >= r)
[4] P(X < r)
[5] P(X <= r)

choose (1-5): 
"""))

# calculation
def binoProbCalc(n, p, q, r):
  ncr = math.factorial(n) / (math.factorial(n-r) * math.factorial(r))
  pr = math.pow(p, r)
  qnr = math.pow(q, n-r)

  return(ncr * pr * qnr)


def binoProbCalc_cond(n, p, q, r, step, x):
  totalProb = 0
  tempProb = 0

  for i in range(step):
      if x == 2 or x == 5:
        r += 1
        tempProb = binoProbCalc(n, p, q, r)
      elif x == 3 or x == 4:
        tempProb = binoProbCalc(n, p, q, r)
        r += 1

      totalProb += tempProb
  
  return(totalProb)


# types of prob
if x == 1:
  prob = round(binoProbCalc(n, p, q, r), 4)
elif x == 2:
  prob = binoProbCalc_cond(n, p, q, r, n - r, x)
elif x == 3:
  prob = binoProbCalc_cond(n, p, q, r, n - r + 1, x)
elif x == 4:
  prob = 1 - binoProbCalc_cond(n, p, q, r, n - r + 1, x)
elif x == 5:
  prob = 1 - binoProbCalc_cond(n, p, q, r, n - r, x)

print("\nprobability: " + str(prob))
