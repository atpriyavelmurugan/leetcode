a=list(input("Enter the code:"))
b=list(input("Enter the code:"))
count=0
s=0
for i in range(len(a)):
   if a[i]==b[i]:
      count+=1

for i in range(len(guess)):
    if guess[i] is not None and guess[i] in code:
        near_hits += 1
        # Remove the matched digit so it is not counted again
        code[code.index(guess[i])] = None

print(f"{count}H{s-1}N")
