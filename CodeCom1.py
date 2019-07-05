#!/usr/bin/env python
# coding: utf-8


import numpy as np
import random
import matplotlib.pyplot as plt


#variables a modifier
#####################
nb_generation = 100
pourcentage_chance_echec = 10
nb_ind_random = 1000
nb_ville = 20
poids_max = 20

#variables utiles à la génération aléatoire et à l'algorithme
###########################################################
depot = []
nb_ind = nb_ville-1
generation = 0
poids_camion = 0
best_distance_voisin = 0
best_distance = 0
a = 0
best_voisin = []
best_depot = []
Liste = [i for i in range(nb_ville)]
Q = 15
N = [i for i in range(1,nb_ville+1)]
V = [0] + N
dist = []



#génération aléatoire des coordonnées des villes et de leur poids
#################################################################
loc_x = np.random.randint(2000, size=(len(V)))
loc_y = np.random.randint(2000, size=(len(V)))
poids_ville = np.random.randint(1,4, size=(len(N)))

#calcul et création de la matrice des distances entre les villes
###################################################################
for i in V:
	v_1 = np.array((loc_x[i],loc_y[i]))
	dist.append([])
	for y in V:
		v_2 = np.array((loc_x[y],loc_y[y]))
		dist[i].append(round(np.linalg.norm(v_1-v_2)))
print(dist)



# fonction de création d'un voisin du meilleur individu trouvé
###############################################################
def switch_cities(tp_ville,voisin):
	voisin = best.copy()
	m = voisin[tp_ville]
	n = voisin[tp_ville+1]
	voisin[tp_ville] = n
	voisin[tp_ville+1] = m
	print(best)
	return voisin



#boucle de création aléatoire des individus test
#(chemin passant par toutes les villes générés)
#################################################
while a < nb_ind_random :
	poids_camion = 0
	depot = []
	order = random.sample(Liste, nb_ville)

	
	# calcul de la distance totale des individus
	for ville in range(nb_ville) :
		if ville == 0 :
			distance = dist[0][order[0]+1]
		if ville < nb_ville-1 :
			distance += dist[order[ville]+1][order[ville+1]+1]

		else :
			distance += dist[order[ville]+1][0]

		if ville <= nb_ville-1 :
			poids_camion += poids_ville[order[ville]]
		
		if poids_camion > poids_max :
			depot.append(order[ville-1])
			distance += dist[0][order[ville-1]]
			distance += dist[0][order[ville]]
			distance -= dist[order[ville]+1][order[ville-1]+1]
			poids_camion = 0
	
	# comparaison des individus avec le meilleur individu trouvé
	if best_distance > distance or best_distance == 0 :
		best_distance = distance
		best = order
		best_depot = depot
		
	print('_________________')
	print('individu test',a)
	print(best, best_distance)
	a = a+1



# boucle de création et de comparaison des voisins du
#meilleur individu test trouvé sur n génération 
######################################################
while generation < nb_generation :
	print('______________')
	print('génération', generation)
	ind = 0
	tp_ville = 0
	while ind < nb_ind :
		rand = random.randint(0,100)
		voisin = best.copy()
		if 99 - pourcentage_chance_echec < rand :
			voisin = random.sample(Liste, nb_ville)
			print('ECHEC CRITIQUE')
			print(voisin)

		else :
			voisin = switch_cities(tp_ville,best)
			tp_ville += 1
			order = voisin
			poids_camion = 0
			depot = []

		
		# calcul de la distance totale des voisins générés
		for ville in range(nb_ville) :
			if ville == 0 :
				distance = dist[0][order[0]+1]
			if ville < nb_ville-1 :
				distance += dist[order[ville]+1][order[ville+1]+1]

			else :
				distance += dist[order[ville]+1][0]

			if ville <= nb_ville-1 :
				poids_camion += poids_ville[order[ville]]

			if poids_camion > poids_max :
				depot.append(order[ville-1])
				distance += dist[0][order[ville-1]]
				distance += dist[0][order[ville]]
				distance -= dist[order[ville]+1][order[ville-1]+1]
				poids_camion = 0

		# comparaison des voisins avec le meilleur voisin trouvé
		if best_distance_voisin > distance or best_distance_voisin == 0 :
			best_distance_voisin = distance
			best_voisin = voisin
			best_depot = depot
		
		print(best_depot)
			
		ind = ind + 1
		print('____________')
		print('individu',ind)
		print(voisin, distance)
		print(best_voisin, best_distance_voisin)
		print(best, best_distance)

	generation = generation + 1 
	
	# comparaison du meilleur voisin trouvé avec le meilleur individu trouvé
	if best_distance_voisin <= best_distance :
		best = best_voisin
		best_distance = best_distance_voisin



# création graphique du meilleur individu trouvé
#################################################
x = [loc_x[0]]
y = [loc_y[0]]
print(best_depot)
for ville in range(nb_ville) :
	x.append(loc_x[best[ville]+1])
	y.append(loc_y[best[ville]+1])
	if best[ville] in best_depot :
		x.append(loc_x[0])
		y.append(loc_y[0])
x.append(loc_x[0])
y.append(loc_y[0])
plt.plot(x,y,zorder=1)
plt.scatter(loc_x[1:],loc_y[1:],c='b')
for i in N:
	plt.annotate('ville_%d'%(i),(loc_x[i]+2,loc_y[i]))
plt.plot(loc_x[0],loc_y[0],c='r',marker='s')
plt.axis('equal')
plt.show()

