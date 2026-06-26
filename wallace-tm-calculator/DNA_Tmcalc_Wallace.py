allowed_inputs = {'A', 'C', 'G', 'T'}
seq = input("Enter your DNA sequence: ").upper()
setseq = set(seq)

if setseq.issubset(allowed_inputs) :  

  nG = seq.count('G')
  nC = seq.count('C')
  nA = seq.count('A')
  nT = seq.count('T')

  print ("Your DNA sequence has " + str(nG) + ' Guanine bases,', str(nC) + ' Cytosine bases,', str(nA) + ' Adenine bases, and', str(nT) + ' Thymine bases.')
  ## Wallace rule (Tm = 2*(A+T) + 4*(G+C)) (for seq under 14-20bp in length)

  Tm = 2*(nA + nT) + 4*(nG + nC)

  print("Approximate melting point = " + str(Tm) + "°Celsius")

else :
    print("Error, please input a valid DNA sequence composed of Adenine, Guanine, Cytosine, and Thymine bases (ex: ACGTGACTGATGA)")