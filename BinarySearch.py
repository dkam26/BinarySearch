
class list(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
        self.seq=[i for i in range(0,self.a*self.b,self.b)]
        self.variablelength=len(self.seq)
    def search(self,t):
        first=0
        last=len(self.seq)-1
        counter=0
    
        while first<=last:
            mid=(first+last)//2       
            counter=counter+1
            
            if self.seq[mid]==t:
                a={counter:mid}
                return a
            
            else:
                if t<self.seq[mid]:
                    last=mid-1
                
                else:
                    first=mid+1
        
class BinarySearch(list):
    def __init__(self,a,b):
        super().__init__(a,b)
l=BinarySearch(10,2)
print(l.search(0))