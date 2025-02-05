# File: logger.py
"""
This file contains the logger
"""
import logging
import os.path

def init_logger(logger=None, log_level="INFO", file_path=None, file_path_level="DEBUG"):
    logger.setLevel(logging.DEBUG)
    
    # Console
    ch = logging.StreamHandler()
    try:
        numeric_level = getattr(logging, log_level.upper(), None)
        ch.setLevel(numeric_level)
    except:
        ch.setLevel(logging.DEBUG)
    ch_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_formatter)
    logger.addHandler(ch)
        
    # File
    if file_path is not None:
        try: 
            fh = logging.FileHandler(file_path)
            try: 
                fh.setLevel(file_path_level)
            except:
                fh.setLevel(logging.DEBUG)
                
            fh_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(fh_formatter)
            logger.addHandler(fh)
            logger.info(f"log file available at: {file_path}")
        except:
            logger.error("File log error")