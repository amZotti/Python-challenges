import pickle

message = "Insert numbers. 0 will terminate"
infile = open("test.pickle","wb"); flag = True
try:
    while flag:
        num = int(input(message))
        if num == 0:
            flag = False

        else:
            pickle.dump(num,infile)
except:
    print("Something went down!")


infile.close()
infile = open("test.pickle","rb")

try:            #File reading
    while True:
        print(pickle.load(infile))

except EOFError:
    print("Thats all folks!")

finally:
    infile.close()
    print("Your done in this town, your DONE!")
        
