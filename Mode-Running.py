import glob
import subprocess
import pandas as pd 
import matplotlib.pyplot as plt
import xarray as xr
import numpy as np
import os
import shutil
import fileinput
import math
from netCDF4 import Dataset

class Storm:
  def __init__(self, timestep, cov_th, radius_th, area, speedx, speedy, i10, i25, i50, i75, i90, loc):
      self.timestep = timestep
      self.cov_th = cov_th
      self.radius_th=radius_th
      self.area=area
      self.speedx=speedx
      self.speedy=speedy
      self.i10=i10
      self.i25=i25
      self.i50=i50
      self.i75=i75
      self.i90=i90
      self.loc=loc

#mode \
#/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/IMERG-Comprehensive/3B-HHR-L.MS.MRG.3IMERG.20180913-S210000-E212959.1260.V05B.HDF5.nc \
#/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/MRMS-Regridded/MRMS_PrecipRate_00.00_20180913-213000-compressed-l5-double.nc \
#/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/MODE \
#-outdir /home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut/ \
#-v 2




folderMRMS="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/"
folderIMERG="/srv/ccrc/data60/z5194283/Data/"
IMERG_files=glob.glob(folderIMERG+"IMERG_Comprehensive_V06/Selected/*.nc")
IMERG_files.sort()
MRMS_files = glob.glob(folderMRMS+"MRMS-Regridded/*.nc")
MRMS_files.sort()
#
i=0
for files in MRMS_files:
    LoadMTD =  "module load gsl/2.3" +" \n" + "module load netcdf-c/4.4.1.1" + " \n" + "module load netcdf-c++/4-4.3.0" +" \n" + "module load met/8.20" + " \n" + "mode \\"
    ObsAddress = MRMS_files[i]+" \\"
    FcstAddress = IMERG_files[i]+" \\"
#   #For HQPrecipitation:
#    ConfigAddress = "/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/MODE-HQPrecipitation \\"
#   #For IRonly:
#    ConfigAddress = "/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/MODE-IRonly \\"
#   #For PrecipitationCal:    
    ConfigAddress = "/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/MODE \\"
#   #For HQPrecipitation:
#    OutputAddress = "/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-HQPrecipitation/ \\"
#   #For IRonly:
#    OutputAddress = "/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-IRonly/ \\"
#   #For PrecipitationCal:    
    OutputAddress = "/srv/ccrc/data60/z5194283/OutPuts/ModeOutputs-V06/ \\"
    Script= LoadMTD + "\n" + FcstAddress + "\n" + ObsAddress + "\n" + ConfigAddress + "\n" + "-outdir " + OutputAddress + "\n" + "-v 2" + "\n"    
    subprocess.getstatusoutput(Script)
    print(str(i))
    i=i+1
    
######## reading information from data: 
##   For HQPrecipitation:    
##outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-HQPrecipitation/"   
##   For IRonly:    
##outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut-IRonly/"   
##   For PrecipitationCal:
#outputfolder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/ModeOutPut/"
#outpufiles=glob.glob(outputfolder+"*_obj.txt")
#outpufiles.sort()    
#IMERG=list()
#MRMS=list()
#Time=0
#t=0
#r=0
#for files in outpufiles:
#                    
#    table = pd.read_table(files, delim_whitespace=True) 
#    #Properties of Forecast and Observed Cluster
#    FcstIndex=-3
#    ObsIndex=-2
#        
#    Fcsti10=table["INTENSITY_10"].values[FcstIndex]
#    Fcsti25=table["INTENSITY_25"].values[FcstIndex]
#    Fcsti50=table["INTENSITY_50"].values[FcstIndex]
#    Fcsti75=table["INTENSITY_75"].values[FcstIndex]
#    Fcsti90=table["INTENSITY_90"].values[FcstIndex]
#    FcstLoc=list()
#    FcstLoc.append([table["CENTROID_X"].values[FcstIndex],table["CENTROID_Y"].values[FcstIndex]])
#    FcstSpeedX=0
#    FcstSpeedY=0
#    FcstArea=int(table["AREA"].values[FcstIndex])
#   
#
#    Obsi10=table["INTENSITY_10"].values[ObsIndex]
#    Obsi25=table["INTENSITY_25"].values[ObsIndex]
#    Obsi50=table["INTENSITY_50"].values[ObsIndex]
#    Obsi75=table["INTENSITY_75"].values[ObsIndex]
#    Obsi90=table["INTENSITY_90"].values[ObsIndex]
#    ObsLoc=list()
#    ObsLoc.append([table["CENTROID_X"].values[ObsIndex],table["CENTROID_Y"].values[ObsIndex]])
#    ObsSpeedX=0
#    ObsSpeedY=0
#    ObsArea=int(table["AREA"].values[ObsIndex])
#    IMERG.append(Storm(Time,t,r,FcstArea,FcstSpeedX,FcstSpeedY,Fcsti10,Fcsti25,Fcsti50,Fcsti75,Fcsti90,FcstLoc))
#    MRMS.append(Storm(Time,t,r,ObsArea,ObsSpeedX,ObsSpeedY,Obsi10,Obsi25,Obsi50,Obsi75,Obsi90,ObsLoc))
#    Time=Time+1
#
#print("plotting ...")    
## plotting    
#MI90=list()
#II90 =list()
#TT=list()
#II75=list()
#MI75=list()
#II50=list()
#MI50=list()
#MA=list()
#IA=list()
#MV=list()
#IV=list()
#Iloc=list()
#MI25=list()
#II25=list()
#MI10=list()
#II10=list()
#
##Ading IMERG and MRMS attributes to different array.
#for jj in range(0, len(IMERG)):
#    TT.append(IMERG[jj].timestep)
#    MI75.append(MRMS[jj].i75)
#    II75.append(IMERG[jj].i75)
#    MI90.append(MRMS[jj].i90)
#    II90.append(IMERG[jj].i90)
#    MI50.append(MRMS[jj].i50)
#    II50.append(IMERG[jj].i50)
#    MI25.append(MRMS[jj].i25)
#    II25.append(IMERG[jj].i25)
#    MA.append(MRMS[jj].area)
#    IA.append(IMERG[jj].area)
#    Iloc.append(IMERG[jj].loc)
#    MI10.append(MRMS[jj].i10)
#    II10.append(IMERG[jj].i10)    
#    
#
#folder="/home/z5194283/hdrive/MET_Tutorial/MyData/RealData/FinalData/"
#IMERG_files=glob.glob(folder+"IMERG-Comprehensive/*.nc")
#IMERG_files.sort()  
#
#i=0
#sensor=list()
#for file in IMERG_files:
##    ds = xr.open_dataset(file)
#    fnc = Dataset(file, 'r')
##    k=ds.variables['HQprecipSource']
#    x=Iloc[i][0][0]
#    y=Iloc[i][0][1]
#    variable = fnc.variables['HQprecipSource']
#    sensor.append(variable[x, y])
##    dsloc = ds.sel(lon=Iloc[i][0][0],lat=Iloc[i][0][1],method='nearest')
##    sensor.append(float(dsloc['HQprecipSource']))
#    i=i+1
#i=0
#QualityIndex=list()
#for file in IMERG_files:
##    ds = xr.open_dataset(file)
#    fnc = Dataset(file, 'r')
##    k=ds.variables['HQprecipSource']
#    x=Iloc[i][0][0]
#    y=Iloc[i][0][1]
#    variable = fnc.variables['precipitationQualityIndex']
#    QualityIndex.append(variable[x, y])
##    dsloc = ds.sel(lon=Iloc[i][0][0],lat=Iloc[i][0][1],method='nearest')
##    sensor.append(float(dsloc['HQprecipSource']))
#    i=i+1
#
##x = np.linspace(0,75,75)
#
##y2 = np.random.exponential(1, len(x))
#
##plt.fill_between(x,sensor, step="pre", alpha=0.4)
#
##plt.fill_between(x,y2, step="pre", alpha=0.4)
#TT = [x+1 for x in TT]
#
#plt.subplot(4,1,1)
#plt.ylim()
#plt.bar(TT, sensor)
#plt.yticks(np.arange(0, 12, step=1))
#plt.xticks(np.arange(0, 75, step=1))
#
##plt.subplot(4,1,3)
##plt.ylim()
##plt.bar(TT, QualityIndex)
##plt.yticks(np.arange(0, 1, step=0.1))
##plt.xticks(np.arange(0, 75, step=1))
#
#Bias = [MI75[x]-II75[x] for x in range(0,len(MI75))]
#
#
#plt.subplot(4,1,1)
##plt.plot(TT, II75, 'C3', zorder=1, lw=2, label='IMERG')
#plt.bar(TT, sensor, 'C2', zorder=2, lw=2, label='MRMS-IMERG')
##plt.plot(TT, MI90, 'o', color='black');
#plt.title('Intensity 75')
#plt.legend(loc='lower right')
##plt.xlabel("Time Step (30 min)")  
#plt.ylabel("Intensity (mm/hr)")    
#plt.xticks(np.arange(0, 75, step=1)) 
#plt.grid()
#plt.tight_layout()  
#      
#plt.subplot(4,1,2)
#plt.plot(TT, II75, 'C3', zorder=1, lw=2, label='IMERG')
#plt.plot(TT, MI75, 'C2', zorder=2, lw=2, label='MRMS')
##plt.plot(TT, MI90, 'o', color='black');
#plt.title('Intensity 75')
#plt.legend(loc='lower right')
##plt.xlabel("Time Step (30 min)")  
#plt.ylabel("Intensity (mm/hr)")    
#plt.xticks(np.arange(0, 75, step=1)) 
#plt.tight_layout()  
#
#plt.subplot(4,1,3)
#plt.plot(TT, II50, 'C3', zorder=1, lw=2, label='IMERG')
#plt.plot(TT, MI50, 'C2', zorder=2, lw=2, label='MRMS')
#plt.title('Intensity 50')
#plt.legend(loc='lower right')
##plt.xlabel("Time Step (30 min)")  
#plt.ylabel("Intensity (mm/hr)") 
#plt.xticks(np.arange(0, 75, step=1))
#plt.tight_layout()  
#
#plt.subplot(4,1,4)
#plt.plot(TT, II25, 'C3', zorder=1, lw=2, label='IMERG')
#plt.plot(TT, MI25, 'C2', zorder=2, lw=2, label='MRMS')
#plt.title('Intensity 25')
#plt.legend(loc='lower right')
#plt.xlabel("Time Step (30 min)")  
#plt.ylabel("Intensity (mm/hr)") 
#plt.xticks(np.arange(0, 75, step=1))
#plt.tight_layout() 