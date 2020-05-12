
import  re
operators=['{',";", ".", ":", "(", ")", "+", "-", "*", "/", "=", ">", "<",'}']

keyWord = ['or','is','then','and','else','if','var','begin','integer','end','while','real','do']
# Using readlines()
file1 = open('program.txt', encoding="utf8")
fToken= open("token.csv","w+")
fidentifier=open("identifier.csv","w+")
lines = file1.readlines()

lineNumber=0
for i in lines:
    temp=i

    foundOp=False
    startIndex=0
    endIndex=0
    for j in range(0,temp.__len__()):
        endIndex=j
        if(temp[j]==' '):
            if(keyWord.__contains__(temp[startIndex:endIndex])):
                fToken.write("keyword  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex)+"\n" )
                #print("keyword  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex))
                startIndex=startIndex+1
            elif (re.search('^[0-9]+.[0-9]+$', temp[startIndex:endIndex]) != None):
                fToken.write("readConst  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                #print("real  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                startIndex = endIndex + 1

            elif (re.search('^[0-9]+$', temp[startIndex:endIndex]) != None):
                if (temp[j] != '.'):
                    fToken.write("intConst  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                    #print("integer  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                    startIndex = endIndex + 1
            elif (re.search('^".+"$', temp[startIndex:endIndex]) != None):
                # todo operators in string
                fToken.write("stringConst  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                #print("string  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                startIndex = endIndex + 1
            elif(not operators.__contains__(temp[startIndex:endIndex])):
                # print("ss"+temp[startIndex:endIndex]+"ss")
                x=" "
                if(temp[startIndex:endIndex]!=''):
                    fToken.write("id  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                    fidentifier.write("id  " + temp[startIndex:endIndex]+"\n")
                    #print("id  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                    startIndex = endIndex + 1

            startIndex=endIndex+1

        elif(operators.__contains__(temp[j])):

            if(operators.__contains__(temp[j+1])):
                #fToken.write("sym  " + temp[j]+temp[j+1] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                #print("operator  " + temp[j]+temp[j+1] + " " + str(lineNumber) + " " + str(startIndex))
                startIndex=startIndex+1



            elif(operators.__contains__(temp[j-1])):
                # print(startIndex)
                pass
            else:
                fToken.write("sym  " + temp[j] + " " + str(lineNumber) + " " + str(startIndex) + "\n")
                #print("operator  " + temp[j] + " " + str(lineNumber) + " " + str(startIndex))
                #startIndex = startIndex + 1

            if(keyWord.__contains__(temp[startIndex:endIndex]) and temp[startIndex:endIndex]!=" "):
                fToken.write("keyword  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex)+"\n")
                #print("keyword  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex))
                startIndex=endIndex+1
                foundOp=True
            elif temp[startIndex:endIndex]!="":
                foundOp = True
                # print("-----")
                # print("s"+temp[startIndex:endIndex]+"s")


                if (re.search('^[0-9]+.[0-9]+$', temp[startIndex:endIndex]) != None):
                    fToken.write("real  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                    #print("real  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                    startIndex=endIndex+1

                elif (re.search('^[0-9]+$', temp[startIndex:endIndex]) != None):
                    if(temp[j]!='.'):
                        fToken.write("integer  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex) + "\n")
                        #print("integer  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                        startIndex = endIndex + 1
                elif (re.search('^".+"$', temp[startIndex:endIndex]) != None):
                    # todo operators in string
                    fToken.write("string  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex)+"\n")
                    #print("string  " + temp[startIndex:endIndex] + " " + str(lineNumber) + " " + str(startIndex))
                    startIndex = endIndex + 1
                elif(temp[startIndex:endIndex]!=''):
                    fToken.write("id  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex)+"\n")
                    #print("id  "+temp[startIndex:endIndex]+" "+str(lineNumber)+ " "+str(startIndex))
                    startIndex = endIndex + 1

    if not foundOp:
        # todo check if work in keywords
        fToken.write("keyword " + temp[startIndex:endIndex] +" "+ str(lineNumber)+" " + " 0 " +"\n")
        #print("keyword " + temp[startIndex:endIndex] +" "+ str(lineNumber)+" " + " 0 ")



    lineNumber=lineNumber+1

fToken.close()
fidentifier.close()
file1.close()