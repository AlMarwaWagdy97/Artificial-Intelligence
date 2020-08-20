import math
class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense

def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0,	labels[0]))
    data.append(item(0, 0, 0, 1,	labels[1]))
    data.append(item(0, 0, 1, 0,	labels[2]))
    data.append(item(0, 0, 1, 1,	labels[3]))
    data.append(item(0, 1, 0, 0,	labels[4]))
    data.append(item(0, 1, 0, 1,	labels[5]))
    data.append(item(0, 1, 1, 0,	labels[6]))
    data.append(item(0, 1, 1, 1,	labels[7]))
    data.append(item(1, 0, 0, 0,	labels[8]))
    data.append(item(1, 0, 0, 1,	labels[9]))
    data.append(item(1, 0, 1, 0,	labels[10]))
    data.append(item(1, 0, 1, 1,	labels[11]))
    data.append(item(1, 1, 0, 0,	labels[12]))
    data.append(item(1, 1, 0, 1,	labels[13]))
    data.append(item(1, 1, 1, 0,	labels[14]))
    data.append(item(1, 1, 1, 1,	labels[15]))
    data.append(item(1, 0, 0, 0,	labels[16]))
    data.append(item(1, 0, 0, 1,	labels[17]))
    data.append(item(1, 0, 1, 0,	labels[18]))
    data.append(item(1, 0, 1, 1,	labels[19]))
    data.append(item(1, 1, 0, 0,	labels[20]))

    return data


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1
        self.list=[]
def entropy(data, index):
    #lenght of Data
    lenght = len(data)
    #make It map
    arr = {}
    for i in range(0,len(data)):
        if(index == 0): labelvar  = data[i].age
        if (index == 1): labelvar = data[i].prescription
        if (index == 2): labelvar = data[i].astigmatic
        if (index == 3): labelvar = data[i].tearRate
        if (index == 4): labelvar = data[i].needLense
        if labelvar not in arr.keys():
            arr[labelvar] = 0
        arr[labelvar] += 1
    res = 0

    for k in arr:
        eq = float(arr[k])/lenght
        res -=  eq * math.log2(eq)
    return  res


def Gain (l , index, list_total_entropy,data):
    count_one_for_attrib = 0
    count_zero_for_attrib = 0
    Total_entropy = entropy(data,4)
    c0_0= 0 ;
    c0_1 = 0
    c1_0=0
    c1_1=0
    length = len(l)
    arr0 = {}
    arr1 = {}
    for i in range(length ):
        if l[i]==1 :

            count_one_for_attrib +=1
            if(list_total_entropy[i]==1):
                 c1_1 +=1
            else:
                c1_0+=1
        if l[i]== 0 :
            count_zero_for_attrib+=1
            if(list_total_entropy[i]==0):
                c0_0+=1
            else:
                c0_1 += 1
   # print("jgbn",)
    if (c1_1 != 0):arr1[1] = c1_1
    if (c1_0 != 0): arr1[0] = c1_0
    if (c0_0 != 0): arr0[0] = c0_0
    if (c0_1 != 0): arr0[1] = c0_1
    esubnt0 = 0
    sum0 = 0
    for k in  arr0:

        eq = float(arr0[k]) / (arr0[0]+arr0[1])

        esubnt0 -= eq * math.log2(eq)
        sum0 += arr0[k]
    esubnt1 = 0
    sum1 = 0
    for k in arr1:
        eq = float(arr1[k]) / (arr1[0]+arr1[1])
        esubnt1 -= eq * math.log2(eq)
        sum1 += arr1[k]
    res = Total_entropy - ( (((sum0)/21)*esubnt0 )+ (((sum1)/21)*esubnt1 ))
    return  res







class ID3:
    def __init__(self, features):
        self.features = features
        

    def classify(self, input):

        datalable = getDataset()
        total_entropy = entropy(datalable, 4)
       # print("Total Entropy ", total_entropy)

        #l = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1]
        e = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0,1,0,1,0]
        #list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for i in range(len(dataset)):
            
                gain = Gain(list,i,e,datalable)
                print("Gain ", gain)

       # gain  = Gain(l,0,e,datalable)
















dataset = getDataset()
features = [Feature('age'),Feature('prescription'),Feature('astigmatic'),Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1]) # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0]) # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0]) # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1]) # should print 1
print('testcase 4: ', cls)





