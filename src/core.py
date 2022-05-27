from src import filter
from src import extracting
from src import fitting
from src import to_csv
from src import graphplot
from src import handler
import numpy as np
import matplotlib as plt


class Core:

    def __init__(self,lot_id,wafer_id,xy_coord,device_name,opt_savefig,opt_showfig):
        self.lot_id = lot_id
        self.wafer_id = wafer_id
        self.xy_coord = xy_coord
        self.device_name = device_name
        self.opt_savefig = opt_savefig
        self.opt_showfig = opt_showfig

    def run_core(self):

       
        # we'll have to find a method to go througth each and every file in each subfolders
        #How about using globe

        filtering = filter.filter(self.lot_id, self.wafer_id, self.device_name, self.xy_coord)
        file_list = filtering.filter()
        print(len(file_list))
        #i = 0
        for elem in file_list:

            filename = elem.split('\\')
            filename = filename[-1].split('.')
            filename = filename[0]
            #print(filename)
            # data extraction
            
            data = extracting.Extract(elem)
            IV = data.get_IV()
            floatWaveLengthList, floatDBList = data.get_Spectrum()
            #print(f'number of the file : {i}, IV data : {IV}')
            #i+=1

            #######################################################
            # Fitting the data
            #######################################################
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
            equation1 = eq1.normal_fit(4)
            fittedX_1 = equation1(x_1)

            #fitting coefficient for the 2nd part
            eq2 = fitting.Fitting(x_2, abs(y_2))
            equation2 = eq2.normal_fit(4)
            fittedX_2 = equation2(x_2)

            #fitting coefficient for the 3rd part
            lm_fitting = fitting.Fitting(x_3, y_3)
            lm_coef = lm_fitting.non_linear_fit()

            #fitting coefficient for the flatten spectrum graph
            flatten_spectrum = fitting.Fitting(floatWaveLengthList[6], floatDBList[6])
            p = flatten_spectrum.flatten_spectrum_fit(3)

            ######################################################
            # Data Analysis Plot
            ######################################################

            plotdata = graphplot.Plot(IV[0],IV[1],floatWaveLengthList,floatDBList,polynome_ref, self.opt_showfig, self.opt_savefig)
            plotdata.data_analysis_plot(x_1, x_2, x_3, fittedX_1, fittedX_2, lm_coef ,filename)
        """

                # use the csv.py here
                # make list 'data' to use csv.py
                r2 = handler.r_square(y_1,equation1(y_1))
                I = handler.Current_value(-1,equation1)
                I2 = handler.Current_value_lmfit(3,lm_coef)
                SPC_r2 = handler.r_square(floatDBList,polynome_ref[3](floatDBList))
                Max_trans = handler.Max_transmission(floatWaveLengthList,polynome_ref,3)

                data = [r2,I,I2,SPC_r2,Max_trans]

                csv = to_scv.Tocsv(data)
                csv.mpandas()

        """
        
