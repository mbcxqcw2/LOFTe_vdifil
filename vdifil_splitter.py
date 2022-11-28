# Tools for splitting e-MERLIN dual-pol .vdif data into separate polarisations.
# Author: C. Walker

from baseband import vdif

def split_vdif_file(vdif_file):
    """
    This function splits a dual-polarisation e-MERLIN .vdif file into
    two single-polarisation e-MERLIN .vdif files, for further use with
    LOFT-e's filterbanking code.
    
    It makes use of Marten van Kerkwijk's baseband code.
    
    INPUTS:
    
    vdif_file : [str] name and location of the vdif file to split.
    
    RETURNS
    
    Two single-polarisation output .vdif files, in the same location
    as the original input file, with the same names, but with an
    additional "_pol0" and "pol1" suffix.
    
    """
    
    input_filename = vdif_file
    print('Running split_vdif_file()')
    print('.vdif file to split: {0}'.format(input_filename))
    
    #define output file names
    output_filename_1 = vdif_file.split(".vdif")[0]+"_pol0.vdif"
    output_filename_2 = vdif_file.split(".vdif")[0]+"_pol1.vdif"
    
    print('files to create: {0}, {1}'.format(output_filename_1,output_filename_2))
    
    ##########################
    #split first polarisation#
    ##########################
    
    print('Creating {0}...'.format(output_filename_1))
    with vdif.open(input_filename, 'rb') as fr, vdif.open(output_filename_1, 'wb') as fw:
        while True:
            try:
                frame=fr.read_frame()
                if frame.header['thread_id']==0:
                    fw.write_frame(frame)
            except EOFError:
                break
    print('... done.')
    
    ###########################
    #split second polarisation#
    ###########################
    
    print('Creating {0}...'.format(output_filename_2))
    with vdif.open(input_filename, 'rb') as fr, vdif.open(output_filename_2, 'wb') as fw:
        while True:
            try:
                frame=fr.read_frame()
                if frame.header['thread_id']==1:
                    fw.write_frame(frame)
            except EOFError:
                break
    print('... done.')    
    
    return
