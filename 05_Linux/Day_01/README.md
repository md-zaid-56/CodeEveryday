# 🐧 Day 002 - Linux File Management & Search Commands

> Learning essential Linux commands for file management, searching, and command-line productivity.

---

# 🎯 Objective

Understand the basic Linux commands used daily by software developers for:

- Creating files and directories
- Copying and moving files
- Renaming files
- Searching files and folders
- Searching text inside files
- Viewing command history

---

# 📚 Topics Covered

- `touch`
- `mkdir`
- `cp`
- `cp -r`
- `mv`
- `find`
- `grep`
- `cat`
- `history`
- `tree`

---

# 📂 Directory Structure

```
Day_002/
│
├── C++
│   └── renamed_file.txt
│
├── python
│   └── file.txt
│
├── python_backup
│   └── file.txt
│
└── file.txt
```

---

# 📄 touch

Creates a new empty file.

### Syntax

```bash
touch filename
```

### Example

```bash
touch file.txt
```

Output

```
file.txt
```

---

# 📁 mkdir

Creates a new directory.

### Syntax

```bash
mkdir folder_name
```

### Example

```bash
mkdir python
```

Output

```
python/
```

---

# 📋 cp

Copies files.

### Syntax

```bash
cp source destination
```

### Example

```bash
cp file.txt copy_file.txt
```

Result

```
file.txt
copy_file.txt
```

Both files exist.

---

## Copy File into Another Folder

```bash
cp file.txt python/
```

Result

```
python/
└── file.txt
```

---

## Copy Entire Directory

The `-r` flag stands for **recursive**.

```bash
cp -r python python_backup
```

Result

```
python/
python_backup/
```

---

# 🚚 mv

Moves or renames files and folders.

---

## Move File

```bash
mv copy_file.txt C++/
```

Result

```
C++/
└── copy_file.txt
```

---

## Rename File

```bash
mv C++/copy_file.txt C++/renamed_file.txt
```

Result

```
renamed_file.txt
```

---

## Rename Directory

```bash
mv python python_notes
```

---

# 🔍 find

Searches files and directories.

---

## Find All Text Files

```bash
find . -name "*.txt"
```

Example Output

```
./file.txt
./python/file.txt
./python_backup/file.txt
./C++/renamed_file.txt
```

---

## Find All Directories

```bash
find . -type d
```

---

## Find Specific Directory

```bash
find . -type d -name "C++"
```

---

# 📖 cat

Displays file contents.

### Example

```bash
cat file.txt
```

Output

```
Hiii this is text from "file.txt"
```

---

# 🔎 grep

Searches for text inside files.

### Syntax

```bash
grep "text" filename
```

### Example

```bash
grep "copied" file.txt
```

Output

```
Hiii this is text from "file.txt" and will be copied...
```

---

## Show Line Numbers

```bash
grep -n "copied" file.txt
```

Example

```
1:Hiii this is text...
```

---

## Recursive Search

```bash
grep -rn "return" .
```

Useful for searching entire projects.

---

# 📜 history

Displays previously executed commands.

### Example

```bash
history
```

Example Output

```
601 mkdir python
602 cp file.txt copy_file.txt
603 find . -name "*.txt"
604 history
```

---

# 🌳 tree

Displays the directory structure in a tree format.

### Example

```bash
tree
```

Output

```
.
├── C++
│   └── renamed_file.txt
├── file.txt
├── python
│   └── file.txt
└── python_backup
    └── file.txt
```

---

# 💡 Additional Useful Commands

## pwd

Shows the current working directory.

```bash
pwd
```

---

## clear

Clears the terminal screen.

```bash
clear
```

Shortcut

```
Ctrl + L
```

---

## which

Finds the location of an executable.

```bash
which python3
```

Example

```
/usr/bin/python3
```

---

## echo

Prints text to the terminal.

```bash
echo "Hello Linux"
```

Create a file

```bash
echo "Python" > notes.txt
```

Append text

```bash
echo "Machine Learning" >> notes.txt
```

---

## head

Displays the first 10 lines of a file.

```bash
head README.md
```

---

## tail

Displays the last 10 lines of a file.

```bash
tail README.md
```

Follow a log file

```bash
tail -f app.log
```

---

# 📊 Commands Summary

| Command | Purpose |
|----------|----------|
| `touch` | Create files |
| `mkdir` | Create directories |
| `cp` | Copy files |
| `cp -r` | Copy directories |
| `mv` | Move or rename files/directories |
| `find` | Search files and folders |
| `grep` | Search text inside files |
| `cat` | Display file contents |
| `history` | Show command history |
| `tree` | Display directory structure |

---

# 🧠 Key Takeaways

- Linux commands are case-sensitive.
- `cp` creates copies, while `mv` moves or renames files.
- Use `cp -r` to copy directories.
- `find` helps locate files and folders.
- `grep` searches for specific text inside files.
- `cat` displays file contents.
- `history` helps reuse previously executed commands.
- `tree` provides a visual representation of the directory structure.

---

# 🎯 Interview Questions

### Q1. Difference between `cp` and `mv`?

- `cp` copies files/directories.
- `mv` moves or renames files/directories.

---

### Q2. Why is `-r` required with `cp`?

Because directories contain multiple files and subdirectories. The `-r` option copies them recursively.

---

### Q3. Difference between `find` and `grep`?

- `find` searches for files/directories.
- `grep` searches for text inside files.

---

### Q4. What does `grep -n` do?

Displays matching lines along with their line numbers.

---

### Q5. What does `history` do?

Displays previously executed terminal commands.

---

# 🏷️ Tags

`Linux` `Ubuntu` `CLI` `File Management` `Terminal` `Developer Tools`

---

# 📅 Day 2 Status

✅ File Creation  
✅ Directory Creation  
✅ Copy Files  
✅ Copy Directories  
✅ Move & Rename Files  
✅ Search Files  
✅ Search Text  
✅ View File Contents  
✅ Command History  
✅ Directory Tree

---

**Next Topic:** Git Fundamentals (Working Tree, Staging Area, Repository & Essential Git Commands)
