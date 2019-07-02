import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    file_matches = []

    if suffix is '':
        return file_matches

    try:
        files = os.listdir(path)
    except:
        return file_matches

    for file in files:
        filepath = path + '/' + file
        if os.path.isfile(filepath):
            if filepath.endswith(suffix):
                file_matches.append(filepath)
        else:
            file_matches.extend(find_files(suffix, filepath))
    return file_matches



# TESTS
matches = find_files('.c', 'testdir')
print('pass' if len(matches) == 4 and matches[0].endswith('.c') else 'fail')

matches = find_files('.c', '')
print('pass' if len(matches) == 0 else 'fail')

matches = find_files('', 'testdir')
print('pass' if len(matches) == 0 else 'fail')

matches = find_files('.xxxx', 'testdir')
print('pass' if len(matches) == 0 else 'fail')
