ev = int(input("Milyen év van?"))
név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = ev - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
érettségi = születési_év + 18
print(név, ', kend ', érettségi, '-ban érettségizik.', sep='')