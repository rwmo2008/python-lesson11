try:
#    my_list = [0, 1, 2]
#    print(my_list[4])
#except IndexError as ie:
#    print(ie)
    infile = open('dataFile.txt','r')
    infile.write("hello")
    infile.close()
except IOError as ioe:
    print("filename:", ioe.filename)
    print("strerror:", ioe.strerror)
#use dir(IOError) to get list of all attributes of IOError object
