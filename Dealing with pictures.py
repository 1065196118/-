import matplotlib.pyplot as plt
a=plt.imread("C:/Users/user/Pictures/beach08_1920x1080.jpg")
print(a.shape)
print(a)
print(a.size)# مجموع العناصر او البكسل  
'''f=open("machean.txt","w+")
b,c,d=a.shape
for x in range(b):
    for y in range(c):
        for z in range(3):
            f.write('\n'+str('Data for : '+str(x)
                             +' & '+str(y)+' & '+str(z))+' is : '
                    +str((a[x,y,z])))
f.close()
plt.imshow(a)
a=open("machean.txt","r")
print (a.read()) '''
# قص الصوره 
plt.subplot(221)
plt.imshow(a)

x=a[280:800,1230:1700,:]
plt.subplot(222)
plt.imshow(x)
     
y=a[520:700,1660:,:]
plt.subplot(223)
plt.imshow(y)

z=a[550:750,480:750,:]
plt.subplot(224)
plt.imshow(z)
# التحكم في الالوان

plt.subplot(221)
plt.imshow(a)

x=a[280:800,1230:1700,0]
plt.subplot(222)
plt.imshow(x)
     
y=a[520:700,1660:,1]
plt.subplot(223)
plt.imshow(y)

z=a[550:750,480:750,2]
plt.subplot(224)
plt.imshow(z)






