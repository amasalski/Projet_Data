#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import matplotlib.pyplot as plt


# In[2]:


#variables 
nb_generation = 100
nb_ville = 10
nb_ind_random = 10000
nb_reset = 10
poids_camion = 0
poids_max = 10

poids_ville = np.random.randint(1,4, size = (nb_ville))
nb_ind = nb_ville-1
generation = 0
reset = 0
best_distance_voisin = 0
best_distance = 0
boat_distance = 0
best_voisin = []
a = 0
print(poids_ville)

Liste = [i for i in range(nb_ville)]

Q = 15
N = [i for i in range(1,nb_ville+1)]
V = [0] + N
dist = []


# In[3]:


loc_x = np.random.randint(2000, size = (len(V)))
loc_y = np.random.randint(2000, size = (len(V)))
for i in V:
    v_1 = np.array((loc_x[i],loc_y[i]))
    dist.append([])
    for y in V:
        v_2 = np.array((loc_x[y],loc_y[y]))
        dist[i].append(round(np.linalg.norm(v_1-v_2)))
#print(dist)


# In[4]:


plt.scatter(loc_x[1:],loc_y[1:],c='b')
for i in N:
    plt.annotate('ville_%d'%(i),(loc_x[i]+2,loc_y[i]))
plt.plot(loc_x[0],loc_y[0],c='r',marker='s')
plt.axis('equal')
#plt.show()


# In[5]:


def switch_cities(best,ind):
    voisin = best.copy()
    m = voisin[ind]
    n = voisin[ind+1]
    voisin[ind+1] = m
    voisin[ind] = n
    return voisin


# In[6]:

while reset <= nb_reset :
    while a < nb_ind_random :
        order = random.sample(Liste, nb_ville)
        #print(order)
        distance = dist[0][order[0]+1]
        poids_camion = poids_ville[0]

        #print(distance)
        for ville in range(nb_ville) :
            if ville < nb_ville-1 :
                distance += dist[order[ville]+1][order[ville+1]+1]
                poids_camion += poids_ville[ville]
                #print(dist[order[ville]+1][order[ville+1]+1])
            else :
                distance += dist[order[ville]+1][0]
                poids_camion += poids_ville[ville]
                #print(dist[order[ville]+1][0])
                #print('stop')
        print('poids camion =', poids_camion)    

        if best_distance > distance or best_distance == 0 :
            best_distance = distance
            best = order
        print('_________________')
        print('individu test',a)
        print(order, distance)
        print(best, best_distance)
        a = a+1


    # In[7]:


    while generation < nb_generation :
        print('______________')
        print('génération', generation)
        ind = 0
        while ind < nb_ind :
            voisin = switch_cities(best,ind)
            order = voisin
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

        if best_distance_voisin <= best_distance or best_distance == 0 :
            best = best_voisin
            best_distance = best_distance_voisin
                
        if best_distance < boat_distance or boat_distance == 0 :
            boat = best
            boat_distance = best_distance

    x = [loc_x[0]]
    y = [loc_y[0]]
    for ville in range(nb_ville) :
        x.append(loc_x[boat[ville]+1])
        y.append(loc_y[boat[ville]+1])
    x.append(loc_x[0])
    y.append(loc_y[0])
    plt.plot(x,y,zorder=1)
    plt.scatter(loc_x[1:],loc_y[1:],c='b')
    for i in N:
        plt.annotate('ville_%d'%(i),(loc_x[i]+2,loc_y[i]))
    plt.plot(loc_x[0],loc_y[0],c='r',marker='s')
    plt.axis('equal')
   

    print('reset', reset)
    generation = 0
    best_distance = 0
    reset = reset + 1 
plt.show()
print(poids_camion)

# In[ ]:





# In[ ]:




