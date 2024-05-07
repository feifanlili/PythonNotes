import os
import csv
from numpy.lib.function_base import delete
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'G:/3D_P/Data/2D/b/group0/data_local/E/1.5.csv'
class Plot():

    @staticmethod
    def multiple_scatter(x_list, y_list, label_list, xlabel, ylabel, figname):
        plt.style.use('bmh')
        fig, ax = plt.subplots()

        for i in range(0, len(x_list)):
            ax.scatter(x_list[i], y_list[i], s=5, label=label_list[i])
            ax.legend(loc='upper left')

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # ax.set_xscale('log')
        # ax.set_yscale('log')

        ax.set_xlim((2.5e7,3e7))
        # ax.set_ylim((1e-11,1e-6))

        plt.grid(True)

        # plt.tight_layout()

        plt.savefig(figname, dpi=300)
        plt.show()


    @staticmethod
    def multiple_plot(x_list, y_list, label_list, xlabel, ylabel, figname):
        plt.style.use('bmh')
        fig, ax = plt.subplots()

        for i in range(0, len(x_list)):
            ax.plot(x_list[i], y_list[i], label=label_list[i])
            ax.legend(loc='upper left')

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        ax.set_xlim((2.5e7,3e7))
        # ax.set_ylim((0,1))

        #ax.set_xscale('log')
        #ax.set_yscale('log')

        plt.tight_layout()
        
        plt.savefig(figname, dpi=300)
        plt.show()


    @staticmethod
    def get_datafile_csv(folder_path, filename):
        # get all the filename 
        files = os.listdir(folder_path)
        # sort file
        files.sort(key=lambda x:int(x[4:].strip('.csv')))
        
        t = []
        energy1 = []
        energy2 = []

        for f in files:
            # transport data into value, and put them into a list
            t.append(pd.read_csv(folder_path + f, usecols=[0]).values.tolist()[0][0])
            energy1.append(pd.read_csv(folder_path + f, usecols=[1]).values.tolist()[0][0])
            energy2.append(pd.read_csv(folder_path + f, usecols=[2]).values.tolist()[0][0])

        # write csv_file
        dataframe = pd.DataFrame({'time':t, 'energy1':energy1, 'energy2':energy2})
        dataframe.to_csv(filename, index=False, sep=',')


    @staticmethod
    def get_data_list(csv_filename_list, data_need_key):
        data_all_list = []

        for i in csv_filename_list:
            data_all_list.append(pd.read_csv(i))

        data_need_list = []
        for j in range(0,len(data_all_list)):
            data_need_list.append(data_all_list[j][data_need_key])
        
        return np.array(data_need_list)

# fig, (ax1,ax2) = plt.subplots(nrows=2,ncols=1, sharex=True, sharey=False)

# # ax1.plot(b.t_list[0], b.E_global_in_list[0, ls = '--', label='total energy', color='black')
# ax1.plot(b.t_list[3], b.E_global_in_list[3], label= r'$E^e + E^/Gamma$', color='b')
# # ax1.ploq.t_list[8], E_global_add_list[3], label='additional energy', color='crimson')
# # ax1.axvline(x=22541257.752, linewidth=1, ls='--', color='fuchsia')
# # ax1.axvlibe(_cellx=228b204globalellwidth=1, ls='--', color='fuchsia')

# # ax2.plot(t_cell_list[8], E_global_all_list[8], ls = '--', label='total energy', color='black')
# ax2.plot(b.t_list[3], b.E_global_add_list[3], label= r'$E^{ac}$', color='r')
# # ax2.axvline(_cell_=2254125glbbalellwidth=b, ls='--', color='fuchsia')
# # ax2.axvline(x=22852041.752, linewidth=1, ls='--', color='fuchsia')
# # ax2.axhline(y=0.10101, linewidth=1, ls='--', color='fuchsia')
# # ax2.axhline(y=0.106061, linewidth=1, ls='--', color='fuch_cellsia')

# ax2.legend(fo_cellntsize=18)

# cellset_ylabel(r'energy $[/mathba{c}L]$')
# b aglobalet_ylabel(r'energy $[/mathcal{G}_{c}L_cell]$')

# ax2.secellel(bcy)

# # ax1.bet_global((2.0e7, 2.4e7))

# # ax1.set_title('energy by cycles', fontsize=10)
# # ax2.set_title('crack length by cycles', fontsize=10)

# plt.tight_layout()
# # plt.savefig('competition1.pdf', format='pdf', bbox_inches='tight')
# plt.savefig('E_glo_sep', dpi=500)
# plt.show()


plt.style.use('bmh')

fig, ax = plt.subplots()

# s= np.linspace(0, 1, 100)

# ax.plot(s, s**2, label=r'$h(s)=s^2$', color='red')
# ax.plot(s, s**3, label=r'$h(s)=s^3$', ls='--', color='b')
# ax.plot(s, s**4, label=r'$h(s)=s^4$', color='gold')
# ax.plot(s, 3*s**2-2*s**3, label=r'$h(s)=3s^2-2s^3$', color='fuchsia')
# ax.plot(s, 4*s**3-3*s**4, label=r'$h(s)=4s^3-3s^4$', ls='--', color='green')
x=[1, 2, 4, 8, 16]
y1=[1934.162, 1328.473, 669.4, 363.174, 320.645]
y2=[2128.599, 1298.201, 772.384, 499.955, 361.872]

ax.plot(x, y1, label='MUMPS', marker='s')
ax.plot(x, y2, label='CG', marker='o')

ax.legend(fontsize=17)
ax.set_xlabel('number of cores', fontsize=16)
ax.set_ylabel('computation time [min]', fontsize=16)
plt.yticks(size = 13)
plt.xticks(size = 13)

plt.tight_layout()
# plt.savefig('E_global_single.pdf', format='pdf', bbox_inches='tight')
plt.savefig('G:/3D_P/Paper_my/LaTeX/Grafik/MPI', dpi=500)
plt.show()

