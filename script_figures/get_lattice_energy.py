#!/usr/bin/env python
# coding: utf-8

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


####################################################


fig, (ax1, ax2) = plt.subplots(2,1,figsize=(14,11),sharex=True,gridspec_kw={'height_ratios': [1, 2]})

x=np.arange(23)
blue='#0057e7'

#plot 1
p_dmc=ax1.errorbar(x,dmc[:,0],dmc[:,1],fmt='o--',lw=1.5,capsize=8,ms=12,label='DMC (this work)',mfc='none',mew=2.,c=blue)
ax1.set_ylabel('$\mathrm{E}^{\mathrm{DMC}}_{\mathrm{latt}}$ [kJ/mol]',fontsize=22,fontname='arial')

yt=np.arange(-160,0,20)
ax1.set_yticks(yt)

ax1.set_ylim([-165,-20])
ax1.tick_params(axis='y', labelsize=18)


#plot 2
AVERAGES=dmc[:,0]

# plot exp
#####
for j in range(23):
    s_extra=extrapolated_enthalpies[j]# -AVERAGES[j]
    len_s=s_extra.size
    if(len_s==1):
        for i in range(len_s):
            ax2.plot(j-0.3,-(s_extra+vib_dhb[j,0]+vib_dhb[j,1])-AVERAGES[j],marker='o',c='black')
    else:
        for i in range(len_s):
            ax2.plot(j-0.3,-(s_extra[i]+vib_dhb[j,0]+vib_dhb[j,1])-AVERAGES[j],marker='o',lw=1.5,c='black')                    

dh_max_extra=np.zeros(23)
dh_min_extra=np.zeros(23)
dh_max=np.zeros(23)
dh_min=np.zeros(23)

for i in range(23):
    dh_max_extra[i]=np.max(extrapolated_enthalpies[i])#-np.average(extrapolated_enthalpies[i]))
    dh_min_extra[i]=np.min(extrapolated_enthalpies[i])#-np.average(extrapolated_enthalpies[i]))
    dh_max[i]=dh_max_extra[i]
    dh_min[i]=dh_min_extra[i]
    
for i in range(23):
    ax2.add_patch(Rectangle((i-0.3, -(dh_max[i]+vib_dhb[i,0]+vib_dhb[i,1])-AVERAGES[i]), 0.6, dh_max[i]-dh_min[i], facecolor='goldenrod',alpha=0.7,linewidth=1.5,edgecolor='black')) # (x, y), width, height

for i in range(23):
    num=int(extrapolated_enthalpies[i].size)
    if(i==3 or i==14 or i==15):
        num=num-1
    ax2.text(i-0.2, -(dh_max[i]+vib_dhb[i,0]+vib_dhb[i,1])-AVERAGES[i] -2.7 , str(num),fontsize=12,weight='medium')
    
    
##plot theory
#RPA
red='#fc3129'
averages_rpa=[]
for j in range(len(rpa)):
    averages_rpa.append(AVERAGES[int(rpa[j,0])])
averages_rpa=np.array(averages_rpa)
ax2.errorbar(rpa[:,0]+0.3,rpa[:,1]-averages_rpa[:],fmt='s',lw=1.5,capsize=8,ms=8,label='RPA+GWSE',mew=1.,c=red,mec='black')
#CC
green='#09672b'
green2='#26de00'
orange='#ff7f01'

averages_emb=[]
for j in range(len(embcc)):
    averages_emb.append(AVERAGES[int(embcc[j,0])])
averages_emb=np.array(averages_emb)
ax2.errorbar(embcc[:,0]+0.3,embcc[:,1]-averages_emb[:],fmt='^',lw=1.5,capsize=8,ms=8,label='$\Delta$CCSD(T)',mew=1.,c=green2,mec='black') #benzene CC



plt.errorbar(ccsdtcbs[0]+0.3,ccsdtcbs[1]-AVERAGES[5],fmt='^',lw=1.5,capsize=8,ms=8,label='CCSD(T)/CBS',mew=1.,c=green,mec='black') #benzene CC
#DMC
p_dmc=plt.errorbar(x+0.3,dmc[:,0]-AVERAGES[:],dmc[:,1],fmt='none',lw=1.5,capsize=8,ms=12,label='DMC (this work)',mfc='none',mew=2.,c=blue)



ax2.set_ylabel('$ \mathrm{E}_{\mathrm{latt}} - \mathrm{E}^{\mathrm{DMC}}_{\mathrm{latt}} $ [kJ/mol]',fontsize=22,fontname='arial')
plt.xticks(np.arange(0,23),names,rotation=90,fontsize=18,fontname='arial')

yt=np.arange(-30,25,5)
ax2.set_yticks(yt)

ax2.set_ylim([-30,+15])
ax2.yaxis.set_minor_locator(MultipleLocator(10))

legend_elements = [p_dmc,
                   #Line2D([0], [0], marker='o',ls='none',capsize=8,mfc='none',mec=blue,mew=2.,markersize=12,color=blue,lw=1.5, label='DMC'),
                   Line2D([0], [0], marker='s',ls='none',markersize=8,color=red,lw=1.5, mew=1.,label='RPA+GWSE',mec='black'),
                   Line2D([0], [0], marker='^',ls='none',markersize=8,color=green2, lw=1.5, mew=1.,mec='black',label='$\Delta$CCSD(T)'),
                   Line2D([0], [0], marker='^',ls='none',markersize=8,color=green, lw=1.5,mew=1., mec='black',label='CCSD(T)/CBS'),
                   Line2D([0], [0] ,color='black',marker='o', ls='none',label=r'Experiment'),
                   #Patch(facecolor='goldenrod', label=r'Range of $\Delta E^{exp}$',edgecolor='black',alpha=0.7,linewidth=1.5) 
                  ]

plt.legend(handles=legend_elements,fontsize=14,ncol=1,fancybox=False,shadow=True,loc='lower left')
ax1.grid(which='both',ls='dashed',lw=1.,alpha=0.3)
ax2.grid(which='both',ls='dashed',lw=1.,alpha=0.3)
plt.rcParams["axes.linewidth"] = 1.5
ax2.tick_params(which='major',length=6,width=1.5)
ax2.tick_params(which='minor',length=6,width=1.)
ax2.tick_params(axis='y', labelsize=18)

plt.tight_layout()
plt.show()
