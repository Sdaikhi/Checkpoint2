#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3
n = input("Tapé la valu de l'integer n : ")

n = int(n)

if(n%2 == 0):
    print("Le nombre '", n, "' tapé est pair ")
else:
    print("Le nombre '", n, "' tapé est impair ")


# In[7]:


#4
l=[]
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        l.append(str(i))

print(','.join(l))


# In[ ]:


#1
first_name = input("Quelle est ton prenom ?: ")
last_name = input("Quelle est ton nom de famille ?: ")

print(last_name + " " + first_name)


# In[ ]:


#5
n = 8
fact = 1
  
for i in range(1,n+1): 
    fact = fact * i 
      
print ("La factorielle de 8 est : ",end="") 
print (fact) 


# In[ ]:


#6
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

print(odd_values_string('hello+team'))


# In[ ]:


#2
n = 5
n2 = int( "%s" % n )
n3 = int( "%s%s" % (n,n) )
n4 = int( "%s%s%s" % (n,n,n) )
print(n2+n3+n4)


# In[ ]:


#je n'ai pas reussi la question 7


# In[ ]:




