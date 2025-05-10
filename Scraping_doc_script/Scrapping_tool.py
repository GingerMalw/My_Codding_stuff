import os
import glob
from datetime import datetime

folder_path = r"C:\Users\malwi\Desktop\Codding_stuff_MW\Python_myscripts\My_Codding_stuff\Scraping_doc_script\DataInput" 
output_folder = r"C:\Users\malwi\Desktop\Codding_stuff_MW\Python_myscripts\My_Codding_stuff\Scraping_doc_script\Created_data"

if __name__ == "__main__":
    input_files = glob.glob(os.path.join(folder_path, "*.txt"))
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

def extract_device_ids(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("DeviceID:"):
                ids = line.replace("DeviceID:", "").strip()
                ids = ids.strip('[]"')
                ids = ids.split('" OR "')
                return ids
    return []

def merge_device_ids(files):
    merged_ids = []
    for file_path in files:
        ids = extract_device_ids(file_path)
        merged_ids.extend(ids)
    
    merged_ids = list(set(merged_ids))
    return merged_ids

def save_merged_device_ids(output_file, merged_ids):
    with open(output_file, 'w') as file:
        merged_line = 'DeviceID: ["' + '" OR "'.join(merged_ids) + '"]'
        file.write(merged_line)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file_name = f"merged_devices_{timestamp}.txt"
output_file = os.path.join(output_folder, output_file_name)

merged_ids = merge_device_ids(input_files)
save_merged_device_ids(output_file, merged_ids)

print(f"Zapisano połączone DeviceID do pliku {output_file}")