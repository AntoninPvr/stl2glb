import trimesh
import logging
import pathlib
from src.arguments import parse_arguments
from src.logger import init_logger

def input_path_to_file_list(input_path: pathlib.Path):
    """
    Convert input path to list of files

    return only .stl files

    :param input_path: str
    :return: list
    """
    if input_path.is_dir():
        files = list(input_path.rglob('*.[sS][tT][lL]*'))
    elif input_path.is_file() and (input_path.suffix == ".stl" or input_path.suffix == ".STL"):
        files = [input_path]
    else:
        raise ValueError("Input path is not a valid file or directory")
    if files == []:
        raise FileNotFoundError(f"No .stl files found in {input_path}")
    return files

def batch_export(input_files: list [pathlib.Path], output_path: pathlib.Path, input_path: pathlib.Path):
    """
    Export a list of files to glb format

    :param input_files: list
    :param output_path: pathlib.Path
    :param input_path: pathlib.Path
    :return: int (number of files exported)
    """
    nbr_exported = 0
    for file in input_files:
        # Create output file path with same directory structure as input
        if output_path is not None:
            if input_path.is_file(): # If input is a file, save in the same directory as the input file
                input_path = input_path.parent
            
            # Keep directory structure replacing input path with output path
            output_file = output_path / file.relative_to(input_path).with_suffix('.glb')

            # Create output directory if it does not exist
            if not output_file.parent.exists():
                output_file.parent.mkdir(parents=True)

        # If no output path is provided, save in the same directory as the input file
        else :
            output_file = file.with_suffix('.glb')

        mesh = trimesh.load_mesh(file)
        # Check if mesh is valid
        if mesh.is_empty:
            logging.error(f"{file} is empty")
            continue
        mesh.export(output_file)
        nbr_exported += 1

    return nbr_exported

def export_in_parallel(input_files, output_path, input_path, num_threads=4):
    import concurrent.futures
    from functools import partial
    """ Function to split export tasks across multiple threads. """
    # Split the files into chunks to distribute across threads
    chunk_size = len(input_files) // num_threads
    chunks = [input_files[i:i + chunk_size] for i in range(0, len(input_files), chunk_size)]
    
    # Create a partial function to pass arguments to `batch_export`
    partial_export = partial(batch_export, output_path=output_path, input_path=input_path)
    
    # Use ThreadPoolExecutor to process the chunks in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(partial_export, chunk) for chunk in chunks]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]

    # Sum the results to get the total number of files exported
    return sum(results)

def main():
    # Initialize logger
    logger = logging.getLogger(__name__)
    init_logger(logger)

    # Parse arguments
    args = parse_arguments()

    # Set log level
    logger.setLevel(args.log_level)

    # Get number of threads
    threads_amount = args.threads

    # get paths
    input_path = pathlib.Path(args.input_path)
    if args.output_path is None:
        if input_path.is_file():
            output_path = input_path.parent
        else:
            output_path = input_path
    else:
        output_path = pathlib.Path(args.output_path)

    # Get list of files to export
    input_files = input_path_to_file_list(input_path)
    logger.info(f"Exporting {len(input_files)} file{'s' if len(input_files) != 1 else ''}")

    # Export files
    if threads_amount == 1:
        nbr_exported = batch_export(input_files, output_path, input_path)
    else:
        logger.info(f"Exporting in parallel using {threads_amount} threads")
        nbr_exported = export_in_parallel(input_files, output_path, input_path, threads_amount)
    
    logger.info(f"Exported {nbr_exported}/{len(input_files)} file{'s' if nbr_exported != 1 else ''} to: {output_path}")

if __name__ == "__main__":
    main()