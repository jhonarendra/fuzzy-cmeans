# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import math, json, numpy
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
    
    ispath = None 
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        
        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
        
        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Input File" ), wx.VERTICAL )
        
        self.m_filePicker2 = wx.FilePickerCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
        sbSizer3.Add( self.m_filePicker2, 0, wx.ALL|wx.EXPAND, 5 )
        
        
        bSizer2.Add( sbSizer3, 1, wx.EXPAND, 5 )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Config" ), wx.VERTICAL )
        
        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText10 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"W", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        bSizer10.Add( self.m_staticText10, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer9.Add( bSizer10, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
        
        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl4 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_textCtrl4, 1, wx.ALL, 5 )
        
        
        bSizer9.Add( bSizer12, 3, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )
        
        bSizer91 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText101 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"maxIter", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText101.Wrap( -1 )
        bSizer101.Add( self.m_staticText101, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer91.Add( bSizer101, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
        
        bSizer121 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl41 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer121.Add( self.m_textCtrl41, 1, wx.ALL, 5 )
        
        
        bSizer91.Add( bSizer121, 3, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer1.Add( bSizer91, 0, wx.EXPAND, 5 )
        
        bSizer92 = wx.BoxSizer( wx.HORIZONTAL )
        
        bSizer102 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText102 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"errorRate", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText102.Wrap( -1 )
        bSizer102.Add( self.m_staticText102, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        bSizer92.Add( bSizer102, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )
        
        bSizer122 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_textCtrl42 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer122.Add( self.m_textCtrl42, 1, wx.ALL, 5 )
        
        
        bSizer92.Add( bSizer122, 3, wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 5 )
        
        
        sbSizer1.Add( bSizer92, 0, wx.EXPAND, 5 )
        
        self.m_button1 = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_button1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )
        
        
        bSizer2.Add( sbSizer1, 1, wx.EXPAND, 5 )
        
        
        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
        
        bSizer3 = wx.BoxSizer( wx.VERTICAL )
        
        self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer39 = wx.BoxSizer( wx.VERTICAL )
        self.m_textCtrl12 = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.TE_READONLY )
        bSizer39.Add( self.m_textCtrl12, 20, wx.ALL|wx.EXPAND, 5 )
        
        
        self.m_panel1.SetSizer( bSizer39 )
        self.m_panel1.Layout()
        bSizer39.Fit( self.m_panel1 )
        bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
        
        
        bSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer1 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        


        self.m_filePicker2.Bind( wx.EVT_FILEPICKER_CHANGED, self.filePicker)
        self.m_button1.Bind( wx.EVT_BUTTON, self.onStart )
    
    def __del__( self ):
        pass
    def filePicker( self, event ):
        
        #path = event.GetPath()
        self.ispath=event.GetPath()
        print(self.ispath)
        

    def onStart( self, event):
        w = int(self.m_textCtrl4.GetValue())
        maxIter = int(self.m_textCtrl41.GetValue())
        errorRate = float(self.m_textCtrl42.GetValue())
        
        print(w)
        print(maxIter)
        print(errorRate)
        csv          = self.ispath

        print(csv)
        cluster_file = 'cluster.json'
        data_file    = 'data.json'

        df = pd.read_csv(csv)
        cluster = []
        for i in range(len(df['Cluster'])):
            cluster.append(df['Cluster'][i])
        count_cluster = []
        for i in range(len(cluster)):
            cluster_name = cluster[i]
            if not cluster[i] in count_cluster:
                count_cluster.append(cluster_name)
        cluster = []
        random_1 = (1/len(count_cluster))/2
        for i in range(len(df['Cluster'])):
            clus = []
            for j in range(len(count_cluster)):
                clus.append(random_1)
            cluster.append(clus)
        for i in range(len(df['Cluster'])):
            for j in range(len(count_cluster)):
                if df['Cluster'][i] == count_cluster[j]:
                    cluster[i][j] = 1 - (random_1*2)
        file_name = cluster_file
        output = open(file_name,"w")
        output.write(str(cluster))
        output.close()

        atribut = []
        for i in range(len(df.columns)):
            atribut.append(df.columns[i])
        atribut.remove('Cluster')
        data = []
        for i in range(len(df[atribut[0]])):
            clus = []
            for j in range(len(atribut)):
                clus.append(df[atribut[j]][i])
            data.append(clus)
        file_name = data_file
        output = open(file_name,"w")
        output.write(str(data))
        output.close()

        P = [0]
        for i in range(maxIter+1):
            P.append(0)
        selisih_arr = []
        report = ''
        for iter in range(1,maxIter+1):
            clusterW = []
            for i in range(len(cluster)):
                clus = []
                for j in range(len(cluster[0])):
                    clus.append(0)
                clusterW.append(clus)
            clusterWX = []
            for h in range(len(data[0])):
                cluss = []
                for i in range(len(cluster)):
                    clus = []
                    for j in range(len(cluster[0])):
                        clus.append(0)
                    cluss.append(clus)
                clusterWX.append(cluss)
            for i in range(len(cluster)):
                for j in range(len(cluster[i])):
                    clusterW[i][j] = cluster[i][j]**w
                    for k in range(len(data[0])):
                        clusterWX[k][i][j] = clusterW[i][j]*data[i][k]
            sumClusterW = []
            sumClusterWX = []
            for i in range(len(cluster[0])):
                sumClusterW.append(0)
            for h in range(len(data[0])):
                clus = []
                for i in range(len(cluster[0])):
                    clus.append(0)
                sumClusterWX.append(clus)
            for i in range(len(cluster)):
                for j in range(len(cluster[0])):
                    sumClusterW[j] = sumClusterW[j] + clusterW[i][j]
            for i in range(len(cluster)):
                for j in range(len(cluster[i])):
                    for k in range(len(data[0])):
                        sumClusterWX[k][j] = sumClusterWX[k][j] + clusterWX[k][i][j]
            pusatCluster = []
            for i in range(len(cluster[0])):
                clus = []
                for j in range(len(data[0])):
                    clus.append(0)
                pusatCluster.append(clus)
            for i in range(len(sumClusterW)):
                for j in range(len(data[0])):
                    pusatCluster[i][j] = sumClusterWX[j][i]/sumClusterW[i]
            VijminVkjWuik = []
            VijminVkjW = []
            for h in range(len(cluster[0])):
                clus = []
                for i in range(len(data)):
                    cluss = []
                    for j in range(len(data[0])):
                        cluss.append(0)
                    clus.append(cluss)
                VijminVkjWuik.append(clus)
                VijminVkjW.append(clus)
            for i in range(len(VijminVkjWuik)):
                for j in range(len(VijminVkjWuik[i])):
                    for k in range(len(data[0])):
                        VijminVkjW[i][j][k] = (data[j][k]-pusatCluster[i][k])**w
            for i in range(len(VijminVkjWuik)):
                for j in range(len(VijminVkjWuik[i])):
                    for k in range(len(data[0])):
                        VijminVkjWuik[i][j][k] = ((data[j][k]-pusatCluster[i][k])**w)*clusterW[j][i]
            X = []
            for i in range(len(data[0])):
                X.append(0)
            for i in range(len(VijminVkjWuik)):
                for j in range(len(VijminVkjWuik[i])):
                    for k in range(len(data[0])):
                        X[k] = X[k] + VijminVkjWuik[i][j][k]
            for k in range(len(data[0])):
                P[iter] = P[iter]+X[k]
            summ = []
            for i in range(len(data)):
                clus = []
                for j in range(len(cluster[0])):
                    clus.append(0)
                summ.append(clus)
            for i in range(len(summ[0])):
                for j in range(len(summ)):
                    counter = 0
                    for k in range(len(data[0])):
                        counter = counter + (data[j][k]-pusatCluster[i][k])**w
                    summ[j][i] = counter**-1
            total = []
            for i in range(len(data)):
                total.append(0)
            for i in range(len(total)):
                for j in range(len(cluster[0])):
                    total[i] = total[i] + summ[i][j]
            for i in range(len(summ[0])):
                for j in range(len(summ)):
                    cluster[j][i] = summ[j][i]/total[j]
            selisih = math.sqrt(math.pow(P[iter]-P[iter-1], 2))
            selisih_arr.append(selisih)
            stop_iter = iter
            report += 'Iterasi '+str(iter)+'/'+str(maxIter)+'\n'
            report += 'P '+str(iter)+': '+str(P[iter])
            report += ' - P'+str(iter-1)+': '+str(P[iter-1])
            report += ' - Selisih: '+str(selisih)+'\n\n'
            if selisih <= errorRate:
                break
        file_name = 'report.txt'
        output = open(file_name,"w")
        output.write(str(report))
        self.m_textCtrl12.SetLabel(report)
        output.close()


        
        

        hasils = ''
        for i in range(len(data)):
            hasil = ''
            hasils +='data '+str(i+1)+': '+str(data[i])
            for j in range(len(cluster[0])):
                if cluster[i][j]>=0.5:
                    hasil = j+1
                    hasils +=' - cluster: '+str(count_cluster[hasil-1])
                    hasils +=' - sebelumnya: '+str(df['Cluster'][i])
                    hasils +=' - persentase: '+str(math.floor(cluster[i][hasil-1]*10000)/100)+'%'
            hasils +='\n'
        file_name = 'hasil.txt'
        output = open(file_name,"w")
        output.write(str(hasils))
        output.close()

        plt.plot(range(iter), selisih_arr, 'b', label='Loss')
        plt.title('Loss')
        plt.legend()
        plt.show()


    
app = wx.App(False)

#create an object of MyFrame2
frame = MyFrame1(None)
#show the frame
frame.Show(True)
#start the application
app.MainLoop()