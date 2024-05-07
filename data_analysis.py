import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class Schraubdome_Data():
    def __init__(self, versuch_type, specimenNumber_forWiederhol = None):
        self.df_list_A_10 = []
        self.df_list_A_10_625 = []
        self.df_list_A_11_25 = []
        self.df_list_A_12_5 = []

        self.df_list_M_10 = []
        self.df_list_M_10_625 = []
        self.df_list_M_11_25 = []
        self.df_list_M_12_5 = []
        
        self.vorpath = 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/01_Grafik/'
        
        # 1: Durchschrauben
        # 2: Einschrauben
        # 3: Wiederholschraubung
        
        if versuch_type == 1:
            # put the dataframe of 5 specimen into a list
            for i in range(1,6):
                df_A_10 = pd.read_csv(self.vorpath + '01_Adstif/01_Durchschrauben/0' + str(i) + '/1.csv')
                df_A_10_625 = pd.read_csv(self.vorpath + '01_Adstif/01_Durchschrauben/0' + str(i) + '/3.csv')
                df_A_11_25 = pd.read_csv(self.vorpath + '01_Adstif/01_Durchschrauben/0' + str(i) + '/4.csv')
                df_A_12_5 = pd.read_csv(self.vorpath + '01_Adstif/01_Durchschrauben/0' + str(i) + '/2.csv')
                
                df_M_10 = pd.read_csv(self.vorpath + '02_Moplen/01_Durchschrauben/0' + str(i) + '/1.csv')
                df_M_10_625 = pd.read_csv(self.vorpath + '02_Moplen/01_Durchschrauben/0' + str(i) + '/3.csv')
                df_M_11_25 = pd.read_csv(self.vorpath + '02_Moplen/01_Durchschrauben/0' + str(i) + '/4.csv')
                df_M_12_5 = pd.read_csv(self.vorpath + '02_Moplen/01_Durchschrauben/0' + str(i) + '/2.csv')
                
                self.df_list_A_10.append(df_A_10)
                self.df_list_A_10_625.append(df_A_10_625)
                self.df_list_A_11_25.append(df_A_11_25)
                self.df_list_A_12_5.append(df_A_12_5)
                
                self.df_list_M_10.append(df_M_10)
                self.df_list_M_10_625.append(df_M_10_625)
                self.df_list_M_11_25.append(df_M_11_25)
                self.df_list_M_12_5.append(df_M_12_5)
            
        elif versuch_type == 2:
            # put the dataframe of 5 specimen into a list
            for i in range(1,6):
                df_A_10 = pd.read_csv(self.vorpath + '01_Adstif/02_Einschrauben/0' + str(i) + '/1.csv')
                df_A_10_625 = pd.read_csv(self.vorpath + '01_Adstif/02_Einschrauben/0' + str(i) + '/3.csv')
                df_A_11_25 = pd.read_csv(self.vorpath + '01_Adstif/02_Einschrauben/0' + str(i) + '/4.csv')
                df_A_12_5 = pd.read_csv(self.vorpath + '01_Adstif/02_Einschrauben/0' + str(i) + '/2.csv')
                
                df_M_10 = pd.read_csv(self.vorpath + '02_Moplen/02_Einschrauben/0' + str(i) + '/1.csv')
                df_M_10_625 = pd.read_csv(self.vorpath + '02_Moplen/02_Einschrauben/0' + str(i) + '/3.csv')
                df_M_11_25 = pd.read_csv(self.vorpath + '02_Moplen/02_Einschrauben/0' + str(i) + '/4.csv')
                df_M_12_5 = pd.read_csv(self.vorpath + '02_Moplen/02_Einschrauben/0' + str(i) + '/2.csv')
                
                self.df_list_A_10.append(df_A_10)
                self.df_list_A_10_625.append(df_A_10_625)
                self.df_list_A_11_25.append(df_A_11_25)
                self.df_list_A_12_5.append(df_A_12_5)
                
                self.df_list_M_10.append(df_M_10)
                self.df_list_M_10_625.append(df_M_10_625)
                self.df_list_M_11_25.append(df_M_11_25)
                self.df_list_M_12_5.append(df_M_12_5)          

        else:
            # put the dataframe of 1st, 2nd, 5th, 9th, 10th einschr. of the defined specimen into a list
            # specimenNumber_forWiederhol = '01','02','03','04','05'
            
            list_tool = [1, 2, 5, 9, 10]
            
            for i in list_tool:
                df_A_10 = pd.read_csv(self.vorpath + '01_Adstif/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/1/' + str(i)+ '.csv')
                df_A_10_625 = pd.read_csv(self.vorpath + '01_Adstif/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/3/' + str(i)+ '.csv')
                df_A_11_25 = pd.read_csv(self.vorpath + '01_Adstif/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/4/' + str(i)+ '.csv')
                df_A_12_5 = pd.read_csv(self.vorpath + '01_Adstif/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/2/' + str(i)+ '.csv')
                
                df_M_10 = pd.read_csv(self.vorpath + '02_Moplen/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/1/' + str(i)+ '.csv')
                df_M_10_625 = pd.read_csv(self.vorpath + '02_Moplen/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/3/' + str(i)+ '.csv')
                df_M_11_25 = pd.read_csv(self.vorpath + '02_Moplen/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/4/' + str(i)+ '.csv')
                df_M_12_5 = pd.read_csv(self.vorpath + '02_Moplen/03_Wiederholschraubung/' + specimenNumber_forWiederhol + '/2/' + str(i)+ '.csv')
                
                self.df_list_A_10.append(df_A_10)
                self.df_list_A_10_625.append(df_A_10_625)
                self.df_list_A_11_25.append(df_A_11_25)
                self.df_list_A_12_5.append(df_A_12_5)
                
                self.df_list_M_10.append(df_M_10)
                self.df_list_M_10_625.append(df_M_10_625)
                self.df_list_M_11_25.append(df_M_11_25)
                self.df_list_M_12_5.append(df_M_12_5) 
                   
    @staticmethod
    def modify_dataframe(filename_list):

        for filename in filename_list:
            df = pd.read_csv(filename)
            
            # change the number format
            if df.columns[0] == 't':
                continue
                
            else: 
                t = []
                DM = []
                for i in df['x']:
                    t.append(float(i.replace(',', '.'))) 
                for j in df['Curve1']:
                    DM.append(float(j.replace(',', '.')))                    
                    
                df.columns = ['t', 'DM']
                df['t'] = np.array(t) * 1e-3
                df['DM'] = np.array(DM)
                
                df.to_csv(filename, index=False)
    
    @staticmethod
    def multiple_plot(dataframe_list, label_list, title, store_address):
        plt.style.use('bmh')

        fig, ax = plt.subplots()

        for i in range(0, len(dataframe_list)):
            ax.plot(np.array(dataframe_list[i]['t']) , dataframe_list[i]['DM'], label=label_list[i], marker = 'o')
            ax.legend(loc='upper left', fontsize=12)

        ax.set_xlabel('Zeit [s]')
        ax.set_ylabel('Drehmoment [Nm]')

        ax.set_title(title, fontsize=20)
        fig.set_size_inches(8,4)
        
        plt.savefig(store_address, dpi=500)
        plt.show()
        
    # @staticmethod
    # def wiederhol_multiple_plot(class_list, label_list, title, store_address):
        # plt.style.use('bmh')

        # fig, ax = plt.subplots()

        # for i in class_list:
            # for j in range(0, len(dataframe_list)):
                
            
            # ax.plot(np.array(dataframe_list[i]['t']) , dataframe_list[i]['DM'], label=label_list[i], marker = 'o')
            # ax.legend(loc='upper left', fontsize=12)

        # ax.set_xlabel('Zeit [s]')
        # ax.set_ylabel('Drehmoment [Nm]')

        # ax.set_title(title, fontsize=20)
        # fig.set_size_inches(8,4)
        
        # plt.savefig(store_address, dpi=500)
        # plt.show()
        


# the file name of all data (for data modification)
filenameList = []
vorpath = 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/01_Grafik/'
list_tool = [1, 2, 5, 9, 10]


for i in range(1,6):
    for j in range(1,5):
        filenameList.append(vorpath + '01_Adstif/01_Durchschrauben/0' + str(i) + '/' + str(j) + '.csv')
        filenameList.append(vorpath + '01_Adstif/02_Einschrauben/0' + str(i) + '/' + str(j) + '.csv')
        filenameList.append(vorpath + '02_Moplen/01_Durchschrauben/0' + str(i) + '/' + str(j) + '.csv')
        filenameList.append(vorpath + '02_Moplen/02_Einschrauben/0' + str(i) + '/' + str(j) + '.csv')
        
        for k in list_tool:
            filenameList.append(vorpath + '01_Adstif/03_Wiederholschraubung/0' + str(i) + '/' + str(j) + '/' + str(k) + '.csv')
            filenameList.append(vorpath + '02_Moplen/03_Wiederholschraubung/0' + str(i) + '/' + str(j) + '/' + str(k) + '.csv')
            
            
data_durch = Schraubdome_Data(1)
data_ein = Schraubdome_Data(2)

data_wieder_1 = Schraubdome_Data(3, '01')
data_wieder_2 = Schraubdome_Data(3, '02')
data_wieder_3 = Schraubdome_Data(3, '03')
data_wieder_4 = Schraubdome_Data(3, '04')
data_wieder_5 = Schraubdome_Data(3, '05')

class_list = [data_wieder_1, data_wieder_2, data_wieder_3, data_wieder_4, data_wieder_5]

label_list_list = []

for l in range(1,6):

    label_list = ['1st(0' + str(l) + ')','2nd(0' + str(l) + ')','3rd(0' + str(l) + ')','5th(0' + str(l) + ')','9th(0' + str(l) + ')']
    label_list_list.append(label_list)


# # --------------------------------------
# plt.style.use('bmh')
# fig, ax = plt.subplots()

# for i in [0]:
    # for j in [0,2,3]:
        
        # ax.plot(class_list[i].df_list_M_10[j]['t'], class_list[i].df_list_M_10[j]['DM'], label=label_list_list[i][j], marker = 'o')
        # ax.plot(class_list[i].df_list_M_10[j]['t'], class_list[i].df_list_M_10[j]['DM'], label=label_list_list[i][j], marker = 'o')
        
        # ax.legend(loc='upper right', fontsize=12)

# ax.set_xlabel('Zeit [s]')
# ax.set_ylabel('Drehmoment [Nm]')

# # ax.set_title(title, fontsize=20)
# fig.set_size_inches(16,10)

# plt.savefig('S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/02_Moplen/03_Wiederholschraubung/10_vergleichen', dpi=500)
# plt.show()
# --------------------------------------
plt.style.use('bmh')
fig, ax = plt.subplots()

list_1 = ['10 mm 1*','10 mm 2*','10 mm 5*','10 mm 9*','10 mm 10*']
list_2 = ['12.5 mm 1*','12.5 mm 2*','12.5 mm 5*','12.5 mm 9*','12.5 mm 10*']

for i in [0,2,3]:
    ax.plot(data_wieder_1.df_list_M_10[i]['t'], data_wieder_1.df_list_M_10[i]['DM'], label=list_1[i], marker = 'o')
    ax.plot(data_wieder_1.df_list_M_12_5[i]['t'], data_wieder_1.df_list_M_12_5[i]['DM'], label=list_2[i], marker = 'X')
    
    ax.legend(loc='upper right', fontsize=15)

ax.set_xlabel('Zeit [s]', fontsize=15)
ax.set_ylabel('Drehmoment [Nm]', fontsize=15)

# ax.set_title(title, fontsize=20)
fig.set_size_inches(16,10)

plt.savefig('S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/03_Vergleichen/Wiederhol')
plt.show()
    
# ----------------------------------------------
# data_durch.modify_dataframe(filenameList)


# label_list_1 = ['01', '02', '03', '04', '05']
# label_list_2 = ['10 mm', '10.625 mm', '11.25 mm', '12.5 mm']
# label_list = ['1st','2nd','3rd','5th','9th']

# Schraubdome_Data.multiple_plot(data_wieder.df_list_M_10, label_list, '10mm', 
# 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/02_Moplen/03_Wiederholschraubung/10')

# Schraubdome_Data.multiple_plot(data_wieder.df_list_M_10_625, label_list, '10.625mm', 
# 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/02_Moplen/03_Wiederholschraubung/10_625')

# Schraubdome_Data.multiple_plot(data_wieder.df_list_M_11_25, label_list, '11.25mm', 
# 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/02_Moplen/03_Wiederholschraubung/11_25')

# Schraubdome_Data.multiple_plot(data_wieder.df_list_M_12_5, label_list, '12.5mm', 
# 'S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/02_Moplen/03_Wiederholschraubung/12_5')


# # --------------- custom plotting ----------------
# plt.style.use('bmh')

# # 1*2
# fig, (ax1,ax2) = plt.subplots(nrows=1,ncols=2, sharex=False, sharey=True)

# ax1.plot(data_ein.df_list_A_10[4]['t'], data_ein.df_list_A_10[4]['DM'], label= '10 mm', marker = 'o')
# ax1.plot(data_ein.df_list_A_10_625[1]['t'], data_ein.df_list_A_10_625[1]['DM'], label= '10.625 mm', marker = '^')
# ax1.plot(data_ein.df_list_A_11_25[1]['t'], data_ein.df_list_A_11_25[1]['DM'], label= '11.25 mm', marker = 's')
# ax1.plot(data_ein.df_list_A_12_5[4]['t'], data_ein.df_list_A_12_5[4]['DM'], label= '12.5 mm', marker = 'X')

# ax2.plot(data_ein.df_list_M_10[4]['t'], data_ein.df_list_M_10[4]['DM'], label= '10 mm', marker = 'o')
# ax2.plot(data_ein.df_list_M_10_625[3]['t'], data_ein.df_list_M_10_625[3]['DM'], label= '10.625 mm', marker = '^')
# ax2.plot(data_ein.df_list_M_11_25[4]['t'], data_ein.df_list_M_11_25[4]['DM'], label= '11.25 mm', marker = 's')
# ax2.plot(data_ein.df_list_M_12_5[1]['t'], data_ein.df_list_M_12_5[1]['DM'], label= '12.5 mm', marker = 'X')

# ax1.legend(fontsize=12)
# ax2.legend(fontsize=12)

# ax1.set_xlabel('Zeit [s]', fontsize=12)
# ax2.set_xlabel('Zeit [s]', fontsize=12)

# ax1.set_ylabel('Drehmoment [Nm]', fontsize=12)

# ax1.set_title('Adstif', fontsize=15)
# ax2.set_title('Moplen', fontsize=15)

# fig.set_size_inches(12,4)

# plt.savefig('S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/03_Vergleichen/Einschrauben', dpi=500)
# plt.show()
# ------------------------------------------------------------------------------------------------------
# # 2*2 
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2, sharex=True, sharey=True)

# ax1.plot(data_ein.df_list_A_10[4]['t'], data_ein.df_list_A_10[4]['DM'], label= '1 * einschr.', marker = 'o')
# ax1.plot(data_wieder.df_list_M_10[4]['t'], data_wieder.df_list_M_10[4]['DM'], label= '10 * einschr.', marker = '^')

# ax1.set_title('10 mm', fontsize=15)

# ax2.plot(data_ein.df_list_A_10_625[4]['t'], data_ein.df_list_A_10_625[4]['DM'], label= '1 * einschr.', marker = 'o')
# ax2.plot(data_wieder.df_list_M_10_625[4]['t'], data_wieder.df_list_M_10_625[4]['DM'], label= '10 * einschr.', marker = '^')

# ax2.set_title('10.625 mm', fontsize=15)

# ax3.plot(data_ein.df_list_A_11_25[4]['t'], data_ein.df_list_A_11_25[4]['DM'], label= '1 * einschr.', marker = 'o')
# ax3.plot(data_wieder.df_list_M_11_25[4]['t'], data_wieder.df_list_M_11_25[4]['DM'], label= '10 * einschr.', marker = '^')

# ax3.set_title('11.25 mm', fontsize=15)

# ax4.plot(data_ein.df_list_A_12_5[4]['t'], data_ein.df_list_A_12_5[4]['DM'], label= '1 * einschr.', marker = 'o')
# ax4.plot(data_wieder.df_list_M_12_5[4]['t'], data_wieder.df_list_M_12_5[4]['DM'], label= '10 * einschr.', marker = '^')

# ax4.set_title('12.5 mm', fontsize=15)

# ax1.legend(fontsize=12)
# ax2.legend(fontsize=12)
# ax3.legend(fontsize=12)
# ax4.legend(fontsize=12)

# ax3.set_xlabel('Zeit [s]', fontsize=12)
# ax4.set_xlabel('Zeit [s]', fontsize=12)

# ax1.set_ylabel('Drehmoment [Nm]', fontsize=12)
# ax3.set_ylabel('Drehmoment [Nm]', fontsize=12)


# fig.set_size_inches(10,5)

# plt.savefig('S:/SIMULATIONSDATEN/SIMULATIONS/AKW_STUDENTS/Feifan/02_Schraubdome/03_Data/03_Vergleichen/Ein_Wieder', dpi=500)
# plt.show()

# print(data_wieder.df_list_M_10[4])