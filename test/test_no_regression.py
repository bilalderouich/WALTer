# coding=utf-8
from walter import project
import pandas,os
from walter.data_access import get_data_dir
from pathlib2 import Path
import numpy.testing as np

def test_same_result():
    #assert : verify if the same wheat field have the same results for the same chosen parameters.

    p = project.Project(name='same') # Create the simulation directory
    params = p.csv_parameters('sim_scheme_test.csv')[0] # recovery of parameters
    lsys, lstring = p.run(**params)
    result_directory = str(p.output_path()) + '/'
    reference_directory = get_data_dir() + "/ref_output/" # Reference folder
    list_of_file_ref = os.listdir(reference_directory) # Listing of the different reference files
    reference = {}
    for i in list_of_file_ref:
        element = reference_directory + i # Recover the absolut path
        up_date = { i : pandas.read_csv(element, sep='\t')} # Recover file and content
        reference.update(up_date) # Reference dictionnary
        list_of_result = os.listdir(result_directory)
        np.assert_array_equal(list_of_file_ref,list_of_result) # Check that the 2 lists are equal
        my_file = Path(result_directory + i)
        if my_file.is_file():
            dfout = pandas.read_csv(my_file, sep='\t')
            print(' \n The tested file is : '+ i + '\n')
            np.assert_array_equal(dfout, reference[i]) # Comparison Reference and Simulation
        else:
            print(' \n The ' + my_file + ' file is non-existent ')


    p.remove(force=True)
