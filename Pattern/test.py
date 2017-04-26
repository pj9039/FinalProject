import PatternDiscovery as pt
import sys

a = pt.findpattern(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),30)
for i in range(0,len(a)):
	print(a[i])
#dg.drawgraph("005940",200,30)
