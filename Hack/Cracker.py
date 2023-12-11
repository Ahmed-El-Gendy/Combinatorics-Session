import pyzipper

zip_file_path = 'Crack_me0.zip'
output_dir = '.'

for i in range(1600):
    s = eval("b'{}'".format(i))
    try:
        with pyzipper.AESZipFile(zip_file_path) as zf:
            zf.pwd = s
            zf.extractall(output_dir)
        print("Extraction successful! Password is: {}".format(i))
        break
        exit()
    except Exception:
        print(i)