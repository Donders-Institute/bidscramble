Scramble
~~~~~~~~

.. code-block:: console

   usage: scramble [-h] inputdir outputdir {stub,tsv,json,nii,fif,brainvision,swap,pseudo} ...

   The general workflow to build up a scrambled dataset is by consecutively running `scramble` for actions of your
   choice. For instance, you could first run `scramble` with the `stub` action to create a dummy dataset with only
   the file structure and some basic files, and then run `scramble` with the `nii` action  to specifically add
   scrambled NIfTI data (see examples below). To combine different scrambling actions, simply re-run `scramble` using
   the already scrambled data as input directory.

   positional arguments:
     inputdir              The BIDS (or BIDS-like) input directory with the original data
     outputdir             The output directory with the scrambled pseudo data

   options:
     -h, --help            Show this help message and exit

   Action:
     {stub,tsv,json,nii,fif,brainvision,swap,pseudo}
                           Add -h, --help for more information
       stub                Saves a dummy inputdir skeleton in outputdir
       tsv                 Saves scrambled tsv files in outputdir
       json                Saves scrambled json files in outputdir
       nii                 Saves scrambled NIfTI files in outputdir
       fif                 Saves scrambled FIF files in outputdir
       brainvision         Saves scrambled BrainVision files in outputdir
       swap                Saves swapped file contents in outputdir
       pseudo              Saves pseudonymized file names and contents in outputdir

   examples:
     scramble inputdir outputdir stub -h
     scramble inputdir outputdir nii -h

.. toctree::
   :maxdepth: 3
   :hidden:
   :caption: Scramble actions

   stub
   tsv
   json
   nii
   fif
   brainvision
   swap
   pseudo
