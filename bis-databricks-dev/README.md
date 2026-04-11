## IDAP-Notebooks ##
This repo is for the Notebook development for IDAP

# NOTEBOOK GUIDE
## This section outlines notebook useage
* ### Common Methods
    * ABC
        * ErrorHandling - Contains methods for error handling
            * outputValidationError - Used by the validations to create and error output file that is saved as a csv file.

        * FileHandling - Contains methods for file based functions
            * isIgnoreHeader - creates a dataframe.  Need to look into consolidating this with the following
            * withoutHeader - creates a dataframe.
            * delimitedFile - creates a dataframe.
            * path_exists - checks if a path exists and will return a boolean based on the existence.

        * GetTypes - Contains methods for data typing and structs
            * getSQLType - Takes a string scala datatype and returns a SQL datatype.
            * getDataType - Takes a string scala datatype and returns a true scala datatype.
            * getStruct - Takes in a dataframe and returns a struct type to be used to build other dataframes.

        * ValidationL3 - Contains methods for file and row level checks3 (Level 3)
            * rowEquals - Check to determine if a row = an expected value.
            * rowGreaterEqual - Check to determine if a row >= an expected value.
            * rowCheckValidator - Main row check validator.  Calls the sub row check validations.
            * fileRulesValidator - Main file check validator.

    * Conversion
        * ConversionMain
            * hasColumn - Checks if dataframe contains a column.
            * lsplit - Creates a row of data from a List.
            * createFixedWidthDF - Creates a fixed width dataframe from a fixed width file. 
            * createDelimitedDF - Creates a dataframe from a dataframe using a recordtype.
            * removeLogFiles - Removes the logfies when writing a dataframe to blob storage.
            * removeFile - Removes a single from a given path.
            * renameDF - Renames a datafile. 
            * writeDfCSV - Creates a CSV from a dataframe.
            * moveFile - Moves a file from a source location to a destination location.

* ### Conversion - Contains Conversion notebooks

* ### DatalakeProcessing
    * FCFClaimsProcessing - Processes FCF files into the processed zone.
    * FilestoProcess - Determines which process script needs to be executed.
    * GoldenClaimsProcessing - Processes golden claims into the consolidated zone
    * MoveFileToConsolidation - Processes files into the consolidated zone
    * MoveFileToProcess - Processes files into the processed zone.

* ### Inbound
    * CSVConversion - Master conversion notebook that calls notebooks in the CommonMethods > Conversion folder
    * Level2Validations - Performs level 2 validations
    * Level3Validations - Performs level 3 validations
    
* ### Synapse Jobs - Contains Synapse load notebooks