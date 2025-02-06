# STL to GLB

This is a simple Python script that converts an STL file to a GLB file. It uses trimesh library to read and export the files.

This script support batch processing, it keeps the original file name and directory structure.

## Installation

You need to have Python 3 installed in your system.

Its recommended to use a virtual environment to install the required libraries.

```bash
python -m venv venv
source venv/bin/activate
```

You can install the required libraries by running:

```bash
pip install -r requirements.txt
```

## Usage

For converting a single file, you can run the script with the following command:
```bash
python ./stl2glb.py -i ./input_path/file.stl -o ./output_path/
```

For batch processing, you can run the script with the following command:
```bash
python ./stl2glb.py -i ./input_path/ -o ./output_path/
```

## Arguments

- `-i` or `--input`: Path to the input file or directory.
- `-o` or `--output`: Path to the output directory.
- `--log-level` (optional): Log level for the script. Default is `WARNING`. Possible values are `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`.
- `-t` or `--threads` (optional): Number of threads to use for processing. Default is 1.

## Caution

This script will overwrite the output files if they already exist.