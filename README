#NOTES:
CUDA code for filterbanking LOFT-e data.
Original author: Mateusz Malenta

#REQUIREMENTS:
CUDA (more info to come)
C++11

#TO MAKE:
```
nvcc -o vdifil -std=c++11 vdifil.cu -lcufft
```

#TO USE:
```
./vdifil -a <data_pol0> -b <data_pol1> -o <outname.fil> -c <headerfile.dat> -s
```
where `<data_pol0>` is the polarisation 0 vdif file recorded for a LOFT-e observation, `<data_pol1>` is the polarisation 1 vdif file for the same observation, `<outname.fil>` is the desired output name for the filterbank file, and `-s` scales the output data to an 8-bit filterbank file. If `-s` is not included, the output filterbank file will be 32-bit.
