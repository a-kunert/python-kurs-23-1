amount=0
for k in range(0,1000000,7):
  old_k = k
  k=k/100
  k=str(k)
  find_digit=k.find(".99")
  if old_k % 100 == 99:
    print(k)
    print(find_digit)
  if find_digit > 0:
    print(k)
    ###Kontrolle
    ###k=float(k)
    ###k=k*100
    ###k=int(k)
    ###print(k)
    amount=amount+1
print(amount)