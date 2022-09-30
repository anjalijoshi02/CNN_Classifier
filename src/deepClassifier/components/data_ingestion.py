import os
import urllib.request as request
from zipfile import ZipFile

from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from tqdm import tqdm


class DataIngestion:
    def __init__(self, config=DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Downloading file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("download started ...")
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded with following info : \n{headers}")
        else:
            logger.info(f"File  already exists")

    def _get_updated_list_of_files(self, list_of_files):
        return [
            f
            for f in list_of_files
            if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)
        ]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)
    def unzip_and_clean(self):
        logger.info(f"unzippinf the file and removing unwanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = (
                zf.namelist()
            )  # this will give the list of files inside the zip file
            updated_list_of_files = self._get_updated_list_of_files(
                list_of_files=list_of_files
            )
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)
