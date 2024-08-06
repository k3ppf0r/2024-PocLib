import os  
  
def find_2024_directories(root_dir):  
    count = 0
    for item in os.listdir(root_dir):  
        full_path = os.path.join(root_dir, item)  
        if os.path.isdir(full_path) and item.startswith('2024'):  
            print("- "+ item)  # 打印目录名称  
            for filename in os.listdir(full_path):  
                print(f"  - {filename}")  
                count += 1
    print("poc count: ", count)
  
if __name__ == "__main__":  
    root_directory = os.path.dirname(__file__)  
    find_2024_directories(root_directory)