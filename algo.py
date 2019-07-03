#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import matplotlib.pyplot as plt


# In[2]:


#variables 
nb_generation = 10
nb_ind = 10
nb_ville = 10
generation = 0
best_distance_voisin = 0
best_distance = 0
best_voisin = []
a = 0
Liste = [i for i in range(nb_ville)]

rnd = np.random
rnd.seed(0)
Q = 15
N = [i for i in range(1,nb_ville+1)]
V = [0] + N
q = {i:rnd.randint(1,10) for i in N}
dist = []


# In[3]:


loc_x = rnd.rand(len(V))*200
loc_y = rnd.rand(len(V))*100
for i in V:
    v_1 = np.array((loc_x[i],loc_y[i]))
    dist.append([])
    for y in V:
        v_2 = np.array((loc_x[y],loc_y[y]))
        dist[i].append(round(np.linalg.norm(v_1-v_2)))
print(dist)


# In[4]:


plt.scatter(loc_x[1:],loc_y[1:],c='b')
for i in N:
    plt.annotate('ville_%d=%d'%(i,q[i]),(loc_x[i]+2,loc_y[i]))
plt.plot(loc_x[0],loc_y[0],c='r',marker='s')
plt.axis('equal')
plt.show()


# In[5]:


def switch_cities(nb_ville,best):
    voisin = best
    r = random.randint(1,nb_ville-2)
    c = random.choice([-1,1])
    m = voisin[r]
    r = r+c
    n = voisin[r]
    voisin[r] = m
    r = r-c
    voisin[r] = n
    return voisin


# In[6]:


while a < nb_ind :
    order = random.sample(Liste, nb_ville)
    #print(order)
    distance = dist[0][order[0]+1]
    #print(distance)
    for ville in range(nb_ville) :
        if ville < nb_ville-1 :
            distance += dist[order[ville]+1][order[ville+1]+1]
            #print(dist[order[ville]+1][order[ville+1]+1])
        else :
            distance += dist[order[ville]+1][0]
            #print(dist[order[ville]+1][0])
            #print('stop')
        

    if best_distance > distance or best_distance == 0 :
        best_distance = distance
        best = order
    print('_________________')
    print('individu test',a)
    print(best, best_distance)
    a = a+1


# In[7]:


while generation < nb_generation :
    print('______________')
    print('génération', generation)
    ind = 0
    while ind < nb_ind :
        voisin = switch_cities(nb_ville,best)
        order = voisin
        #print(order)
        distance = dist[0][order[0]+1]
            #print(distance)
        for ville in range(nb_ville) :
            if ville < nb_ville-1 :
                distance += dist[order[ville]+1][order[ville+1]+1]
                #print(order[ville+1]+1)
            else :
                distance += dist[order[ville]+1][0]
            #print(distance)

        if best_distance_voisin > distance or best_distance_voisin == 0 :
            best_distance_voisin = distance
            best_voisin = voisin
            
        ind = ind + 1
        print('____________')
        print('individu',ind)
        print(voisin, distance)
        print(best_voisin, best_distance_voisin)
        print(best, best_distance)

    generation = generation + 1     
    if best_distance_voisin <= best_distance :
        best = best_voisin
        best_distance = best_distance_voisin
    

plt.show()


# In[ ]:





# In[ ]:



