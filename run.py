# here is the entry point of the program
# we just create one instance of an object

from src import core


if __name__=="__main__":

    #main of the project

    # Input parameters (this is a shitty idea really wtf is that)

    lot_id = []
    wafer_id = ['D07']
    xy_cord = ['(0,0)','(-1,-1)']
    device_name = ['LMZ']
    opt_savefig = False
    opt_showfig = False

    run = core.Core(lot_id, wafer_id, xy_cord, device_name, opt_savefig, opt_showfig)
    run.run_core()