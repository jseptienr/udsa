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
    files = os.listdir(path)
    #print(l)
    for file in files:
        filepath = path + '/' + file
        if os.path.isfile(filepath):
            if filepath.endswith(suffix):
                file_matches.append(filepath)
        else:
            file_matches.extend(find_files(suffix, filepath))
    return file_matches

#print_directory('/home/septienj/projects/udacity-dsa/python/P1/testdir')
matches = find_files('.c', 'testdir')
for match in matches:
    print(match)
