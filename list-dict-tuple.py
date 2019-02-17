nameMap={'TOM':10,'Albert':15,'Rob':5}

#print dir(nameMap)
#Print Tuples sorted by it's key
print sorted( [ (v,k) for k,v in nameMap.items() ] )