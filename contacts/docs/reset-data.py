# default array
array = [['Jym'], ['Patel'], [''], ['jympatel@yahoo.com']]
# editors can put their name in array if they want to

# save to pickle file
import pickle
outfile = open('data/pickle-main', 'wb')
pickle.dump(array, outfile)
outfile.close()
# sucess
print("RESET HAS BEEN SUCESSFUL!")
print()