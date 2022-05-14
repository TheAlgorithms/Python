import pickle
key = 'SKD0DW99SAMXI19#DJI9'

outfile = open('data/pickle-key', 'wb')
pickle.dump(key, outfile)
outfile.close()

print("key RESTORED to default")