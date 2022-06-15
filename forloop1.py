
print('----Loop in List----')

friend = ['Aum', 'Kreang', 'Meji', 'Jean'] #loop in list

for i in friend:
    print(i)
    if i == 'Meji':
        print('เชิญ VIP เข้ามา')
    else:
        print('รอก่อนนะครับ')
    
print('----Loop in Diction----')

friend2 = {'Aum':'อั้ม','Kreang':'เกรียง'}

#show key
for f in friend2:
    print(f)

#show items
for f in friend2.items():
    print(f)

#show key only
for f in friend2.keys():
    print(f)

#show value only
for f in friend2.values():
    print(f)

#ต้องการลำดับ
for i,f in enumerate(friend,start=1):
    print(i,f)

#ต้องการลำดับ dict
for i,f in enumerate(friend2.items()): #iจะเป็นลำดับ fจะเป็น items
    print(i,f)

#ต้องการลำดับ dict แยก key
for i,(k,v) in enumerate(friend2.items()):
    print(i,k,v)