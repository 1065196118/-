# -
مشروع يقوم بعمل جميع التقديرات للمواد الدراسية
material_1=int(input("enter the material_1 =  "))
material_2=int(input("enter the material_2 =  "))
material_3=int(input("enter the material_3 =  "))
material_4=int(input("enter the material_4 =  "))
material_5=int(input("enter the material_5 =  "))
print("\n")
print("Appreciation the material_1 :-  ")
if material_1>=50 and material_1<65:
       print("Accepted")
elif material_1>=65 and material_1<75:
       print("Good\n")
elif material_1>=75 and material_1<85:
       print("Very Good\n")
elif material_1>=85 and material_1<=100:
       print("Excellent\n")
elif material_1>=0 and material_1<50:
         print("week\n")
else:
        print("degree is wrong\n")
print("Appreciation the material_2 :-  ")
if material_2>=50 and material_2<65:
       print("Accepted\n")
elif material_2>=65 and material_2<75:
        print("Good\n")
elif material_2>=75 and material_2<85:
       print("Very Good\n")
elif material_2>=85 and material_2<=100:
       print("Excellent\n")
elif material_2>=0 and material_2<50:
       print("week\n")
else:
       print("degree is wrong\n")
print("Appreciation the material_3  :-  ")
if material_3>=50 and material_3<65:
       print("Accepted\n")
elif material_3>=65 and material_3<75:
      print("Good\n")
elif material_3>=75 and material_3<85:
     print("Very Good\n")
elif material_3>=85 and material_3<=100:
       print("Excellent\n")
elif material_3>=0 and material_3<50:
        print("week\n")
else:
      print("degree is wrong\n")
print("Appreciation the material_4  :-  ")
if material_4>=50 and material_4<65:
        print("Accepted\n")
elif material_4>=65 and material_4<75:
      print("Good\n")
elif material_4>=75 and material_4<85:
      print("Very Good\n")
elif material_4>=85 and material_4<=100:
        print("Excellent\n")
elif material_4>=0 and material_4<50:
       print("week\n")
else:
        print("degree is wrong\n")
print("Appreciation the material_5  :-  ")
if material_5>=50 and material_5<65:
        print("Accepted\n")
elif material_5>=65 and material_5<75:
       print("Good\n")
elif material_5>=75 and material_5<85:
       print("Very Good\n")
elif material_5>=85 and material_5<=100:
        print("Excellent\n")
elif material_5>=0 and material_5<50:
    print("week\n")
else:
       print("degree is wrong\n")
s=material_1 + material_2 + material_3 + material_4 + material_5
print("total summation",s)
per=(s/500)*100
print("percentage p.c =  ",per,"%")
print("General appreciation  :-   ")
if per>=50 and per<65:
        print("Accepted\n")
elif per>=65 and per<75:
       print("Good\n")
elif per>=75 and per<85:
        print("Very Good\n")
elif per>=85 and per<=100: 
     print("Excellent\n")
elif per>=0 and per<50: 
        print("Precipitate\n")
else:
       print("degree is wrong\n")
       
import matplotlib.pyplot as plt

x=(material_1,material_2,material_3,material_4,material_5)
plt.plot(x)
plt.plot(x,'m--*')
plt.xlabel('x')
plt.ylabel('Grades')
plt.title('Grading statistic')







