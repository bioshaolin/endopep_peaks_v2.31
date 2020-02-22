import os
import sys
import argparse
import subprocess
import re
import glob
import shlex
import operator
from collections import defaultdict
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, Normalize
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1 import make_axes_locatable


df_0 = pd.read_csv("endo.csv")
df_00 = pd.read_csv("~/endopep_peaks/scripts/py_dir/vis_dir/reference.csv")
df = pd.concat([df_00,df_0],ignore_index=True)
df_1 = df[['bot_id','Peak_1_A','sn_Peak_1_A']]
df_1.set_index('bot_id', inplace=True)
df_1['sn_Peak_1_A'] = df_1['sn_Peak_1_A'].fillna(df_1['sn_Peak_1_A'].min())
df_1 = df_1.round(3)
print(df_1)

z = df_1['sn_Peak_1_A'].min()
print(z)
df_1['sn_Peak_1_A'] = np.where(df_1['sn_Peak_1_A']==0, z, df_1['sn_Peak_1_A'])
print(df_1)

fig, axes = plt.subplots(nrows=3,ncols=1, sharex=True)

######
# a1 #
######

#fig_a1, ax_a1 = plt.subplots()
colormap_1 = LinearSegmentedColormap.from_list('colorbar', ['#FF9999','#990000'], N=1000)
norm = Normalize(vmin=min(df_1['sn_Peak_1_A']),vmax=max(df_1['sn_Peak_1_A']))
colors = [colormap_1(norm(v)) for v in df_1['sn_Peak_1_A']]
plot_1 = df_1['Peak_1_A'].plot(ax=axes[0],kind='bar', color=colors ,width=0.8, ylim=[996.800,1000.800], fontsize=5)

plt.xticks(rotation=90)
plt.ylim([996.800,1000.800])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()
'''
sm = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm)
sm.set_array([])
plt.colorbar(sm, pad=0.05, orientation='vertical')
'''
######
# a2 #
######

df_2 = df[['bot_id','Peak_2_A','sn_Peak_2_A']]
df_2.set_index('bot_id', inplace=True)
df_2['sn_Peak_2_A'] = df_2['sn_Peak_2_A'].fillna(df_2['sn_Peak_2_A'].min())
df_2 = df_2.round(3)
print(df_2)

z2 = df_2['sn_Peak_2_A'].min()
print(z2)
df_2['sn_Peak_2_A'] = np.where(df_2['sn_Peak_2_A']==0, z2, df_2['sn_Peak_2_A'])
print(df_2)

#fig_a2, ax_a2 = plt.subplots()
colormap_2 = LinearSegmentedColormap.from_list('colorbar', ['#FF9999','#990000'], N=1000)
norm_a2 = Normalize(vmin=min(df_2['sn_Peak_2_A']),vmax=max(df_2['sn_Peak_2_A']))
colors = [colormap_2(norm_a2(v)) for v in df_2['sn_Peak_2_A']]
plot_2 = df_2['Peak_2_A'].plot(ax=axes[1],kind='bar', color=colors ,width=0.8, ylim=[2302.900,2312.100],fontsize=5)

plt.xticks(rotation=90)
plt.ylim([2302.900,2312.100])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()
'''
sm_2 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_a2)
sm_2.set_array([])
plt.colorbar(sm_2, pad=0.05, orientation='vertical')
'''
########
# in_a #
########

df_3 = df[['bot_id','Intact_A','sn_Intact_A']]
df_3.set_index('bot_id', inplace=True)
df_3['sn_Intact_A'] = df_3['sn_Intact_A'].fillna(df_3['sn_Intact_A'].min())
df_3 = df_3.round(3)
print(df_3)

z3 = df_3['sn_Intact_A'].min()
print(z3)
df_3['sn_Intact_A'] = np.where(df_3['sn_Intact_A']==0, z3, df_3['sn_Intact_A'])
print(df_3)

#fig_a3, ax_a3 = plt.subplots()
colormap_1 = LinearSegmentedColormap.from_list('colorbar', ['#FF9999','#990000'], N=1000)
norm_a3 = Normalize(vmin=min(df_3['sn_Intact_A']),vmax=max(df_3['sn_Intact_A']))
colors = [colormap_1(norm_a3(v)) for v in df_3['sn_Intact_A']]
plot_3 = df_3['Intact_A'].plot(ax=axes[2],kind='bar', color=colors ,width=0.8, ylim=[3280.700,3293.700], fontsize=5)

plt.xticks(df.index,rotation=90)
plt.ylim([3280.700,3293.700])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()
'''
sm_3 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_a3)
sm_3.set_array([])
plot = plt.colorbar(sm_3, pad=0.05, orientation='vertical')
'''
############
# together #
############

axes[0].set_title('Peak_1_A', fontsize=7, loc='left')
axes[0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1].set_title('Peak_2_A', fontsize=7, loc='left')
axes[1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2].set_title('Intact_A', fontsize=7, loc='left')
axes[2].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=True)
axes[2].get_xticklabels()[0].set_color('red')
axes[2].get_xticklabels()[1].set_color('red')
axes[2].get_xticklabels()[2].set_color('red')
axes[0].tick_params(axis='y', labelsize=7)
axes[1].tick_params(axis='y', labelsize=7)
axes[2].tick_params(axis='y', labelsize=7)

x_axis = axes[2].axes.get_xaxis()
x_axis.set_label_text('bot_id')
x_label = x_axis.get_label()
x_label.set_visible(False)

axes[0].set_facecolor('#D4D4D4')
axes[1].set_facecolor('#D4D4D4')
axes[2].set_facecolor('#D4D4D4')


fig.set_facecolor('#ECECEC')
lower_bg_1 = patches.Rectangle((0, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_2 = patches.Rectangle((0.25, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_3 = patches.Rectangle((0.50, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_4 = patches.Rectangle((0.75, 0.0), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
lower_bg_5 = patches.Rectangle((0, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_6 = patches.Rectangle((0.25, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_7 = patches.Rectangle((0.50, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_8 = patches.Rectangle((0.75, 0.99), width=0.25, height=0.01,\
transform=fig.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
fig.patches.extend([lower_bg_1,lower_bg_2,lower_bg_3,lower_bg_4,\
lower_bg_5,lower_bg_6,lower_bg_7,lower_bg_8])

fig.text(0.0,0.003, '*Reference measurements are mean values of specimen-type validations.', fontsize=6)
fig.suptitle('Peak Values', fontsize=10,x=0.5 ,y=1, weight='bold')
fig.tight_layout()


date = time.strftime("%m.%d.%Y")
fig.savefig('Peak_Values'+'_'+date+'.png',dpi=900)
#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
#plt.show()

###########################
# Separate colorbar plots #
###########################

fig_2, axc = plt.subplots(nrows=1,ncols=3,constrained_layout=False, sharex=True)

### a1 ###
sm = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm)
sm.set_array([])
c1 = plt.colorbar(sm, ax=axc[0] ,pad=0.05, orientation='vertical')
c1.set_label('Peak_1_A', fontsize=7)
#plt.tight_layout()

### a2 ###
sm_2 = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm_a2)
sm_2.set_array([])
c2 = plt.colorbar(sm_2,ax=axc[1] ,pad=0.05, orientation='vertical')
c2.set_label('Peak_2_A', fontsize=7)
#plt.tight_layout()

### ia ###
sm_3 = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm_a3)
sm_3.set_array([])
c3 = plt.colorbar(sm_3,ax=axc[2] , pad=0.05, orientation='vertical')
c3.set_label('Intact_A', fontsize=7)
#plt.tight_layout()

fig_2.delaxes(axc[0])
fig_2.delaxes(axc[1])
fig_2.delaxes(axc[2])
fig_2.suptitle('SN Gradient Legend', fontsize=10, y=1, weight='bold')

fig_2.set_facecolor('#D4D4D4')
lower_bg_1 = patches.Rectangle((0, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_2 = patches.Rectangle((0.25, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_3 = patches.Rectangle((0.50, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_4 = patches.Rectangle((0.75, 0.0), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
lower_bg_5 = patches.Rectangle((0, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FF9999',edgecolor='none',zorder=0)
lower_bg_6 = patches.Rectangle((0.25, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#00CC66',edgecolor='none',zorder=0)
lower_bg_7 = patches.Rectangle((0.50, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#FFCC66',edgecolor='none',zorder=0)
lower_bg_8 = patches.Rectangle((0.75, 0.99), width=0.25, height=0.01,\
transform=fig_2.transFigure,facecolor='#66CCFF',edgecolor='none',zorder=0)
fig_2.patches.extend([lower_bg_1,lower_bg_2,lower_bg_3,lower_bg_4,\
lower_bg_5,lower_bg_6,lower_bg_7,lower_bg_8])
fig_2.tight_layout()


#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
fig_2.savefig('SN_Gradient_Legend'+'_'+date+'.png',dpi=900)
plt.show()
