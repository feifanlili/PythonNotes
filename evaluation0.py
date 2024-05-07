import numpy as np
import pandas as pd
import os
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
from scipy.optimize import curve_fit

class evaluation():
    def __init__(self, name, value_list,
                vorpath_all, vorpath_cell, vorpath_point):
        self.name = name
        self.value_list = value_list

        self.filename_all_list = []
        self.filename_global_list = []
        self.filename_point_list = []
        self.label_list = []

        self.t_tip_list = []
        self.tip_new_list = []
        # self.E_global_add_new_list = []
        # self.E_global_in_new_list = []
        
        self.DeltaK_list = []
        self.rate_list = []

        for i in self.value_list:
            self.filename_all_list.append(vorpath_all + str(i) + '.csv')     
            self.filename_global_list.append(vorpath_cell + str(i) + '.csv')
            self.filename_point_list.append(vorpath_point + str(i) + '.csv')   
            self.label_list.append(self.name + '=' + str(i))
        
        self.t_list = self.get_data_list(self.filename_all_list, 'time')
        self.a_list = self.get_data_list(self.filename_all_list, 'crack_len')
       
        self.tip_old_list = self.get_data_list(self.filename_all_list, 'crack_tip')
        self.E_global_add_list = self.get_data_list(self.filename_all_list, 'potin_sum')
        self.E_global_in_list = self.get_data_list(self.filename_all_list, 'potadd_sum')
        self.E_global_all_list = np.array(self.E_global_in_list) + np.array(self.E_global_add_list)

        self.t_cell_list = self.get_data_list(self.filename_global_list, 'time')
        self.E_cell_add_list = self.get_data_list(self.filename_global_list, 'E_add')
        self.E_cell_in_list = self.get_data_list(self.filename_global_list, 'E_in')
        self.E_cell_all_list = np.array(self.E_cell_add_list) + np.array(self.E_cell_in_list)

        for j in range(0,len(self.t_list)):
            self.pointdata = self.get_point(self.t_list[j],self.tip_old_list[j])
            self.t_tip_list.append(self.pointdata[0])
            self.tip_new_list.append(self.pointdata[1])
            # self.E_global_add_new_list.append(self.pointdata[2])
            # self.E_global_in_new_list.append(self.pointdata[3])

            self.DeltaK = self.compute_stress_intensity_factor_square(self.pointdata[1], 0.002)
            self.DeltaK = np.delete(self.DeltaK,[0])
            self.DeltaK_list.append(self.DeltaK)

            crack_growth_rate = []
            for j in range(0,len(self.pointdata[0])-1):
                da = self.pointdata[1][j+1] - self.pointdata[1][j]
                dt = self.pointdata[0][j+1] - self.pointdata[0][j]
                crack_growth_rate.append(da/dt)
            self.rate_list.append(crack_growth_rate)
        

    @staticmethod
    def compute_lame_parameters(E, nu):
        lam = E * nu / ((1+nu)*(1-2*nu))
        mu  = E / (2*(1+nu))
        return lam, mu

        
    @staticmethod
    def compute_paris_law(a, t, N):
        # a: crack length
        _L = 0.1
        _t = 1.
        a = a * _L
        t = t * _t
        crack_growth = []
        for i in range(0, N-1):
            da = a[i+1] - a[i]
            dt = t[i+1] - t[i]
            crack_growth.append(da / dt)  ## add term into the list
        return np.array(crack_growth)

    def compute_crack_growth_ratio(a, t, N):
        _L = 0.1
        _t = 1.
        a = a * _L
        t = t * _t
        crack_growth = []
        for i in range(0, N-1):
            da = a[i+1] - a[i]
            dt = t[i+1] - t[i]
            crack_growth.append(da / dt)
        crack_growth = np.array(crack_growth)
        ## get the position of data1, which meet the condition 0 < da/dt < 1
        index = np.nonzero(np.logical_and(1 > crack_growth, crack_growth > 0)) 
        n = len(index)
        index = np.array(index).T
        # a: crack length
        crack_growth_ratio = []
        da = a[index[0]+1] - a[1]
        dt = t[index[0]+1] - t[1]
        crack_growth_ratio.append(da / dt)
        for i in range(0, len(index)-1):
            da = a[index[i+1]+1] - a[index[i]+1]
            dt = t[index[i+1]+1] - t[index[i]+1]
            crack_growth_ratio.append(da / dt)
        return np.array(crack_growth_ratio) 


    @staticmethod
    def compute_stress_intensity_factor_ctspeciment(a, DeltaF): #DeltaK depends on cracklenth,loading,geometry
        # a: crack length
        # DeltaF: applied force
        _L = 1
        _t = 1
        a = a * _L
        L = 1.2 * _L
        B = 0.25* L
        
        alpha = a/L
        lam, nu = evaluation.compute_lame_parameters(22.50000, 0.3)
        # print(lam)
        # print(mu)
        Gc = 2330 # J/m2
        DeltaF = math.sqrt(2*nu*Gc/_L) * DeltaF * (0.25*3.14*0.5*_L*B) * 2
        print(DeltaF/2)
        print(0.25*3.14*0.5*_L*B)
        # print(20000/math.sqrt(2*mu*Gc/_L))

        tress_intensity_factor = DeltaF / (B*np.sqrt(L)) * \
                 (2 + a/L) / pow((1 - a/L), 3/2) * \
                 (0.886 + 4.64*pow(a/L, 2) - 13.32*pow(a/L, 3) + 14.72*pow(a/L, 4) - 5.69*pow(a/L, 5))
        
        fac = 1000
        return tress_intensity_factor/1e9*fac
    
    def compute_stress_intensity_factor_square(self, a, DeltaF):
        # alpha = a/W = 0.1
        # H/W = 1.0
        _L = 1
        F_t = 1.0174
        lam, mu = evaluation.compute_lame_parameters(22.50000, 0.3)
        # print(lam)
        # print(mu)
        Gc = 2330
        DeltaF = DeltaF * 2
        sigma = DeltaF / (_L)

        tress_intensity_factor = sigma * np.sqrt(np.pi * a) * F_t
        
        return tress_intensity_factor

    @staticmethod
    def compute_energy_ratio(potadd, potin, N):
        energy_ratio = []
        for i in range(0, N):
            energy_ratio.append(potadd[i] / (potadd[i]+potin[i]))
        return np.array(energy_ratio)

    @staticmethod
    def compute_fatigue_energy(potadd, N):
        Gc = 2330
        L = 2
        fatigue_energy = []
        for i in range(0, N):
            fatigue_energy.append(potadd[i] / (Gc * L))
        return np.array(fatigue_energy)

    @staticmethod
    def compute_straiN5nergy(potin, N):
        Gc = 2330
        L = 2
        straiN5nergy = []
        for i in range(0, N):
            straiN5nergy.append(potin[i] / (Gc * L))
        return np.array(straiN5nergy)


    @staticmethod
    def read_file(filename):
        if os.path.isfile(filename):  ## to find the data1 file
            with open(filename, 'r') as f:  ## open the file in textform
                line = f.read().split('\n')
                c1 = []
                ## transform the text into data1(number)
                for i in line[:-1]:  ## to read from beginning to the end of the line
                    var = i.split(': ')
                    c1.append(float(var[0]))
            return np.array(c1)
        else:
            print('can not find ' + filename)
            exit(0)


    @staticmethod
    def get_datafile_csv(folder_path, filename):
        # get all the filename 
        files = os.listdir(folder_path)
        # sort filename
        files.sort(key=lambda x:int(x[4:].strip('.csv')))
        
        t = []
        E_add = []
        E_in = []

        for f in files:
            # transport data to value, and put them into a list
            t.append(pd.read_csv(folder_path + f, usecols=[0]).values.tolist()[0][0])
            E_add.append(pd.read_csv(folder_path + f, usecols=[1]).values.tolist()[0][0])
            E_in.append(pd.read_csv(folder_path + f, usecols=[2]).values.tolist()[0][0])

        # write csv_file
        dataframe = pd.DataFrame({'time':t, 'E_add':E_add, 'E_in':E_in})
        dataframe.to_csv(filename,index=False, sep=',')


    @staticmethod
    def get_point(t_old, tip_old):
        t_old = np.delete(t_old, [0])
        tip_old = np.delete(tip_old, [0])
        # E_add_old = np.delete(E_add_old, [0])
        # E_in_old = np.delete(E_in_old, [0]) 

        tip_new = [tip_old[0]]
        t_new = [t_old[0]]
        # E_add_new = [E_add_old[0]]
        # E_in_new = [E_in_old[0]]

        for i in range(1,len(tip_old)):
            if tip_old[i]-tip_old[i-1] == 0:
                i+=1
                # continue
            else:
                tip_new.append(float(tip_old[i]))
                t_new.append(float(t_old[i]))
                # E_add_new.append(float(E_add_old[i]))
                # E_in_new.append(float(E_in_old[i]))

        return np.array(t_new), np.array(tip_new) #, np.array(E_add_new), np.array(E_in_new)
    

    @staticmethod
    def get_data_list(filename_list, key):

        data_list_all = []
        for i in filename_list:
            data_list_all.append(pd.read_csv(i))

        data_list_need = []
        for j in range(0,len(data_list_all)):
            data_list_need.append(np.array(data_list_all[j][key]))
        
        return data_list_need


    @staticmethod
    def multiple_scatter(x_list, y_list, label_list, xlabel, ylabel, figname):
        plt.style.use('bmh')

        fig, ax = plt.subplots()

        # ax.axhline(y=0.06060606, xmin=1.3e7, xmax=1.8e7, linewidth=1, ls='--', color='b', alpha=0.5)
        # ax.axhline(y=0.09090909, linewidth=1, ls='--', color='b', alpha=0.5)
        # ax.axhline(y=0.12121212, linewidth=1, ls='--', color='b', alpha=0.5)
        if len(x_list)==1:
            ax.scatter(x_list[0], y_list[0], color='k') 
        else:
            for i in range(0, len(x_list)):  
                if i==10:
                    ax.scatter(x_list[i], y_list[i], s=35, marker='^', label=label_list[i], color='r')
                    ax.legend(loc='upper left', fontsize=12)              
                else:
                    ax.scatter(x_list[i], y_list[i], s=20, label=label_list[i])
                    ax.legend(loc='upper left', fontsize=12)

        ax.set_xlabel(xlabel, fontsize=16)
        ax.set_ylabel(ylabel, fontsize=16)

        ax.set_xscale('log')
        ax.set_yscale('log')

        ax.set_xlim((1.5e-3, 3.5e-3))
        ax.set_ylim((1.5e-10,1e-5))

        # plt.yticks(size = 12)
        # plt.xticks(size = 12)
    
        plt.tight_layout()

        plt.savefig(figname, dpi=500)
        # plt.savefig(figname + '.pdf', format='pdf', bbox_inches='tight')
        plt.show()


    @staticmethod
    def multiple_plot(x_list, y_list, label_list, xlabel, ylabel, figname):
        plt.style.use('bmh')
        fig, ax = plt.subplots()
        
        for i in range(0, len(x_list)):
            ax.plot(x_list[i], y_list[i], label=label_list[i], linewidth=2)
            ax.legend(loc='upper left')

        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)

        # ax.set_xlim((2e7, 3e7))
        # ax.set_ylim((1.5e-10,1e-5))

        #ax.set_xscale('log')
        #ax.set_yscale('log')

        plt.tight_layout()
        
        plt.savefig(figname, dpi=800)
        # plt.savefig(figname + '.pdf', format='pdf', bbox_inches='tight')
        plt.show()


    @staticmethod
    def compare_multiple_scatter(x1_list, y1_list, x2_list, y2_list,
                                label1_list, label2_list,
                                xlabel, ylabel, figname):
        plt.style.use('bmh')
        fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
        
        for i in range(0, len(x1_list)):
            if i==9:
                ax1.scatter(x1_list[i], y1_list[i], s=30, marker='^', label=label1_list[i], color='r')
                ax1.legend(loc='upper left', fontsize=7)  
            elif i==3:
                ax1.scatter(x1_list[i], y1_list[i], s=30, marker='x', label=label1_list[i], color='b')
                ax1.legend(loc='upper left', fontsize=7)                  
            else:
                ax1.scatter(x1_list[i], y1_list[i], s=12, label=label1_list[i])
                ax1.legend(loc='upper left', fontsize=7)

        for j in range(0, len(x2_list)):
            if j==10:
                ax2.scatter(x2_list[j], y2_list[j], s=30, marker='^', label=label2_list[j], color='r')
                ax2.legend(loc='upper left', fontsize=7)
            elif j==4:
                ax2.scatter(x2_list[j], y2_list[j], s=30, marker='x', label=label2_list[j], color='b')
                ax2.legend(loc='upper left', fontsize=7)
            else:
                ax2.scatter(x2_list[j], y2_list[j], s=12, label=label2_list[j])
                ax2.legend(loc='upper left', fontsize=7)
        # ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)                
        ax2.set_xlabel(xlabel)
        ax2.set_ylabel(ylabel)
        
        plt.tight_layout()

        plt.savefig(figname, dpi=500)
        # plt.savefig(figname + '.pdf', format='pdf', bbox_inches='tight')
        plt.show()

    @staticmethod
    def compare_multiple_plot(x1_list, y1_list, x2_list, y2_list,
                                label1_list, label2_list,
                                xlabel, y1label, y2label, figname):
        plt.style.use('bmh')
        fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False)
        
        for i in range(0, len(x1_list)):
            if i==9:
                ax1.plot(x1_list[i], y1_list[i], marker='^', label=label1_list[i], color='r')
                ax1.legend(loc='upper left', fontsize=7)  
            elif i==3:
                ax1.scatter(x1_list[i], y1_list[i], marker='x', label=label1_list[i], color='b')
                ax1.legend(loc='upper left', fontsize=7)                  
            else:
                ax1.plot(x1_list[i], y1_list[i], label=label1_list[i])
                ax1.legend(loc='upper left', fontsize=7)

        for j in range(0, len(x2_list)):
            if j==10:
                ax2.plot(x2_list[j], y2_list[j], marker='^', label=label2_list[j], color='r')
                ax2.legend(loc='upper left', fontsize=7)
            elif j==4:
                ax2.plot(x2_list[j], y2_list[j], s=30, marker='x', label=label2_list[j], color='b')
                ax2.legend(loc='upper left', fontsize=7)
            else:
                ax2.plot(x2_list[j], y2_list[j], label=label2_list[j])
                ax2.legend(loc='upper left', fontsize=7)
        # ax1.set_xlabel(xlabel)
        ax1.set_ylabel(y1label)  
        ax2.set_ylabel(y2label)   

        ax2.set_xlabel(xlabel)
        
        
        plt.tight_layout()
        plt.savefig(figname, dpi=300)
        # plt.savefig(figname + '.pdf', format='pdf', bbox_inches='tight')
        plt.show()
# ------------------- data1 processing ------------------- #

def get_data_all(list_object):
    for i in list_object:
        crack_tip = [0]

        t = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/t.dat')
        crack_len = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/crack_length.dat')
        crack_tip.extend(evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/crack_tip.dat'))
        potadd_sum = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/potadd_sum.dat')
        potin_sum = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/potin_sum.dat')
        sig_max = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/sig_max.dat')
        sig_min = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/sig_min.dat')
        D_max = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/D_max.dat')
        D_min = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/D_min.dat')
        dD_max = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/dD_max.dat')
        dD_min = evaluation.read_file('G:/3D_P/Data/2D/b/group0/' + str(i) +'/pfmfrac/debug/dD_min.dat')

        dataframe = pd.DataFrame({
                                    'time':t, 
                                    'crack_len': crack_len, 
                                    'crack_tip': crack_tip,
                                    'potadd_sum': potadd_sum,
                                    'potin_sum': potin_sum,
                                    'potall_sum': potadd_sum + potin_sum,
                                    'sig_max': sig_max,
                                    'sig_min': sig_min,
                                    'D_max': D_max,
                                    'D_min':D_min,
                                    'dD_max': dD_max,
                                    'dD_min': dD_min
                                    })
        dataframe.to_csv('G:/3D_P/Data/2D/b/group0/data_all/'+str(i)+'.csv',index=False, sep=',')

def modify_energy_cell(filename_global_list):
    for filename in filename_global_list:
        df = pd.read_csv(filename)
        df.columns = ['time', 'E_add', 'E_in']
        df['E_add'] = df['E_add'] * 5.051e-6
        df['E_in'] = df['E_in'] * 5.051e-6
        df.to_csv(filename, index=False)

def modify_cracktip(filename_all_list):
    for filename in filename_all_list:
        df = pd.read_csv(filename)
        filt = (df['crack_tip'] > 0.25)
        df.drop(index=df[filt].index, inplace=True)
        df.to_csv(filename, index=False)  

list_b = [1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
list_q = [10000, 20000, 30000, 40000, 50000, 100000, 150000, 200000, 250000, 300000, 350000]
list_Dc = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

b = evaluation('b', list_b, 'G:/3D_P/Data/2D/b/group0/data_all/', 
                'G:/3D_P/Data/2D/b/group0/data_local/E/',
                'G:/3D_P/Data/2D/b/group0/data_local/s/')
q = evaluation('q', list_q, 'G:/3D_P/Data/2D/q/group0/data_all/', 
                'G:/3D_P/Data/2D/q/group0/data_local/E/',
                'G:/3D_P/Data/2D/q/group0/data_local/s/')
Dc = evaluation('Dc', list_Dc, 'G:/3D_P/Data/2D/Dc/group0/data_all/', 
                'G:/3D_P/Data/2D/Dc/group0/data_local/E/',
                'G:/3D_P/Data/2D/Dc/group0/data_local/s/')
# vor='G:/3D_P/Data/2D/q/group0/'
# bot='/pfmfrac/080/res/E/'
# for item in list_q:
#     evaluation.get_datafile_csv(vor+str(item)+bot, 'G:/3D_P/Data/2D/q/group0/data_local/E/'+str(item)+'.csv')

# modify_energy_cell(q.filename_global_list)
# b.multiple_scatter([b.t_tip_list[3]], [q.t_list[8]], [b.label_list[3]], 'cycles', r'cracklength [L]', 'cracktip_0')
# evaluation.compare_multiple_scatter(b.t_tip_list, b.tip_new_list, q.t_tip_list, q.tip_new_list,
#                                     b.label_list, q.label_list, 
#                                     'cycles', r'crack length [L]', 'cracktip_compare')
# Dc.multiple_scatter(Dc.t_tip_list, Dc.tip_new_list, Dc.label_list, 'cycles', r'crack length [L]', 'cracktip_Dc')
# b.multiple_plot(b.t_list[1:10:4], b.E_global_add_list[1:10:4], b.label_list[1:10:4], 'cycles', r'$E^{ac} [\mathcal{G}_{c}L]$', 'E_global_add')
# evaluation.compare_multiple_plot(b.t_list[1:10:4], b.E_global_add_list[1:10:4], 
#                                     b.t_list[1:10:4], b.E_global_in_list[1:10:4],
#                                     b.label_list[1:10:4], b.label_list[1:10:4],
#                                     'cycles', r'$E^{ac} [\mathcal{G}_{c}L]$',
#                                     r'$E^{in} [\mathcal{G}_{c}L]$', 'E_global')

# ParisLaw
# evaluation.multiple_scatter([b.DeltaK_list[3]], [b.rate_list[3]], [b.label_list[3]], 
#                             r'$\Delta K [\sqrt{2 \mu \mathcal{G}_{c}}]$ (log)', 
#                             r'$\mathrm{d}a/\mathrm{d}N~[L]$ (log)', 
#                             'G:/3D_P/Paper_my/LaTeX/Grafik/Law0')

# Energy
# evaluation.multiple_plot(t_cell_list[0:9:8], E_global_add_list[0:9:8], label_list[0:9:8], 'cycles', r'$E [\mathcal{G}_{c}L]$', 'E_global_add_2' )

# print(mpl.rcParams.keys())

# ------------- single plot ------------- #
plt.style.use('bmh')

fig, ax = plt.subplots()

s= np.linspace(0, 1, 100)

# ax.plot(s, 2*s, label=r'$h\'(s)=2s$', color='red')
# ax.plot(s, 4*s**3, label=r'$h\'(s)=4s^3$', color='b')
# ax.plot(s, 6*s-6*s**2, label=r'$h\'(s)=6s-6s^2$', color='fuchsia')

ax.plot(s, s**2, label=r'$h(s)=s^2$', color='red')
ax.plot(s, s**4, label=r'$h(s)=s^4$', color='b')
ax.plot(s, 3*s**2-2*s**3, label=r'$h(s)=3s^2-2s^3$', color='fuchsia')

# # ax.plot(s, s**3, label=r'$h(s)=s^3$', ls='--', color='gold')
# # ax.plot(s, 4*s**3-3*s**4, label=r'$h(s)=4s^3-3s^4$', ls='--', color='green')


# # ax.plot(b.t_cell_list[3], b.E_cell_all_list[3], ls = '--', label = r'$E$', color='black')
# # ax.plot(b.t_cell_list[3], b.E_cell_in_list[3], label= r'$E^e + E^\Gamma$', color='b')
# # ax.plot(b.t_cell_list[3], b.E_cell_add_list[3], label= r'$E^{ac}$', color='r')

# ax.scatter(b.t_tip_list[3], b.tip_new_list[3], color='k')

ax.legend(loc='upper left', fontsize=16)

ax.set_xlabel('s', fontsize=15)
ax.set_ylabel('h(s)', fontsize=15)

# ax.set_xlabel('cycles', fontsize=18)
# ax.set_ylabel(r'crack length [L]', fontsize=18)
# # ax.ticklabel_format(style='sci',axis='y')
# # plt.yticks(size = 14)
# # plt.xticks(size = 14)
# # ax.set_xlim((2e7, 2.4e7))
# plt.tight_layout()
# # # # plt.savefig('E_global_single.pdf', format='pdf', bbocelles='tight')
plt.savefig('G:/3D_P/Paper_my/LaTeX/Grafik/hs_0', dpi=500)
plt.show()

# ------------- 2 plot -----------cel# 
# fig, (ax1,(ax2, ax3)) = plt.subplots(nrows=2,ncols=1, sharex=True, sharey=False)

# # yticks_top=np.linspace(0, 0.2, 5)
# # yticks_bottom=np.linspace(0, 0.003_cell, cel # ax1.plot(Dc.t_list[0], Dc.E_global_all_list[3], ls = '--', label = r'$E$', color='black')
# # ax1.scatter(b.t_tip_list[3], b.tip_new_list[3], color='k')
# ax1.plot(Dc.t_list[0], Dc.E_global_in_list[3], label= r'$E^e + E^\Gamma$', color='b')
# ax2.plot(Dc.t_list[0], Dc.E_global_add_list[3], label= r'$E^{ac}$', color='r')

# ax1.legend(fontsize=17)
# ax2.legend(fontsize=17)
# ax2.set_xlabel('cycles', fontsize=15)
# # ax1.set_ylabel(r'cr8ck length [L]', fontsize=15)
# # ax1.set_yl8bel(r'$E [\mathcal{G}_{c}L]$', fontsize=15)
# # ax2.set_ylabel(r'8E [\mathcal{G}_{c}L]$', fontsize=15)8
# # ax1.set_yticks(labelsize = 14)
# # ax2.set_ytick_cells(labelsize = 1cell ax2.set_xticks(labelsizecell
# # ax1.set_yti_cellcklabels(ytic_cellks_top)
# # ax2.set_yticklabels(yticks_bottom)
# # plt.yticks(si_cellze = 14)
# plt.xticks(size =cel# plt.tight_lay_cellout()
# # # plt.savefig('competition1.pdf', format='pdf', bbox_inches='tight')
# plt.savefig('E__cellglobal_sep', dpi=500)

#  ------------- 3 plot ------------- #
# list_b = [1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0]
# list_q = [10000, 20000, 30000, 40000, 50000, 100000, 150000, 200000, 250000, 300000, 350000]
# list_Dc = [0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
# fig, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1, sharex=True, sharey=True)
# fig, ((ax1,ax4),(ax2,ax5),(ax3,ax6)) = plt.subplots(nrows=3, ncols=2, sharex=True, sharey=True)

# ax1.plot(Dc.t_list[2], Dc.E_global_all_list[2], ls = '--', label=r'$E$', color='black')
# ax1.plot(Dc.t_list[2], Dc.E_global_in_list[2], label= r'$E^e + E^\Gamma$', color='b')
# ax1.plot(Dc.t_list[2], Dc.E_global_add_list[2], label= r'$E^{ac}$', color='r')

# ax2.plot(Dc.t_list[3], Dc.E_global_all_list[3], ls = '--', color='black')
# ax2.plot(Dc.t_list[3], Dc.E_global_in_list[3], color='b')
# ax2.plot(Dc.t_list[3], Dc.E_global_add_list[3], color='r')

# ax3.plot(Dc.t_list[4], Dc.E_global_all_list[4], ls = '--', color='black')
# ax3.plot(Dc.t_list[4], Dc.E_global_in_list[4], color='b')
# ax3.plot(Dc.t_list[4], Dc.E_global_add_list[4], color='r')

# ax4.plot(Dc.t_list[5], Dc.E_global_all_list[5], ls = '--', color='black')
# ax4.plot(Dc.t_list[5], Dc.E_global_in_list[5], color='b')
# ax4.plot(Dc.t_list[5], Dc.E_global_add_list[5], color='r')

# ax5.plot(Dc.t_list[6], Dc.E_global_all_list[6], ls = '--', color='black')
# ax5.plot(Dc.t_list[6], Dc.E_global_in_list[6], color='b')
# ax5.plot(Dc.t_list[6], Dc.E_global_add_list[6], color='r')

# ax6.plot(Dc.t_list[7], Dc.E_global_all_list[7], ls = '--', color='black')
# ax6.plot(Dc.t_list[7], Dc.E_global_in_list[7], color='b')
# ax6.plot(Dc.t_list[7], Dc.E_global_add_list[7], color='r')


# ax1.legend(loc='upper left', fontsize=16)
# # # ax2.legend()
# # # ax3.legend()

# ax1.set_title(r'$D_c=0.4$', fontsize=15)
# ax2.set_title(r'$D_c=0.5$', fontsize=15)
# ax3.set_title(r'$D_c=0.6$', fontsize=15)
# ax4.set_title(r'$D_c=0.7$', fontsize=15)
# ax5.set_title(r'$D_c=0.8$', fontsize=15)
# ax6.set_title(r'$D_c=0.9$', fontsize=15)
# # ax2.set_title(r'$D_c=0.000$', fontsize=15)
# # ax3.set_title(r'$D_c=0.000$', fontsize=15)

# ax1.set_ylabel(r'$E [\mathcal{G}_{c}L]$', fontsize=18)
# ax2.set_ylabel(r'$E [\mathcal{G}_{c}L]$', fontsize=18)
# ax3.set_ylabel(r'$E [\mathcal{G}_{c}L]$', fontsize=18)

# ax3.set_xlabel('cycles', fontsize=18)
# ax6.set_xlabel('cycles', fontsize=18)

# # ax1.set_xlim((2e7, 3e7))
# # # # plt.grid(linestyle = "--")
# plt.tight_layout()
# # plt.savefig('E_global.pdf', format='pdf', bbox_inches='tight')
# plt.savefig('E_global_Dc', dpi=500)
# plt.show()