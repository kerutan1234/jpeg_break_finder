from PIL import Image
import io

# JPEGファイルのパス
file_path = 'a/1.jpg'

# サムネイルの情報（ヘッダーの位置とサムネイルの長さ）
thumbnail_offset = 0x3ADA  # サムネイルへのポインタの位置を指定
thumbnail_length = 5175    # サムネイルのバイト数を指定

# 画像ファイルをバイナリモードで開く
with open(file_path, 'rb') as f:
    # サムネイルのデータが格納されている位置に移動
    f.seek(thumbnail_offset)
    # サムネイルのデータを読み取る
    thumbnail_data = f.read(thumbnail_length)

# サムネイルのデータからPILイメージを作成
thumb_img = Image.open(io.BytesIO(thumbnail_data))

# サムネイルを表示
thumb_img.show()

# サムネイルをファイルに保存
thumb_img.save('a/thumbnail.jpg')