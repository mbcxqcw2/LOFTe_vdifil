# NOTES:

WILL CURRENTLY CRASH! make_vdifil_header() needs to be updated to extract the scan number and scan telescope information from the .vdif filename.

Code for filterbanking LOFT-e data.

Filterbanks are made using vdifil.cu.
Requires header files which may be created using vdifil_headers.py. 

Note: vdifil.cu only takes .vdif observations split into two separate polarisation files. If the two polarisations are stored in a single file, then these must be split up (using, e.g., baseband). 

Authors: Mateusz Malenta (CUDA code), C. Walker (Python tools)

# REQUIREMENTS:
- CUDA (more info to come)
- C++11
- LOFTe_parseVex: https://github.com/mbcxqcw2/LOFTe_parseVex (and dependencies)

# TO MAKE THE FILTERBANKER:
After git cloning this repository, do:
```
>nvcc -o vdifil -std=c++11 vdifil.cu -lcufft
```
to create the `vdifil` executable which may be run with data and headers (see next steps).

# TO MAKE A FILTERBANK HEADER FILE:
After git cloning this repository and adding it to your python path, do:
```
>from LOFTe_vdifil import vdifil_headers as vh
>vh.make_vdifil_header(<vdif_file.vdif>,<vex_file.vex>,<header_file.dat>)
```
where `<vdif_file.vdif>` is an e-MERLIN .vdif file, `<vex_file.vex>` is its associated .vex file, and `<header_file.dat>` is the desired name of the output header file. 

# TO SPLIT A VDIF FILE BY POLARISATION:
Note: this is necessary if both pols were stored in the same .vdif file. If polarisations were stored separately, this step may be skipped.

After git cloning this repository and adding it to your python path, do:
```
>TBC
```
where...

# TO USE THE FILTERBANKER:
split the .vdif file into separate polarisatins `<pol0.vdif>` and `<pol1.vdif>` and then:
```
>./vdifil -a <pol0.vdif> -b <pol1.vdif> -o <outname.fil> -c <header_file.dat> -s
```
where `<outname.fil>` is the desired output name for the filterbank file, and `-s` scales the output data to an 8-bit filterbank file. If `-s` is not included, the output filterbank file will be 32-bit.
