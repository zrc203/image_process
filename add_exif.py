import os
import re

from PIL import Image
import piexif as ef
import time

exif_dic = ef.load(Image.open('IMG.jpg').info['exif'])
del exif_dic['thumbnail']
g = os.walk(r'F:\我的照片\201209军训')
for dirpath, dirnames, filenames in g:
    for filename in filenames:

        file_path = f'{dirpath}\\{filename}'
        if 'psb' in filename:
            # filename = filename.replace('-', '')[:14]
            # old_time = time.strptime(filename, '%Y%m%d%H%M%S')
            # tar = time.strftime('%Y:%m:%d %H:%M:%S', old_time).encode()

            tar = b'2012:09:18 13:35:55'
            exif_dic['Exif'][36867] = tar
            exif_dic['Exif'][36868] = tar

            exif_dic['GPS'][2] = ((26, 1), (22, 1), (39712799, 1000000))
            exif_dic['GPS'][4] = ((106, 1), (38, 1), (44480400, 1000000))

            exif_byte = ef.dump(exif_dic)
            ef.insert(exif_byte, file_path)
            print(file_path)





