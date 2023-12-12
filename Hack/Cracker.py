import pyzipper

zip_file_path = 'Hack/Crack_me.zip'
output_dir = './Hack/'

for i in range(7000):
    m = str(i)
    while len(m) < 4:
        m = '0' + m
    s = eval(f"b'{m}'")
    try:
        with pyzipper.AESZipFile(zip_file_path) as zf:
            zf.pwd = s
            zf.extractall(output_dir)
        print("Extraction successful! Password is: {}".format(m))
        break
    except Exception:
        print(m)