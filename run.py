# here is the entry point of the program
# we just create one instance of an object

from src import filter
from src import extracting
from src import fitting
import numpy as np


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
            #print(IV)


            #####################################################################################################

            # We do the fitting here 
            # we create objects for the reference curve, the IV graph and the flatten spectrum

            # we can now create object to create plots, we can used these coefficient of fitting for the function in the plot.py file
            # I think we can write a better code for the x_1,x_2, etc part


            # fitting coefficent for the ref curve
            ref_coef = fitting.Fitting(floatWaveLengthList[6], floatDBList[6]) #create a fitting object
            polynome_ref = ref_coef.reference_fit() #store the coefficient of the normal fitting


            # creating the x and y for the differents part of the IV fitted graph
            x_1 = np.array(IV[0][0:8])
            x_2 = np.array(IV[0][7:10])
            x_3 = np.array(IV[0][9:])
            y_1 = np.array(IV[1][0:8])
            y_2 = np.array(IV[1][7:10])
            y_3 = np.array(IV[1][9:])

            #fitting coefficient for the 1st part
            eq1 = fitting.Fitting(x_1, abs(y_1)) 
            equation1 = eq1.normal_fit(5)

            #fitting coefficient for the 2nd part
            eq2 = fitting.Fitting(x_2, abs(y_2))
            equation2 = eq2.normal_fit(5)

            #fitting coefficient for the 3rd part
            lm_fitting = fitting.Fitting(x_3, y_3)
            lm_coef = lm_fitting.non_linear_fit()


            #fitting coefficient for the flatten spectrum graph
            flatten_spectrum = fitting.Fitting(floatWaveLengthList[6], floatDBList[6])
            p = flatten_spectrum.flatten_spectrum_fit(3)
            
        else:
            print("it don't have LMZ in his name")
    else:
        print('its not an xml file')
    