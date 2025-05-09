Action: pseudo
^^^^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir pseudo [-h] [-d] [-b] [-s PATTERN] [-p PATTERN] [-a {yes,no}]
                                             {random,permute,original}

   Adds pseudonymized versions of the input directory to the output directory, such that the subject label is
   replaced by a pseudonym anywhere in the filepath as well as inside all text files (such as json and tsv-files).

   positional arguments:
     {random,permute,original}
                           The method to generate the pseudonyms

   options:
     -h, --help            Show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)
     -p PATTERN, --participant PATTERN
                           The findall() regular expression pattern that is used to extract the subject label from
                           the relative filepath. NB: Do not change this if the input data is in BIDS format
                           (default: ^sub-(.*?)(?:/|$).*)
     -a {yes,no}, --agnostics {yes,no}
                           If yes, in addition to the included files (see `--select` for usage), pseudomymize all
                           modality agnostic files in the input directory (such as participants.tsv, code, etc.)
                           (default: yes)

   examples:
     scramble inputdir outputdir pseudo
     scramble inputdir outputdir_remove1 pseudo random  -s '(?!sub-003(/|$)).*'
     scramble inputdir outputdir_keep1 pseudo original -s 'sub-003(/|$).*'
