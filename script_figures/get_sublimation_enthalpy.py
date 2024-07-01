#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
from matplotlib.lines import Line2D
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

axis_font={'family':'arial','size':18}

####### data upload

dmc=np.loadtxt('../data_figures/diffusion-monte-carlo/DMC')

nmol=np.loadtxt('../data_figures/diffusion-monte-carlo/nmol')
names=["1,4-cyclohexanedione" ,"Acetic Acid" ,"Adamantane" ,"Ammonia" ,"Anthracene" ,"Benzene" ,"CO$_2$" ,"Cyanamide" ,"Cytosine" ,"Ethyl carbamate" ,"Formamide" ,"Imidazole" ,"Naphthalene" ,r"Oxalic Acid $\alpha$" ,r"Oxalic Acid $\beta$" ,"Pyrazine" ,"Pyrazole" ,"Triazine" ,"Trioxane" ,"Uracil" ,"Urea" ,"Hexamine" ,"Succinic Acid" ]


rpa=np.loadtxt('../data_figures/other/RPA',usecols=(2,1))
embcc=np.loadtxt('../data_figures/other/DeltaCCSDT')
ccsdtcbs=np.loadtxt('../data_figures/other/CCSDT-CBS')

vib_dhb=np.loadtxt('../data_figures/vibrational-contribution/vib_DHB',usecols=(0,2))
dhb_error=np.loadtxt('../data_figures/vibrational-contribution/DHB_uncertainty')




path_to_extrapolated='../data_figures/experiments/extrapolated'
extrapolated_enthalpies=[]
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_1_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_2_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_3_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_4_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_5_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_6_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_7_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_8_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_9_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_10_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_11_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_12_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_13_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_14_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_15_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_16_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_17_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_18_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_19_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_20_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_21_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_22_with_corrections.txt'))
extrapolated_enthalpies.append(np.loadtxt(path_to_extrapolated+'/expdata_23_with_corrections.txt'))


# In[ ]:


####################
############ 
####################

fig, ax = plt.subplots(figsize=(12,8))

x=np.arange(0,23,1)

dh_max=np.zeros(23)
dh_min=np.zeros(23)

for i in range(23):  
    dh_max[i]=np.max(extrapolated_enthalpies[i])
    dh_min[i]=np.min(extrapolated_enthalpies[i])

    
for k,j in enumerate(x):
    s=extrapolated_enthalpies[k]
    len_s=s.size
    for i in range(len_s):
        #plt.errorbar(j-0.2,s[i],xerr=0.2,capsize=0,lw=1.5,c='black',alpha=0.7)
        plt.errorbar(j-0.2,dh_max[k],xerr=0.2,capsize=0,lw=1.5,c='black',alpha=0.8)
        plt.errorbar(j-0.2,dh_min[k],xerr=0.2,capsize=0,lw=1.5,c='black',alpha=0.8)

for i,k in enumerate(x):
    ax.add_patch(Rectangle((k-0.2-0.2, dh_min[i]), 0.4, dh_max[i]-dh_min[i], color='goldenrod',alpha=1.,linewidth=0.1,ec='black',lw=1.5)) # (x, y), width, height

for i in range(23):
    num=int(extrapolated_enthalpies[i].size)
    if(i==14 or i==15):
        num=num-1
    plt.text(i-0.44, dh_min[i]-5. , str(num),fontsize=10,weight='medium')
    
for i,j in enumerate(x):
    #plt.errorbar(j+0.2,-dmc[i,0]-vib_dhb[i,0]-vib_dhb[i,1],yerr=dmc[i,1],xerr=0.2,capsize=0,lw=1.5,c='#0119cb')
    plt.errorbar(j+0.2,-dmc[i,0]-vib_dhb[i,0]-vib_dhb[i,1]-6-dhb_error[i,1],xerr=0.2,capsize=0,lw=1.5,c='#0119cb')
    plt.errorbar(j+0.2,-dmc[i,0]-vib_dhb[i,0]-vib_dhb[i,1]+6+dhb_error[i,1],xerr=0.2,capsize=0,lw=1.5,c='#0119cb')

for i,k in enumerate(x):
    ax.add_patch(Rectangle((k-0.2+0.2, -dmc[i,0]-vib_dhb[i,0]-vib_dhb[i,1]-6-dhb_error[i,1]), 0.4, 2*(6+dhb_error[i,1]), color='#6cd6ff',alpha=1.,ec='#0119cb',lw=1.5)) # (x, y), width, height

plt.ylabel('Sublimation Enthalpy  [kJ/mol]',**axis_font)
plt.xticks(x,names,rotation=90,**axis_font)

yt=np.arange(20,200,20)
plt.yticks(yt,fontsize=18)

plt.ylim([18,180])

custom_lines = [Line2D([0], [0], color='black', lw=4),
                Line2D([0], [0], color='#0119cb', lw=4)]
import matplotlib.patches as mpatches
exp_patch = mpatches.Patch(facecolor='goldenrod', edgecolor='black', lw=1.5, label='Experiments')
comp_patch = mpatches.Patch(facecolor='#6cd6ff', edgecolor='blue', lw=1.5,label='Computation')

plt.legend(handles=[exp_patch, comp_patch],fontsize=18,ncol=2,fancybox=False,shadow=True)
plt.grid(ls='--',lw=1.,alpha=0.5)
plt.rcParams["axes.linewidth"] = 1.5
ax.tick_params(length=6,width=1.5)
plt.tight_layout()
plt.show()

