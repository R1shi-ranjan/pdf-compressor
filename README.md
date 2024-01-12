# pdf-compressor
REQUIRED LIBRARIES


sudo apt-get install ghostscript

pip install PyPDF2

 Breakdown of the code:

Compression Function (compress)
Uses Ghostscript to compress a PDF file with specified quality options.
Quality options range from 0 to 4, with 0 being the default and 4 being the highest compression for prepress.
Calculates and prints the compression ratio and final file size after compression.

Ghostscript Path Function (get_ghostscript_path)
Checks common names for the Ghostscript executable and returns the path if found.
Raises an exception if Ghostscript is not found in the system.
Main Compression Function (compress_pdf_file)
Invokes the compression function with provided input and output file paths and quality level.

Command-Line Interface (argparse)
Parses command-line arguments.
input: Path of the input PDF file (required).
-o, --out: Path of the output PDF file (optional, default is "temp.pdf").
-b, --backup: Creates a backup of the original PDF file.
--open: Opens the compressed PDF file after compression.
-c, --compression: Compression level (0 to 4).


Main Function (main)
Parses command-line arguments.
Runs the compression function with provided arguments.
Handles backup and file removal based on options.
Opens the compressed PDF file if specified.
            Execution Check (if “__name__” == "__main__":)
Calls the main function when the script is executed directly.

This script leverages Ghostscript's capabilities to compress PDF files, allowing users to customize compression levels and manage output paths. Users can run the script from the command line, providing input and optional parameters for compression.
To run the script, users can execute it in the terminal/cmd with appropriate arguments. For example:
python script_name.py input.pdf -o output.pdf -b --open -c 3
This command compresses the input PDF (input.pdf) with quality level 3, creates a backup, and opens the compressed file (output.pdf).

OUTPUT
256mb to 24mb









