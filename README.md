# pharma_bricks


in preprocessing we get the raw edit x12 837 files and convert them into xml format using pyx12 library.

later we updated them to convert into csv format because bis- get csv as their input. their conversion happened externally so we need to write the logic on our own.

the csv conversion defined in claim_box/consolidation

now we have to csv which holds the header and the lines of the edi data.

the gold layer table forming is in progress...