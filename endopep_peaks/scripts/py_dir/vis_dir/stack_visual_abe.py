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

fig, axes = plt.subplots(nrows=6,ncols=2, sharex=True)

######
# a1 #
######

#fig_a1, ax_a1 = plt.subplots()
colormap_1 = LinearSegmentedColormap.from_list('colorbar', ['#FF9999','#990000'], N=1000)
norm = Normalize(vmin=min(df_1['sn_Peak_1_A']),vmax=max(df_1['sn_Peak_1_A']))
colors = [colormap_1(norm(v)) for v in df_1['sn_Peak_1_A']]
plot_1 = df_1['Peak_1_A'].plot(ax=axes[0,0],kind='bar', color=colors ,width=0.8, ylim=[996.800,1000.800], fontsize=5)

plt.xticks(rotation=90)
plt.ylim([996.800,1000.800])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

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
plot_2 = df_2['Peak_2_A'].plot(ax=axes[1,0],kind='bar', color=colors ,width=0.8, ylim=[2302.900,2312.100],fontsize=5)

plt.xticks(rotation=90)
plt.ylim([2302.900,2312.100])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

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
plot_3 = df_3['Intact_A'].plot(ax=axes[2,0],kind='bar', color=colors ,width=0.8, ylim=[3280.700,3293.700], fontsize=5)

plt.xticks(df.index,rotation=90)
plt.ylim([3280.700,3293.700])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

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
plot_4 = df_4['Peak_1_B'].plot(ax=axes[3,0],kind='bar', color=colors ,width=0.8, ylim=[1756.500,1763.700], fontsize=5)

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
plot_5 = df_5['Peak_2_B'].plot(ax=axes[4,0],kind='bar', color=colors ,width=0.8, ylim=[2277.700,2286.900], fontsize=5)

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
plot_6 = df_6['Intact_B'].plot(ax=axes[5,0],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([4018.400,4034.600])
plt.gcf().subplots_adjust(bottom=0.15)
plt.tight_layout()

######
# e1 #
######

df_7 = df[['bot_id','Peak_1_E','sn_Peak_1_E']]
df_7.set_index('bot_id', inplace=True)
df_7['sn_Peak_1_E'] = df_7['sn_Peak_1_E'].fillna(df_7['sn_Peak_1_E'].min())
df_7 = df_7.round(3)
print(df_7)

z6 = df_7['sn_Peak_1_E'].min()
print(z6)
df_7['sn_Peak_1_E'] = np.where(df_7['sn_Peak_1_E']==0, z6, df_7['sn_Peak_1_E'])
print(df_7)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e = Normalize(vmin=min(df_7['sn_Peak_1_E']),vmax=max(df_7['sn_Peak_1_E']))
colors = [colormap_3(norm_e(v)) for v in df_7['sn_Peak_1_E']]
plot_7 = df_7['Peak_1_E'].plot(ax=axes[0,1],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([1129.200,1133.800])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# e2 #
######

df_8 = df[['bot_id','Peak_2_E','sn_Peak_2_E']]
df_8.set_index('bot_id', inplace=True)
df_8['sn_Peak_2_E'] = df_8['sn_Peak_2_E'].fillna(df_8['sn_Peak_2_E'].min())
df_8 = df_8.round(3)
print(df_8)

z7 = df_8['sn_Peak_2_E'].min()
print(z7)
df_8['sn_Peak_2_E'] = np.where(df_8['sn_Peak_2_E']==0, z7, df_8['sn_Peak_2_E'])
print(df_8)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e2 = Normalize(vmin=min(df_8['sn_Peak_2_E']),vmax=max(df_8['sn_Peak_2_E']))
colors = [colormap_3(norm_e2(v)) for v in df_8['sn_Peak_2_E']]
plot_8 = df_8['Peak_2_E'].plot(ax=axes[1,1],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([2493.600,2503.600])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

######
# ie #
######

df_9 = df[['bot_id','Intact_E','sn_Intact_E']]
df_9.set_index('bot_id', inplace=True)
df_9['sn_Intact_E'] = df_9['sn_Intact_E'].fillna(df_9['sn_Intact_E'].min())
df_9 = df_9.round(3)
print(df_9)

z8 = df_9['sn_Intact_E'].min()
print(z8)
df_9['sn_Intact_E'] = np.where(df_9['sn_Intact_E']==0, z8, df_9['sn_Intact_E'])
print(df_9)

#fig_a3, ax_a3 = plt.subplots()
colormap_3 = LinearSegmentedColormap.from_list('colorbar', ['#FFCC66','#FFCC00'], N=1000)
norm_e3 = Normalize(vmin=min(df_9['sn_Intact_E']),vmax=max(df_9['sn_Intact_E']))
colors = [colormap_3(norm_e3(v)) for v in df_9['sn_Intact_E']]
plot_9 = df_9['Intact_E'].plot(ax=axes[2,1],kind='bar', color=colors ,width=0.8)

plt.xticks(rotation=90)
plt.ylim([3607.800,3622.200])
plt.gcf().subplots_adjust(bottom=0.15)
plt.gca().get_xticklabels()[0].set_color('red')
plt.gca().get_xticklabels()[1].set_color('red')
plt.gca().get_xticklabels()[2].set_color('red')
plt.tight_layout()

############
# together #
############

axes[0,0].set_title('Peak_1_A', fontsize=7, loc='left')
axes[0,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1,0].set_title('Peak_2_A', fontsize=7, loc='left')
axes[1,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2,0].set_title('Intact_A', fontsize=7, loc='left')
axes[2,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[3,0].set_title('Peak_1_B', fontsize=7, loc='left')
axes[3,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[4,0].set_title('Peak_2_B', fontsize=7, loc='left')
axes[4,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[5,0].set_title('Intact_B', fontsize=7, loc='left')
axes[5,0].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=True)
axes[5,0].get_xticklabels()[0].set_color('red')
axes[5,0].get_xticklabels()[1].set_color('red')
axes[5,0].get_xticklabels()[2].set_color('red')
axes[0,1].set_title('Peak_1_E', fontsize=7, loc='left')
axes[0,1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[1,1].set_title('Peak_2_E', fontsize=7, loc='left')
axes[1,1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
axes[2,1].set_title('Intact_E', fontsize=7, loc='left')
axes[2,1].tick_params(axis='x', labelsize=4, bottom=True,top=False,labelbottom=False)
x_axis = axes[5,1].axes.get_xaxis()
x_axis.set_label_text('bot_id')
x_label = x_axis.get_label()
x_label.set_visible(False)
axes[0,0].tick_params(axis='y', labelsize=7)
axes[1,0].tick_params(axis='y', labelsize=7)
axes[2,0].tick_params(axis='y', labelsize=7)
axes[3,0].tick_params(axis='y', labelsize=7)
axes[4,0].tick_params(axis='y', labelsize=7)
axes[5,0].tick_params(axis='y', labelsize=7)
axes[0,1].tick_params(axis='y', labelsize=7)
axes[1,1].tick_params(axis='y', labelsize=7)
axes[2,1].tick_params(axis='y', labelsize=7)

fig.delaxes(axes[3,1])
fig.delaxes(axes[4,1])
fig.delaxes(axes[5,1])

axes[0,0].set_facecolor('#D4D4D4')
axes[1,0].set_facecolor('#D4D4D4')
axes[2,0].set_facecolor('#D4D4D4')
axes[3,0].set_facecolor('#D4D4D4')
axes[4,0].set_facecolor('#D4D4D4')
axes[5,0].set_facecolor('#D4D4D4')
axes[0,1].set_facecolor('#D4D4D4')
axes[1,1].set_facecolor('#D4D4D4')
axes[2,1].set_facecolor('#D4D4D4')

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

x_axis = axes[0,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)
x_axis = axes[1,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)
x_axis = axes[2,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)
x_axis = axes[3,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)
x_axis = axes[4,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)
x_axis = axes[5,0].axes.get_xaxis()
x_label = x_axis.get_label()
x_label.set_visible(False)

date = time.strftime("%m.%d.%Y")
fig.savefig('Peak_Values'+'_'+date+'.png',dpi=900)
#mng = plt.get_current_fig_manager()
#mng.window.showMaximized()
#plt.show()

###########################
# Separate colorbar plots #
###########################

fig_2, axc = plt.subplots(nrows=4,ncols=3,constrained_layout=False, sharex=True)

### a1 ###
sm = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm)
sm.set_array([])
c1 = plt.colorbar(sm, ax=axc[0,0] ,pad=0.05, orientation='vertical')
c1.set_label('Peak_1_A', fontsize=7)
#plt.tight_layout()

### a2 ###
sm_2 = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm_a2)
sm_2.set_array([])
c2 = plt.colorbar(sm_2,ax=axc[0,1] ,pad=0.05, orientation='vertical')
c2.set_label('Peak_2_A', fontsize=7)
#plt.tight_layout()

### ia ###
sm_3 = plt.cm.ScalarMappable(cmap=colormap_1, norm=norm_a3)
sm_3.set_array([])
c3 = plt.colorbar(sm_3,ax=axc[0,2] , pad=0.05, orientation='vertical')
c3.set_label('Intact_A', fontsize=7)
#plt.tight_layout()

### b1 ###
sm_4 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b)
sm_4.set_array([])
c4 = plt.colorbar(sm_4, ax=axc[1,0],pad=0.05, orientation='vertical')
c4.set_label('Peak_1_B', fontsize=7)
#plt.tight_layout()

### b2 ###
sm_5 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b2)
sm_5.set_array([])
c5 = plt.colorbar(sm_5,ax=axc[1,1] ,pad=0.05, orientation='vertical')
c5.set_label('Peak_2_B', fontsize=7)
#plt.tight_layout()

### ib ###
sm_6 = plt.cm.ScalarMappable(cmap=colormap_2, norm=norm_b3)
sm_6.set_array([])
c6 = plt.colorbar(sm_6,ax=axc[1,2],pad=0.05 ,orientation='vertical')
c6.set_label('Intact_B', fontsize=7)
#plt.tight_layout()

### e1 ###
sm_7 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e)
sm_7.set_array([])
c7 = plt.colorbar(sm_7,ax=axc[2,0],pad=0.05 ,orientation='vertical')
c7.set_label('Peak_1_E', fontsize=7)

### e2 ###
sm_8 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e2)
sm_8.set_array([])
c8 = plt.colorbar(sm_8,ax=axc[2,1],pad=0.05 ,orientation='vertical')
c8.set_label('Peak_2_E', fontsize=7)

### ie ###
sm_9 = plt.cm.ScalarMappable(cmap=colormap_3, norm=norm_e3)
sm_9.set_array([])
c9 = plt.colorbar(sm_9,ax=axc[2,2],pad=0.05 ,orientation='vertical')
c9.set_label('Intact_E', fontsize=7)


fig_2.delaxes(axc[0,0])
fig_2.delaxes(axc[0,1])
fig_2.delaxes(axc[0,2])
fig_2.delaxes(axc[1,0])
fig_2.delaxes(axc[1,1])
fig_2.delaxes(axc[1,2])
fig_2.delaxes(axc[2,0])
fig_2.delaxes(axc[2,1])
fig_2.delaxes(axc[2,2])
fig_2.delaxes(axc[3,0])
fig_2.delaxes(axc[3,1])
fig_2.delaxes(axc[3,2])
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
