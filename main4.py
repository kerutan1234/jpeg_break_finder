from PIL import Image
import os

def extract_thumbnail_from_exif(jpeg_path):
    with Image.open(jpeg_path) as img:
        exif_data = img._getexif()
        if exif_data:
            # PILライブラリはサムネイルを(0x501B)キーで格納します
            thumbnail_data = exif_data.get(0x501B)
            if thumbnail_data:
                # サムネイルデータをバイナリとして書き込む
                thumbnail_path = jpeg_path.replace('.jpg', '_thumbnail.jpg')
                with open(thumbnail_path, 'wb') as f:
                    f.write(thumbnail_data)
                print(f"サムネイルを抽出して保存しました: {thumbnail_path}")
                return thumbnail_path
            else:
                print("サムネイルがEXIFデータに含まれていません。")
        else:
            print("EXIFデータが見つかりませんでした。")

# 使用例
jpeg_path ='a/1.jpg'
extract_thumbnail_from_exif(jpeg_path)
