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

fig, axes = plt.subplots(nrows=3,ncols=1, sharex=True)

######
# f1 #
######

df_10 = df[['bot_id','Peak_1_F','sn_Peak_1_F']]
df_10.set_index('bot_id', inplace=True)
df_10['sn_Peak_1_F'] = df_10['sn_Peak_1_F'].fillna(df_10['sn_Peak_1_F'].min())
df_10 = df_10.round(3)
print(df_10)

z9 = df_10['sn_Peak_1_F'].min()
print(z9)
df_10['sn_Peak_1_F'] = np.where(df_10['sn_Peak_1_F']==0, z9, df_10['sn_Peak_1_F'])
print(df_10)

#fig_a3, ax_a3 = plt.subplots()
colormap_4 = LinearSegmentedColormap.from_list('colorbar', ['#66CCFF','#003366'], N=1000)
norm_f = Normalize(vmin=min(df_10['sn_Peak_1_F']),vmax=max(df_10['sn_Peak_1_F']))
colors = [colormap_4(norm_f(v)) for v in df_10['sn_Peak_1_F']]
plot_10 = df_10['Peak_1_F'].plot(ax=axes[0],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([1342.500,1347.900])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# f2 #
######

df_11 = df[['bot_id','Peak_2_F','sn_Peak_2_F']]
df_11.set_index('bot_id', inplace=True)
df_11['sn_Peak_2_F'] = df_11['sn_Peak_2_F'].fillna(df_11['sn_Peak_2_F'].min())
df_11 = df_11.round(3)
print(df_11)

z10 = df_11['sn_Peak_2_F'].min()
print(z10)
df_11['sn_Peak_2_F'] = np.where(df_11['sn_Peak_2_F']==0, z10, df_11['sn_Peak_2_F'])
print(df_11)

#fig_a3, ax_a3 = plt.subplots()
colormap_4 = LinearSegmentedColormap.from_list('colorbar', ['#66CCFF','#003366'], N=1000)
norm_f2 = Normalize(vmin=min(df_11['sn_Peak_2_F']),vmax=max(df_11['sn_Peak_2_F']))
colors = [colormap_4(norm_f2(v)) for v in df_11['sn_Peak_2_F']]
plot_11 = df_11['Peak_2_F'].plot(ax=axes[1],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([3777.300,3792.500])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# if #
######

df_12 = df[['bot_id','Intact_F','sn_Intact_F']]
df_12.set_index('bot_id', inplace=True)
df_12['sn_Intact_F'] = df_12['sn_Intact_F'].fillna(df_12['sn_Intact_F'].min())
df_12 = df_12.round(3)
print(df_12)

z11 = df_12['sn_Intact_F'].min()
print(z11)
df_12['sn_Intact_F'] = np.where(df_12['sn_Intact_F']==0, z11, df_12['sn_Intact_F'])
print(df_12)

#fig_a3, ax_a3 = plt.subplots()
colormap_4 = LinearSegmentedColormap.from_list('colorbar', ['#66CCFF','#003366'], N=1000)
norm_f3 = Normalize(vmin=min(df_12['sn_Intact_F']),vmax=max(df_12['sn_Intact_F']))
colors = [colormap_4(norm_f3(v)) for v in df_12['sn_Intact_F']]
plot_12 = df_12['Intact_F'].plot(ax=axes[2],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([5100.800,5121.200])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

############
# together #
############

axes[0].set_title('Peak_1_F', fontsize=7, loc='left')
axes[0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1].set_title('Peak_2_F', fontsize=7, loc='left')
axes[1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2].set_title('Intact_F', fontsize=7, loc='left')
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

### f1 ###
sm_10 = plt.cm.ScalarMappable(cmap=colormap_4, norm=norm_f)
sm_10.set_array([])
c10 = plt.colorbar(sm_10,ax=axc[0],pad=0.05 ,orientation='vertical')
c10.set_label('Peak_1_F', fontsize=7)

### f2 ###
sm_11 = plt.cm.ScalarMappable(cmap=colormap_4, norm=norm_f2)
sm_11.set_array([])
c11 = plt.colorbar(sm_11,ax=axc[1],pad=0.05 ,orientation='vertical')
c11.set_label('Peak_2_F', fontsize=7)

### if ###
sm_12 = plt.cm.ScalarMappable(cmap=colormap_4, norm=norm_f3)
sm_12.set_array([])
c12 = plt.colorbar(sm_12,ax=axc[2],pad=0.05 ,orientation='vertical')
c12.set_label('Intact_F', fontsize=7)

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
