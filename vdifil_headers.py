# Tools for creating a vdifil header for filterbanking vdif data
# Author: C. Walker

import os
import numpy as np
from LOFTe_parseVex_lib import parse_vex, get_vex_sched
from baseband import vdif
from matplotlib import pyplot as plt

def make_vdifil_header(vdif_file,vex_file,outfilename):
    """
    This function generates a header file which can be used by LOFTe_vdifil
    (https://github.com/mbcxqcw2/LOFTe_vdifil)
    
    to filterbank an e-MERLIN .vdif file
    
    INPUTS:
    
    vdif_file : [str] location of the .vdif file to filterbank
    vex_file : [str] location of the .vdif file's associated .vex file
    outfilename : [str] location and filename to store output header file
    
    RETURNS:
    
    a header file stored at outfilename for use with LOFTe_vdifil
    
    """
    
    ###############################
    #hard-coded header information#
    ###############################
    #NOTE: these can be updated to generate automatically
    #as more functionality is added to LOFTe_parseVex_lib

    RAWFILE = 'LofteMkI'
    AZ = 0.0
    DEC = 0.0
    RA = 0.0
    REFDM = 0.0
    TSAMP = 0.0
    ZA = 0.0
    DATATYPE=1
    BEAMNO = 0
    MACHINEID = 82
    NOBEAMS = 0
    OUTBITS = 32
    NOCHANS = 256
    NOIFS = 1
    TELESCOPEID = 82

    #######################################################
    #get scan number and scan telescope from vdif filename#
    #######################################################

    scan_number = #need to do
    scan_tel = #need to do

    ###############################
    #read first frame of vdif data#
    ###############################

    fh = vdif.open(vdif_file,'rs')
    TSTART = fh.start_time.mjd #extract start time of observation
    fh.close()
    
    ####################
    #parse the vex file#
    ####################
    
    vex_data = parse_vex(vex_file) #extract all .vex file data
    schedule_info = get_vex_sched(vex_data) #extract schedule information
    
    #extract information about the correct scan from vex file
    scan_info = schedule_info[scan_number]
    SOURCE=scan_info['scan_source']

    #convert telescope names to all lowercase to match file naming scheme
    alltels = np.array([i.lower() for i in scan_info['scan_stations']])

    #get index for correct telescope
    tel_idx = np.where(alltels==scan_tel)[0][0]

    #get center frequency for observation in Hz
    FCENT = scan_info['station_fcents'][tel_idx].to('Hz').value

    #get bandwidth for observation in Hz
    FOFF = scan_info['station_bandwidths'][tel_idx].to('Hz').value
    
    #write data to a header file
    print('VDIF HEADER INFORMATION:\n')

    with open(outfilename,"w") as f:
        print('RAWFILE {0}'.format(RAWFILE),file=f)
        print('SOURCE {0}'.format(SOURCE),file=f)
        print('AZ {0}'.format(AZ),file=f)
        print('DEC {0}'.format(DEC),file=f)
        print('FCENT {0}'.format(FCENT),file=f)
        print('FOFF {0}'.format(FOFF),file=f)
        print('RA {0}'.format(RA),file=f)
        print('REFDM {0}'.format(REFDM),file=f)
        print('TSAMP {0}'.format(TSAMP),file=f)
        print('TSTART {0}'.format(TSTART),file=f)
        print('ZA {0}'.format(ZA),file=f)
        print('DATATYPE {0}'.format(DATATYPE),file=f)
        print('BEAMNO {0}'.format(BEAMNO),file=f)
        print('MACHINEID {0}'.format(MACHINEID),file=f)
        print('NOBEAMS {0}'.format(NOBEAMS),file=f)
        print('OUTBITS {0}'.format(OUTBITS),file=f)
        print('NOCHANS {0}'.format(NOCHANS),file=f)
        print('NOIFS {0}'.format(NOIFS),file=f)
        print('TELESCOPEID {0}'.format(TELESCOPEID),file=f)
        
    print('written to {0}'.format(outfilename))
    
    return
