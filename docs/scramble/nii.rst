Action: nii
^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir nii [-h] [-d] [-b] [-s PATTERN] [-c [SPECS]]
                                          {null,blur,permute,scatter,wobble} ...

   Adds scrambled versions of the NIfTI files in the input directory to the output directory. If no
   scrambling method is specified, the default behavior is to null all image values.

   positional arguments:
     {null,blur,permute,scatter,wobble}
                           Scrambling method (default: null). Add -h, --help for more information
       null                Replaces all values with zeros
       blur                Apply a 3D Gaussian smoothing filter
       permute             Perform random permutations along one or more image dimensions
       scatter             Perform random permutations using a sliding 3D permutation kernel
       wobble              Deform the images using 3D random waveforms

   options:
     -h, --help            Show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)
     -c [SPECS], --cluster [SPECS]
                           Use the DRMAA library to submit the scramble jobs to a high-performance compute (HPC)
                           cluster. You can add an opaque DRMAA argument with native specifications for your HPC
                           resource manager (NB: Use quotes and include at least one space character to prevent
                           premature parsing -- see examples) (default: None)

   examples:
     scramble inputdir outputdir nii
     scramble inputdir outputdir nii scatter -h
     scramble inputdir outputdir nii scatter 2 -s 'sub-.*_MP2RAGE.nii.gz' -c '--mem=5000 --time=0:20:00'
     scramble inputdir outputdir nii wobble -a 2 -f 1 8 -s 'sub-.*_T1w.nii'
