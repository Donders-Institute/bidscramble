Action: stub
^^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir stub [-h] [-d] [-b] [-s PATTERN] [-a {yes,no}]

   Creates a copy of the input directory tree in which all files are empty stubs. Optionally, modality-agnostic BIDS
   files from the input directory are copied over (with content), such as the README, dataset_descrption and
   participants rootfiles, as well as files in phenotype, code, and similar files in sourcedata and derivatives. In
   this way you can create a richer BIDS output folder without the modality specific content.

   options:
     -h, --help            show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)
     -a {yes,no}, --agnostics {yes,no}
                           If yes, in addition to the included files (see `--select` for usage), add modality-
                           agnostic BIDS files (default: yes)

   examples:
     scramble inputdir outputdir stub
     scramble inputdir outputdir stub -s '.*\.(nii|json|tsv)'
     scramble inputdir outputdir stub -s '(?!derivatives(/|$)).*'
     scramble inputdir outputdir stub -s '(?!sub.*scans.tsv|/func/).*'
