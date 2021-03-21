import pandas
from robot.api.deco import keyword
from robot.api.logger import librarylogger as logger
import random


class DataReader(object):

    def __init__(self) -> None:
        super().__init__()

    @keyword('Read sheet ${sheet} from exel file ${file}')
    def read_excel_file(self, sheet: str, file: str):
        excel_df = pandas.read_excel(file, sheet)
        return excel_df.to_dict('index')

    @keyword('Select random ${field} from ${input_dictionary}')
    def select_random_record(self,field: str = '', input_dictionary: dict = None ):
        random_record = random.choice(input_dictionary)
        if field != '':
            try:
                return random_record[field]
            except Exception as ex:
                logger.error(ex)
                return None
        else:
            return random_record

    @keyword('Find records which have ${field} is ${value} in ${input_dict}')
    def find_records_by_field(self, field: str, value: str, input_dict: dict):
        list_records = []
        for record in input_dict:
            if str(input_dict[record][field]).lower() == value.lower():
                list_records.append(input_dict[record])
        return list_records
