#!/bin/python3

import argparse, re, os, subprocess
import numpy as np
import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(description='argment')
    parser.add_argument('-s','-spice',type=str,help='import spice file')
    args = parser.parse_args()
    simulator = "/usr/bin/ngspice"
    interval = 10
    #print(args)
    cmd = str(simulator)+" -b "+str(args.s)+" > __tmp__"
    spicerun = args.s
    spicerun += ".run"
    with open(spicerun, 'w') as f:
      outlines = []
      outlines.append(cmd)
      f.writelines(outlines)
    f.close

    # run ngspice
    cmd = ['sh', spicerun]
    try:
      res = subprocess.check_call(cmd)
    except:
      print("Failed to launch spice")

    # init 2D array
    data_array = []
    index = []

    # read result
    linenum = 0
    with open("__tmp__", 'r') as f:
      # if the line starts from number, this is plotted data
      pattern = re.compile(r'^[0-9]')
      for inline in f:
        if(pattern.match(inline)):
          linenum += 1
          if(linenum % interval == 0):
            data_array.append(inline.split())
          #print(inline)
    f.close()

    # if the line starts from "Index", this is index 
    with open("__tmp__", 'r') as f:
      pattern = re.compile(r'^Index')
      for inline in f:
        if(pattern.match(inline)):
            index = inline.split()
            #print(index)
    f.close()

    # transopose
    data_array_T = np.array(data_array).T.tolist()

    # print
#    for i in range(len(data_array_T)):
#      for j in range(len(data_array_T[i])):
#        print(data_array_T[i][j], end=' ')
#        print("\n")
    if(len(data_array_T) == 3):
      fig = plt.figure(figsize=(10,6))
      ax = fig.add_subplot()
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.locator_params(axis='x',nbins=6)#y軸，6個以内．
      plt.locator_params(axis='y',nbins=6)#y軸，6個以内．
      ax.plot(data_array_T[1], data_array_T[2])
      ax.set_xlabel(index[1])
      ax.set_ylabel(index[2])

    elif(len(data_array_T) == 4):
      fig = plt.figure(figsize=(10,6))
      ax1 = fig.add_subplot(2,1,1)
      ax1.plot(data_array_T[1], data_array_T[2])
      ax1.set_xlabel(index[1])
      ax1.set_ylabel(index[2])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,2)
      ax2.plot(data_array_T[1], data_array_T[3])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[3])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
    elif(len(data_array_T) == 5):
      fig = plt.figure(figsize=(10,6))
      ax1 = fig.add_subplot(2,1,1)
      ax1.plot(data_array_T[1], data_array_T[2])
      ax1.set_xlabel(index[1])
      ax1.set_ylabel(index[2])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,2)
      ax2.plot(data_array_T[1], data_array_T[3])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[3])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,3)
      ax2.plot(data_array_T[1], data_array_T[4])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[4])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示

    elif(len(data_array_T) == 6):
      fig = plt.figure(figsize=(10,6))
      ax1 = fig.add_subplot(2,1,1)
      ax1.plot(data_array_T[1], data_array_T[2])
      ax1.set_xlabel(index[1])
      ax1.set_ylabel(index[2])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,2)
      ax2.plot(data_array_T[1], data_array_T[3])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[3])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,3)
      ax2.plot(data_array_T[1], data_array_T[4])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[4])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
    
      ax2 = fig.add_subplot(2,1,4)
      ax2.plot(data_array_T[1], data_array_T[5])
      ax2.set_xlabel(index[1])
      ax2.set_ylabel(index[5])
      plt.gca().xaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示
      plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))#y軸小数点以下3桁表示

    plt.show()


if __name__ == '__main__':
  main()
