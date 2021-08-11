amount=int(input("Enter the amount (Rs): "))
note2000=note500=note200=note100=note50=note20=note10=note5=note2=note1=0

if amount>=2000:
     note2000=amount//2000
     amount -= note2000*2000   # We subtracted 2000 from the amount aftr its been divided
if amount>=500:
     note500=amount//500
     amount -= note500*500    # We subtracted 500 from the amount aftr its been divided
if amount>=200:
     note200=amount//200
     amount -= note200*200    # We subtracted 200 from the amount aftr its been divided
if amount>=100:
     note100=amount//100
     amount -= note100*100    # We subtracted 100 from the amount aftr its been divided
if amount>=50:
     note50=amount//50
     amount -= note50*50      # We subtracted 50 from the amount aftr its been divided
if amount>=20:
     note20=amount//20
     amount -= note20*20      # We subtracted 20 from the amount aftr its been divided
if amount>=10:
     note10=amount//10
     amount -= note10*10      # We subtracted 10 from the amount aftr its been divided
if amount>=5:
     note5=amount//5
     amount -= note5*5        # We subtracted 5 from the amount aftr its been divided
if amount>=2:
     note2=amount//2
     amount -= note2*2        # We subtracted 2 from the amount aftr its been divided
if amount>=1:
     note1=amount//1
     amount -= note1*1        # We subtracted 1 from the amount aftr its been divided

print(f"Note of 2000: ",note2000)
print(f"Note of 500: ",note500)
print(f"Note of 200: ",note200)
print(f"Note of 100: ",note100)
print(f"Note of 50: ",note50)
print(f"Note of 20: ",note20)
print(f"Note of 10: ",note10)
print(f"Note of 5: ",note5)
print(f"Note of 2: ",note2)
print(f"Note of 1: ",note1)