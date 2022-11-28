# NOTES:

Code for filterbanking LOFT-e data.

Filterbanks are made using vdifil.cu.
Requires header files which may be created using vdifil_headers.py. 

Note: vdifil.cu only takes .vdif observations split into two separate polarisation files. If the two polarisations are stored in a single file, then these must be split up (using, e.g., baseband). 

Authors: Mateusz Malenta (CUDA code), C. Walker (Python tools)

---

# REQUIREMENTS:
- CUDA (more info to come)
- C++11
- LOFTe_parseVex: https://github.com/mbcxqcw2/LOFTe_parseVex (and dependencies)
- baseband: https://github.com/mhvk/baseband (and dependencies)

---

# USAGE:
## 1) TO START:
Git clone this repository. Add the location of the directory to your python path.

## 2) TO MAKE THE FILTERBANKER:
After git cloning this repository, enter the directory and do:
```
>nvcc -o vdifil -std=c++11 vdifil.cu -lcufft
```
to create the `vdifil` executable which may be run with data and headers (see next steps).

## 3) TO MAKE FILTERBANK HEADER FILES:
After git cloning this repository and adding it to your python path, one can do:
```
>import vdifil_headers as vh
>vh.make_vdifil_header(<vdif_file.vdif>,<vex_file.vex>,<header_file.dat>)
```
where `<vdif_file.vdif>` is the e-MERLIN .vdif file to be filterbanked, `<vex_file.vex>` is its associated .vex file, and `<header_file.dat>` is the desired name of the output header file. 

## 4) TO SPLIT `.VDIF` FILES BY POLARISATION:
Note: this step is required to run the `vdifil` executable if both polarisations were stored in the same .vdif file. If the polarisations were stored in separate files, this step may be skipped.

After git cloning this repository and adding it to your python path, one can do:
```
>TBC
```
where...

## 5) TO USE THE FILTERBANKER:
Split the .vdif file to filterbank into separate polarisations `<pol0.vdif>` and `<pol1.vdif>` if necessary. Create `<header_file.dat>`. Then do:
```
>./vdifil -a <pol0.vdif> -b <pol1.vdif> -o <outname.fil> -c <header_file.dat> -s
```
where `<outname.fil>` is the desired output name for the filterbank file, and `-s` scales the output data to an 8-bit filterbank file. If `-s` is not included, the output filterbank file will be 32-bit.
