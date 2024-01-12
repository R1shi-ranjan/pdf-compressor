import argparse
import os
import shutil
import subprocess

_doc_ = """
Your documentation goes here. This will be displayed when the user runs the script with the -h or --help option.
"""

def compress(input_file_path, output_file_path, quality):
    # Define quality options
    quality_options = {
        0: "/default",
        1: "/screen",
        2: "/ebook",
        3: "/printer",
        4: "/prepress",
    }

    # Set initial and final sizes
    initial_size = os.path.getsize(input_file_path)
    final_size = 0

    # Call Ghostscript to compress PDF
    gs_path = get_ghostscript_path()
    subprocess.call(
        [
            gs_path,
            "-dNOPAUSE",
            "-dBATCH",
            "-dQUIET",
            "-dSAFER",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS={}".format(quality_options[quality]),
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            "-sOutputFile={}".format(output_file_path),
            input_file_path,
        ]
    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.5f}MB".format(final_size / 1000000))
    print("Done.")

    return final_size

def get_ghostscript_path():
    gs_names = ["gs", "gswin32", "gswin64"]
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(
        f"No GhostScript executable was found on path ({'/'.join(gs_names)})"
    )

def compress_pdf_file(input_file_path, output_file_path, quality):
    compress(input_file_path, output_file_path, quality)

def main():
    parser = argparse.ArgumentParser(description=_doc_, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("input", help="Relative or absolute path of the input PDF file")
    parser.add_argument("-o", "--out", help="Relative or absolute path of the output PDF file")
    parser.add_argument("-b", "--backup", action="store_true", help="Backup the old PDF file")
    parser.add_argument("--open", action="store_true", default=False, help="Open PDF after compression")
    parser.add_argument("-c", "--compression", type=int, default=2, choices=range(5), help="Set the compression level")
    args = parser.parse_args()

    # In case no output file is specified, store in temp file
    if not args.out:
        args.out = "temp.pdf"

    # Run
    compress_pdf_file(args.input, args.out, args.compression)

    # In case no output file is specified, erase the original file
    if args.out == "temp.pdf":
        if args.backup:
            shutil.copyfile(args.input, args.input.replace(".pdf", "_BACKUP.pdf"))
        shutil.copyfile(args.out, args.input)
        os.remove(args.out)

    # In case we want to open the file after compression
    if args.open:
        if args.out == "temp.pdf" and args.backup:
            shutil.copyfile(args.input, args.input.replace(".pdf", "_BACKUP.pdf"))
            shutil.copyfile(args.out, args.input)
            os.remove(args.out)

if __name__ == "__main__":
    main()