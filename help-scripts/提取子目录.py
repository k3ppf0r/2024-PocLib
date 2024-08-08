import os  
  
def find_2024_directories(root_dir):  
    count = 0
    dates = os.listdir(root_dir)
    sorted_dates_2024 = sorted(  
        [date for date in dates if date.startswith('2024-')],  
        key=lambda x: (-int(x.split('-')[0]), -int(x.split('-')[1]), str(x.split('-')[2]))  
    )  
    for item in sorted_dates_2024:  
        full_path = os.path.join(root_dir, item)  
        print("\n- "+ item)  # 打印目录名称  
        for filename in os.listdir(full_path):  
            print(f"  - {filename}") 
            if "2024用友" in filename:  
                yonyou_poc_path = os.path.join(full_path, filename)
                for yf in os.listdir(yonyou_poc_path):  
                    print(f"      - {yf}")
                    count += 1
            count += 1
    print("poc count: ", count)
  
if __name__ == "__main__":  
    root_directory = os.path.dirname(__file__)  
    find_2024_directories(root_directory)
