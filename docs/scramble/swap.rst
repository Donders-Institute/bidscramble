Action: swap
^^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir swap [-h] [-d] [-b] [-s PATTERN] [-g ENTITY [ENTITY ...]]

   Randomly swaps the content of data files between a group of similar files in the input directory and save
   them as output.

   options:
     -h, --help            Show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)
     -g ENTITY [ENTITY ...], --grouping ENTITY [ENTITY ...]
                           A list of (full-name) BIDS entities that make up a group between which file contents are
                           swapped. See: https://bids-
                           specification.readthedocs.io/en/stable/appendices/entities.html (default: ['subject'])

   examples:
     scramble inputdir outputdir swap
     scramble inputdir outputdir swap -s '.*\.(nii|json|tsv)'
     scramble inputdir outputdir swap -s '(?!derivatives(/|$)).*' -b
     scramble inputdir outputdir swap -g subject session run
