Action: json
^^^^^^^^^^^^

.. code-block:: console

   usage: scramble inputdir outputdir json [-h] [-d] [-b] [-s PATTERN] [-p PATTERN]

   Adds scrambled key-value versions of the json files in the input directory to the output directory. If no
   preserve expression is specified, the default behavior is to null all values.

   options:
     -h, --help            Show this help message and exit
     -d, --dryrun          Do not save anything, only print the output filenames in the terminal (default: False)
     -b, --bidsvalidate    If given, all input files are checked for BIDS compliance when first indexed, and
                           excluded when non-compliant (as in pybids.BIDSLayout) (default: False)
     -s PATTERN, --select PATTERN
                           A fullmatch regular expression pattern that is matched against the relative path of the
                           input data. Files that match are scrambled and saved in outputdir (default: (?!\.).*)
     -p PATTERN, --preserve PATTERN
                           A fullmatch regular expression pattern that is matched against all keys in the json
                           files. The json values are copied over when a key matches positively (default: None)

   examples:
     scramble inputdir outputdir json
     scramble inputdir outputdir json participants.json -p '.*'
     scramble inputdir outputdir json 'sub-.*.json' -p '(?!AcquisitionTime|Date).*'
