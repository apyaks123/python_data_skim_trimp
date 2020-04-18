import math
# Global variables
str = []




def readFile():
    count = -1
    with open("quotes.txt") as fp: 
        Lines = fp.readlines() 
        for line in Lines: 
            count += 1
            
            x = {count,  line.strip()}
            str.append(line)
            print("-------------------------------------------")
            print("Line{}: {}".format(count, line.strip())) 


def init():
    
    self.next = None
    data = None
    return self



def add(self,data):
    current = self
    while current != None & current.next != None:
      
        self.data = item
        current = current.next
    return self.data


   
    

def macromenu():
                global item
                print("-------------------------------------------")
                print("-------------------------------------------")
                #print("Please enter 1 - 9, to select which line you want to skim and trim. Thank you!!!")
                keyboard = int(input("Please enter 0 - 9, to select which line you want to skim and trim:"))
                print(keyboard)
                print("-------------------------------------------")
                print("-------------------------------------------")
                if (keyboard == 0):
                    item = str[0]
                    print(item)
                    return item
                elif (keyboard == 1):
                    item = str[1]
                    print(str[1])
                    return item
                elif (keyboard == 2):
                    item = str[2]
                    print(str[2])
                    return item
                elif (keyboard == 3):
                    item = str[3]
                    print(str[3])
                    return item
                elif (keyboard == 4):
                    item = str[4]
                    print(str[4])
                    return item
                elif (keyboard == 5):
                    item = str[5]
                    print(str[5])
                    return item
                elif (keyboard == 6):
                    item = str[6]
                    print(str[6])
                    return item
                elif (keyboard == 7):
                    item = str[7]
                    print(str[7])
                    return item
                elif (keyboard == 8):
                    item = str[8]
                    print(str[8])
                    return item
                elif (keyboard == 9):
                    item = str[9]
                    print(str[9])
                    return item
                else:
                    "Please enter value from 0-9 and try again. Thank you!!!!"
                    macromenu()

            
    




def skim():
        global skim
        print("-------------------------------------------")
        print("-------------------------------------------")

        skim = int(input("Please enter 0 - 2, to select how many n  to to skim:"))
        print("-------------------------------------------")
        print("-------------------------------------------")
        return skim
        
def trim():
        global trim
        print("-------------------------------------------")
        print("-------------------------------------------")
        trim = int(input("Please enter 0 - 2, to select how many n  to to grams/trims:"))
        print("-------------------------------------------")
        print("-------------------------------------------")
        return trim
    



def skimTrim():
        global sss
        
        f = open('nskipmgram_quotes.txt', 'a+')
        
        f.write("-------------------------------------------\n")
        f.write("-------------------------------------------\n")
        f.write('sentence: ' +  item)
        print('in skim trim')
        if item:
            if skim:
                if trim:
                    x = item.split()
                    print(len(x))
                    y = skim
                    z = trim
                    w = len(x)
                    p = w/(y + z)
                    k = math.ceil(p)
                    leng = k + 1
                    print(leng)
                    #print(y)
                    f.write('Output of' +  repr(y) + '-skip' + '-' + repr(z) + '-grams:\n')
                    f.write('Output sentence: ')
                    if (trim == 2):
                        
                        
                        counter = 0
                        index = 0
                        while (leng >= counter):
                            counter += 1
                            
                
                            #f.write('This is a test\n')
                            
                            f.write(x[index] + ' ' + x[w - (y + z - index + 1)] + ',')
                            print(x[index] + ' ' + x[w - (y + z - index + 1)] + ',')
                            #sss = (x[index] + ' ' + x[w - (y + z - index)] + ',')
                            #print >> f, sss
                            
                            #print(sss)
                            index += 1

                    elif (trim == 3):
                        counter = 0
                        index = 0
##                        while (leng >= counter):
##                            counter += 1
                            
                
                            #f.write('This is a test\n')
                            
                        f.write(x[0] + ' ' + x[w - (y + z -  1)] +  ' ' + x[w + 2 - (y + z - 2)] + ' ')
                        print(x[0] + ' ' + x[w - (y + z - 1)] +  ' ' + x[w + 2 - (y + z - 2)] + ' ')
                            #sss = (x[index] + ' ' + x[w - (y + z - index)] + ',')
                            #print >> f, sss
                            
                            #print(sss)
##                            index += 1
##                        


                    

                        

                    


        f.write("\n-------------------------------------------\n")
        f.write("-------------------------------------------\n")             
                            
        f.close()                 
                    
                                                    
                       
            
        
        

def main():
    readFile()
    macromenu()
    skim()
    trim()
    skimTrim()
    

main()

