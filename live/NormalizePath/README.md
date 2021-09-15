# Normalize Path

Given a string s containing an absolute Unix-based directory path write a program that normalizes this path using the following rules.

Input:

```bash
"/usr/local//./../bin/."
```

Output:

```bash
"/usr/bin"
```

Input:

```bash
"/home/../.."
```

Output:

```bash
"/"
```

Input:

```bash
"/etc/system/../../home/user"
```

Output:

```bash
"/home/user"
```
