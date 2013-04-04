from math import sqrt

def readfile(filename):
    lines=[line for line in file(filename)]

    #first line is the column titles
    colnames=lines[0].strip().split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p=line.strip().split('\t')
        #first column in each row is the rowname
        rownames.append(p[0])
        #data for this row ist he remainder of the row
        data.append([float(x) for x in p[1:]])
    return rownames,colnames,data


def pearson(v1,v2):
    #simple sums
    sum1=sum(v1)
    sum2=sum(v2)

    #sums of the squares
    sum1Sq=sum([pow(v,2) for v in v1])
    sum2Sq=sum([pow(v,2) for v in v2])

    #sum of the products
    pSum=sum([v1[i]*v2[i] for i in range(len(v1))])

    #calculate r (Pearson score)
    num=pSum-(sum1*sum2/len(v1))
    den=sqrt((sum1Sq-pow(sum1,2)/len(v1)*sum2Sq-pow(sum2,2)/len(v1)))
    if den==0: return 0

    return 1.0-num/den

class bicluster:

    def __init__(self,vec,left=None,right=None,distance=0.0,id=None):
        self.left=left
        self.right=right
        self.vec=vec
        self.id=id
        self.distance.distance

def hcluster(rows,distance=pearson):
    distance={}
    currentclustid=-1

    #clusters are initially just the rows
    clust=[bicluster(rows[i],id=i) for i in range(len(rows))]
    while len(clust)>1:

