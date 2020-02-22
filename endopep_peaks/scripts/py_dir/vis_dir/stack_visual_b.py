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

fig, axes = plt.subplots(nrows=3,ncols=1, sharex=True)

######
# b1 #
######

df_4 = df[['bot_id','Peak_1_B','sn_Peak_1_B']]
df_4.set_index('bot_id', inplace=True)
df_4['sn_Peak_1_B'] = df_4['sn_Peak_1_B'].fillna(df_4['sn_Peak_1_B'].min())
df_4 = df_4.round(3)
print(df_4)

z4 = df_4['sn_Peak_1_B'].min()
print(z4)
df_4['sn_Peak_1_B'] = np.where(df_4['sn_Peak_1_B']==0, z4, df_4['sn_Peak_1_B'])
print(df_4)

#fig_a2, ax_a2 = plt.subplots()
colormap_2 = LinearSegmentedColormap.from_list('colorbar', ['#00CC66','#006633'], N=1000)
norm_b = Normalize(vmin=min(df_4['sn_Peak_1_B']),vmax=max(df_4['sn_Peak_1_B']))
colors = [colormap_2(norm_b(v)) for v in df_4['sn_Peak_1_B']]
plot_4 = df_4['Peak_1_B'].plot(ax=axes[0],kind='bar', color=colors ,width=0.8, ylim=[1756.500,1763.700], fontsize=5)

plt.xticks(rotation=90)
plt.ylim([1756.500,1763.700])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

######
# b2 #
######

df_5 = df[['bot_id','Peak_2_B','sn_Peak_2_B']]
df_5.set_index('bot_id', inplace=True)
df_5['sn_Peak_2_B'] = df_5['sn_Peak_2_B'].fillna(df_5['sn_Peak_2_B'].min())
df_5 = df_5.round(3)
print(df_5)

z5 = df_5['sn_Peak_2_B'].min()
print(z5)
df_5['sn_Peak_2_B'] = np.where(df_5['sn_Peak_2_B']==0, z5, df_5['sn_Peak_2_B'])
print(df_5)

#fig_a2, ax_a2 = plt.subplots()
colormap_2 = LinearSegmentedColormap.from_list('colorbar', ['#00CC66','#006633'], N=1000)
norm_b2 = Normalize(vmin=min(df_5['sn_Peak_2_B']),vmax=max(df_5['sn_Peak_2_B']))
colors = [colormap_2(norm_b2(v)) for v in df_5['sn_Peak_2_B']]
plot_5 = df_5['Peak_2_B'].plot(ax=axes[1],kind='bar', color=colors ,width=0.8, ylim=[2277.700,2286.900], fontsize=5)

plt.xticks(rotation=90)
plt.ylim([2277.700,2286.900])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

########
# in_b #
########

df_6 = df[['bot_id','Intact_B','sn_Intact_B']]
df_6.set_index('bot_id', inplace=True)
df_6['sn_Intact_B'] = df_6['sn_Intact_B'].fillna(df_6['sn_Intact_B'].min())
df_6 = df_6.round(3)
print(df_6)

z6 = df_6['sn_Intact_B'].min()
print(z6)
df_6['sn_Intact_B'] = np.where(df_6['sn_Intact_B']==0, z6, df_6['sn_Intact_B'])
print(df_6)

#fig_a3, ax_a3 = plt.subplots()
colormap_2 = LinearSegmentedColormap.from_list('colorbar', ['#00CC66','#006633'], N=1000)
norm_b3 = Normalize(vmin=min(df_6['sn_Intact_B']),vmax=max(df_6['sn_Intact_B']))
colors = [colormap_2(norm_b3(v)) for v in df_6['sn_Intact_B']]
plot_6 = df_6['Intact_B'].plot(ax=axes[2],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([4018.400,4034.600])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

############
# together #
############

axes[0].set_title('Peak_1_B', fontsize=7, loc='left')
axes[0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1].set_title('Peak_2_B', fontsize=7, loc='left')
axes[1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2].set_title('Intact_B', fontsize=7, loc='left')
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

### b1 ###
sm_4 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b)
sm_4.set_array([])
c4 = plt.colorbar(sm_4, ax=axc[0],pad=0.05, orientation='vertical')
c4.set_label('Peak_1_B', fontsize=7)
#plt.tight_layout()

### b2 ###
sm_5 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b2)
sm_5.set_array([])
c5 = plt.colorbar(sm_5,ax=axc[1] ,pad=0.05, orientation='vertical')
c5.set_label('Peak_2_B', fontsize=7)
#plt.tight_layout()

### ib ###
sm_6 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b3)
sm_6.set_array([])
c6 = plt.colorbar(sm_6,ax=axc[2],pad=0.05 ,orientation='vertical')
c6.set_label('Intact_B', fontsize=7)
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
