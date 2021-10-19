"""
# PROBLEM 17 [HARD]

This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext


The directory dir contains an empty sub-directory subdir1 and a sub-directory
subdir2 containing a file file.ext.

The string:
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t" +
    "subsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory `dir` contains two sub-directories `subdir1` and `subdir2`.
`subdir1` contains a file `file1.ext` and an empty second-level sub-directory
`subsubdir1`. `subdir2` contains a second-level sub-directory `subsubdir2`
containing a file `file2.ext`.

We are interested in finding the longest (number of characters) absolute path to
a file within our file system. For example, in the second example above, the
longest absolute path is `"dir/subdir2/subsubdir2/file2.ext"`, and its length is
32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to a file in the abstracted file system. If
there is no file in the system, return 0.

Note:
- The name of a file contains at least a period and an extension.
- The name of a directory or sub-directory will not contain a period.
"""

def longest_path(file_sytem: str) -> int:
    """
    Returns longest path length of the provided filesystem str representation.
    Time: O(N) being N the length of file_system objects
    Space: O(N) being N the amount of objects in the longest path
    """
    file_objects: list[str] = file_sytem.split('\n')
    path_list: list = []
    longest: int = 0
    for file_object in file_objects:
        prefix: str = "\t" * len(path_list)
        if file_object.startswith(prefix) or len(path_list) == 0:
            path_list.append(file_object.removeprefix(prefix))
        else:
            if "." in path_list[-1]:
                longest = max(len('/'.join(path_list)), longest)
            while file_object.startswith(prefix) is False and path_list:
                path_list.pop()
                prefix: str = "\t" * len(path_list)
            path_list.append(file_object.removeprefix(prefix))

    if "." in path_list[-1]:
        return max(len('/'.join(path_list)), longest)

    return longest


if __name__ == "__main__":
    test_cases: list = [
        {
            "input_path": "",
            "longest": 0
        },
        {
            "input_path": "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext",
            "longest": 20 # dir/subdir2/file.ext
        },
        {
            "input_path": "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t" +
                "subdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext",
            "longest": 32 # dir/subdir2/subsubdir2/file2.ext
        },
        {
            "input_path": "dir\n\tf1.txt\n\tsubdir\n\t\tsubsubdir\nf1.txt",
            "longest": 10 # dir/f1.txt
        },
        {
            "input_path": "dir\n\tsubdir\n\t\tsubsubdir\nf1.txt",
            "longest": 6 # f1.txt
        }
    ]

    for test_case in test_cases:
        assert longest_path(test_case["input_path"]) == test_case["longest"]

    print("Successfully tested.")
