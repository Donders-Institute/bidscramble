Merge
~~~~~

.. code-block:: console

   usage: merge [-h] inputdirs [inputdirs ...] outputdir

   Merges non-overlapping/partial (e.g. single subject) BIDS datasets with identically processed derivative data

   positional arguments:
     inputdirs   The list of BIDS (or BIDS-like) input directories with the partial (e.g. single- subject) data
     outputdir   The output directory with the merged data

   options:
     -h, --help  show this help message and exit

   examples: merge singlesubject-1 singlesubject-2 singlesubject-3 outputdir
