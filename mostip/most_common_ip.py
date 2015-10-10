__author__ = 'Administrator'
__date__='2015-10-10'

import os
from collections import Counter


class MostIp():
    def __init__(self, source,temp,benchmark):
        self.source=source
        self.temp=temp
        self.benchmark=benchmark

    def splitfile(self):
        '''
        based on hash func to split file,benchmark=10
        '''
        temp_file_path=[]
        if not os.path.exists(temp):
            os.makedirs(temp)

        for i in xrange(self.benchmark):
            temp_file_path.append(open(temp+str(i)+'.txt',mode='w'))

        #print temp_file_path

        with open(source)as f:
            for line in f:
                temp_file_path[hash(line)%self.benchmark].write(line)

        for i in xrange(self.benchmark):
            temp_file_path[i].close()


    def getmostip(self):

        bigip=[]
        if not os.path.exists(self.temp):
            print 'please check you file path!'

        for basedir,dirs,files in os.walk(self.temp):
            for file in files:
                fpath=os.path.join(basedir,file)


                flines=[]
                with open(fpath) as f:
                    for line in f:
                        flines.append(line.replace('\n',' '))

                try:
                    bigip.append(Counter(flines).most_common()[0])

                except:
                    pass
        return  bigip

    def sortip(self,tme):

        return (sorted(tme,key = lambda a:a[1],reverse=True)[0])[0]

#start here:
baseaddr='C:/most_ip'
filename='/ip.txt'
tmp='/temp/'
source=baseaddr+filename
temp=baseaddr+tmp


te=MostIp(source,temp,10)
#split one to N
te.splitfile()
#write lines into small file
fc=te.getmostip()
#get the popluar ip info
print te.sortip(fc)








