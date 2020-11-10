# mobil=['toyota','jazz','jazz']
# print(type(mobil))
# print(mobil)

# # huruf=('a','b','b','c')
# # print(huruf)

# #set
# z={1,2,3,1,2,3}
# print(type(z))
# print(z)

p={1,2,4,7,9,19}
q={5,12,16,17,7,9,19,6}
r={19,6,3,8}

#Gabungan P dan Q
unpq = p.union(q)
print('gabungan p dan q adalah',unpq)

#Gabungan dari P dan R
unpr = p.union(r)
print('gabungan p dan r adalah',unpr)

#gabungan Q dan R
unqr=q.union(r)
print("gabungan q dan R adalah",unqr)

print("irisan dari gabungan p da q serta q an r adalah", unpq.intersection(unqr))

print("symetric difference qr dan pq",unqr.symmetric_difference(unpq))