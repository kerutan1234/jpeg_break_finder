import os
import io
from PIL import Image, UnidentifiedImageError

def find_jpeg_thumbnail(data):
    start_marker = b'\xff\xd8'
    end_marker = b'\xff\xd9'
    start = data.find(start_marker, 2)  # ファイルの先頭にある主要なJPEG画像をスキップ
    if start != -1:
        end = data.find(end_marker, start)
        if end != -1:
            return start, end + len(end_marker)
    return None, None

def extract_and_save_thumbnail(jpg_path, output_dir):
    try:
        with open(jpg_path, 'rb') as f:
            data = f.read()

        thumbnail_offset, thumbnail_end = find_jpeg_thumbnail(data)

        if thumbnail_offset and thumbnail_end:
            thumbnail_data = data[thumbnail_offset:thumbnail_end]
            try:
                thumb_img = Image.open(io.BytesIO(thumbnail_data))
                
                # 出力ファイル名を作成（元のファイル名に基づく）
                file_name = os.path.basename(jpg_path)
                output_path = os.path.join(output_dir, file_name)
                thumb_img.save(output_path)

                print(f"サムネイルを保存しました: {output_path}")
            except UnidentifiedImageError:
                print(f"サムネイルが破損しています（スキップ）: {jpg_path}")
        else:
            print(f"サムネイルを見つけることができませんでした: {jpg_path}")
    except IOError:
        print(f"ファイルを読み取ることができませんでした（スキップ）: {jpg_path}")

# 入力フォルダと出力フォルダ
input_dir = 'a'
output_dir = 'output_thumbnails'

# 出力フォルダが存在しない場合は作成
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 入力フォルダ内の全てのJPEGファイルを処理
for file in os.listdir(input_dir):
    if file.lower().endswith('.jpg') or file.lower().endswith('.jpeg'):
        jpg_path = os.path.join(input_dir, file)
        extract_and_save_thumbnail(jpg_path, output_dir)
