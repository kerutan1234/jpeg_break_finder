import os
from PIL import Image

def extract_and_save_thumbnail(jpeg_path, save_path):
    try:
        with Image.open(jpeg_path) as img:
            # EXIF情報からサムネイルデータを取得
            exif_data = img._getexif()
            if exif_data and 0x501B in exif_data:
                thumbnail_data = exif_data[0x501B]
                with open(save_path, 'wb') as f:
                    f.write(thumbnail_data)
                return True
    except Exception as e:
        print(f"Error occurred while processing {jpeg_path}: {e}")
    return False

def extract_thumbnails_from_folder(source_folder, destination_folder):
    # 出力ディレクトリが存在しない場合は作成
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # フォルダ内の全ファイルに対して処理
    for filename in os.listdir(source_folder):
        if filename.lower().endswith('.jpg'):
            jpeg_path = os.path.join(source_folder, filename)
            save_path = os.path.join(destination_folder, filename.replace('.jpg', '_thumbnail.jpg'))
            # サムネイル抽出
            if extract_and_save_thumbnail(jpeg_path, save_path):
                print(f"Extracted thumbnail from {filename}")
            else:
                print(f"Could not extract thumbnail from {filename}")

# 使用例
source_folder = 'a'
destination_folder = 'b'
extract_thumbnails_from_folder(source_folder, destination_folder)
