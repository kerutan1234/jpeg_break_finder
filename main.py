"""
画像データ (jpg, png, gif など) の
破損をチェックする Python コード例。
check_image_files.py
"""

from pathlib import Path
import re
from traceback import format_exception_only
from PIL import Image # Pillow ライブラリ
import os
import shutil
import time
import pprint
from tqdm import tqdm

def main():

    """メイン関数"""
    print('start')

    # (1/4) 画像ファイルの場所を決めます。
    #add="C:/Users/SZ6/Nextcloud/画像/jpg"
    print("ファイルの場所入力　R:/画像")
    add=input()
    dirlist=[]
    os.listdir(add)
    os.makedirs(add+'/ngfile2', exist_ok=True)
    for curDir in os.walk(add):
        dirlist.append(curDir[0].replace(os.sep,'/'))
    pprint.pprint(dirlist)
    nglist=[]
    for i in tqdm(dirlist):
        #print(i)
        src_dir = Path(i)
        # (2/4) フォルダの中のファイルを列挙します。
        for p in src_dir.glob('*'):
            # ファイルでなければ、スキップします。
            if not p.is_file():
                continue

            # 拡張子が画像でなければ、スキップします。
            # p.suffix: パスの拡張子の部分。
            # re.IGNORECASE: 大文字小文字を無視。
            if not re.match(r'^\.(?:jpg|png|gif|jpeg|bmp|ico|raw|svg|tif|wmf)$', p.suffix, flags=re.IGNORECASE):
                continue

            # (3/4) 画像ファイルを開きます。
            with p.open('rb') as f:

                # (4/4) 画像データをチェックします。
                try:
                    # PIL で画像データを開きます。
                    # PIL が『画像形式を判定できなかった場合』は、
                    # UnidentifiedImageError の例外が発生しました。
                    im = Image.open(f, 'r')
                    # 画像データの破損をチェックします。
                    # ベリファイに失敗した場合は、
                    # SyntaxError などの例外が発生しました。
                    im.verify()
                except Exception as e:
                    # 何らかのエラーがあった。
                    #print(f'NG {p.name} {e.__class__.__name__}')

                    # e に msg 属性があれば取得、無ければ None にしておきました。
                    msg = getattr(e, 'msg', None)
                    #print(f'(message) {msg}')

                    # トレースバックの最後の行だけを取得してみました。
                    ex_text = format_exception_only(type(e), e)[0].rstrip('\n')
                    #print(f'(exception) {ex_text}')
                    nglist.append(p)
                else:
                    # エラーは検出できなかった。
                    #print(f'ok {p.name}')
                    pass
    print('end')
    for move in nglist:
         os.remove(move)
    return


if __name__ == '__main__':
    main()
