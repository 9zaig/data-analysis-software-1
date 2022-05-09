# here is the entry point of the program
# we just create one instance of an object


if __name__=="__main__":
    
    #main of the project
    file = filter.Filter("./dat/D07/20190715_190855/HY202103_D07_(-1,-1)_LION1_DCM_LMZC.xml") 
    # we'll have to find a method to go througth each and every file in each subfolders

    #we check if the file is an xml file
    if file.is_xml() == True:
        print("its the right type of file")

        #we check if the file contain LMZC in his name
        if file.has_LMZC() == True:
            print("it got LMZ in his name")
            #we can work on the file now

            #we extract the data
            data = extracting.Extract("./dat/D07/20190715_190855/HY202103_D07_(-1,-1)_LION1_DCM_LMZC.xml")
            IV = data.get_IV()
            floatWaveLengthList, floatDBList = data.get_Spectrum()
            print(IV)

        else:
            print("it don't have LMZ in his name")
    else:
        print('its not an xml file')
    