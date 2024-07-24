import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\cjk\Downloads'

# 파일 유형별 이동할 폴더 경로
folders = {
    'images': ['jpg', 'jpeg'],
    'data': ['csv', 'xlsx'],
    'docs': ['txt', 'doc', 'pdf'],
    'archive': ['zip']
}

# 각 폴더의 경로 설정
folders_paths = {key: os.path.join(download_folder, key) for key in folders}

# 폴더가 없으면 생성
for path in folders_paths.values():
    if not os.path.exists(path):
        os.makedirs(path)

# 파일 이동 함수
def move_files(file_extension_list, destination_folder):
    for file_name in os.listdir(download_folder):
        if file_name.split('.')[-1] in file_extension_list:
            src_path = os.path.join(download_folder, file_name)
            dst_path = os.path.join(destination_folder, file_name)
            shutil.move(src_path, dst_path)
            print(f'Moved: {file_name} to {destination_folder}')

# 각 파일 형식에 대해 파일 이동
for folder_name, extensions in folders.items():
    move_files(extensions, folders_paths[folder_name])

print("파일 이동이 완료되었습니다.")
