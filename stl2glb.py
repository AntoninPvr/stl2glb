import trimesh
import logging
from src.arguments import parse_arguments
from src.logger import init_logger

def main():
    # Initialize logger
    logger = logging.getLogger(__name__)
    init_logger(logger)

    args = parse_arguments()
    # get file name
    file_name = args.input_file
    output_file = args.output_file
    
    # Load STL file
    if file_name is None:
        raise ValueError("No input file provided")
    else:
        mesh = trimesh.load_mesh(file_name)
        logger.info(f"Loaded file: {file_name}")

    # Export GLB file
    if output_file is None:
        output_file = file_name.rsplit('.', 1)[0]  # Removes last '.' and everything after
        output_file += ".glb"

    logger.info(f"Exported file: {output_file}")
    mesh.export(output_file)

if __name__ == "__main__":
    main()