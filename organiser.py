import os
import shutil
import json
import logging
from datetime import datetime
from pathlib import Path


#-------------------------setup logging-------------------------

log_folder= Path(__file__).parent / "logs"
log_folder.mkdir(exist_ok=True)
logfile=log_folder / f"log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

logging.basicConfig(
    level=logging.INFO,                 #Record INFO messages, WARNING messages, and ERROR messages.
    format="%(asctime)s %(levelname)s  %(message)s",
    handlers=[
        logging.FileHandler(logfile),      #Save logs into the log file.
        logging.StreamHandler()            #print logs in the terminal while the program is running.
    ]
)
logger = logging.getLogger(__name__)

#-----------------------load config ---------------------------------------

def load_config()->dict:                    #This function is expected to return a dictionary.

    config_path= Path(__file__).parent/"config"/"config.json" 

    with open(config_path, "r") as f:
        return json.load(f)
#-----------------------main function-------------------------
def get_destination_folder(extension:str, rules:dict)->str:

    extension=extension.lower()

    for folder,extensions in rules.items():    #for key, value in dictionary.items():

        if extension in extensions: 
            return folder
        return "Others"
    
def organize_folder(target_path:str)->None:

    """
    Scan target_path and move every file into a subfolder
    based on its extension.
    """

    target= Path(target_path)
    if not target.exists():
        logger.error(f"Target path {target} does not exist.")
        return
    
    if not target.is_dir():
        logger.error(f"Target path {target} is not a folder.")
        return
    
    config=load_config()
    rules=config["rules"]

    skipped=0

    moved=0

    logger.info(f"Start organizing folder: {target}")
    logger.info("="*55)

    for items in target.iterdir():

        if items.is_dir() and items.name.startswith("."):
            #logger.info(f"Skip hidden folder: {item}")
            skipped+=1
            continue
        if os.path.isdir(items):
            continue  # This skips "Others", "Documents", and ALL folders!

        extension=items.suffix

        destination_folder_name=get_destination_folder(extension, rules)
        destination_folder=target/destination_folder_name

        #-------- create destination subfolder if it doesn't exist------------
        destination_folder.mkdir(exist_ok=True)

        destination_file=destination_folder/items.name

      #-------- if a file with same name exists, add a timestamp----------
        if destination_file.exists():
            stem=destination_file.stem
            suffix=destination_file.suffix
            timestamp=datetime.now().strftime("%Y%m%d%H%M%S")
            destination_file=destination_folder/f"{stem}_{timestamp}{suffix}"
        shutil.move(str(items), str(destination_file))
        logger.info(f"moved:{items} --> {destination_file}")
        moved+=1

    logger.info("="*55)
    logger.info(f"Done moved: {moved} | skipped:{skipped}")
    logger.info(f"log saved to: {logfile}")
#------------------entry point------------------------------
if __name__=="__main__":
    import sys

    if len(sys.argv) < 2:
        home= Path.home()
        downloads=home/"Downloads"
        print(f"no path is given,Using default path: {downloads}")
        organize_folder(str(downloads))
    else:
            organize_folder(sys.argv[1])


    
