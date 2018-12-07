from shutil import copyfileobj


def concat_files(*arr):
    with open('concatenated_files','w') as wfd:
        for f in arr:
            with open(f,'r') as fd:
                text = fd.read()
                if not text.endswith('\n'):
                    text += '\n'
                wfd.write(text)

