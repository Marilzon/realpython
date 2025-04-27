import glob
from datetime import datetime
input_path = glob.glob("real_cases/extract_tables_from_rpt/data/*.rpt")[-1]


print(input_path)
