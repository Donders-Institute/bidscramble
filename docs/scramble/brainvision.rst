Action: brainvision
^^^^^^^^^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir brainvision [-h] [-d] [-b] [-s PATTERN] {null,permute} ...

   Adds scrambled versions of the BrainVision EEG files in the input directory to the output directory. If no
   scrambling method is specified, the default behavior is to null the data.

   positional arguments:
     {null,permute}        Scrambling method (default: null). Add -h, --help for more information
       null                Replaces all values with zeros
       permute             Randomly permute the EEG samples in each channel

   options:
     -h, --help            Show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)

   examples:
     scramble inputdir outputdir brainvision
     scramble inputdir outputdir brainvision permute
