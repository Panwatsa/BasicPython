friend = ['Aum', 'Kreang', 'Meji', 'Jean']

friend2 = {'Aum':'อั้ม','Kreang':'เกรียง'}

visitor = 'Meji'

if visitor in friend or visitor.title() in friend:
    print('คุณ {} เป็น member เชิญเข้ามาด้านใน'.format(visitor))
    if visitor in friend2 or visitor.title() in friend2:
        print('สวัสดีคุณ' + friend2[visitor.title()])
    else:
        print('สวัสดีครับ')

else:
    print('ไม่พบรายชื่อ กรุณาติดต่อเจ้าหน้าที่')