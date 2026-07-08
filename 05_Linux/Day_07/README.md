# 🐧 Linux - Day 02

## 📅 Date
08 July 2026

---

# 📖 Introduction

Today I learned some of the most commonly used Linux file management commands.

These commands are essential for every developer because they help create directories, create files, read file contents, inspect file information, and manage files efficiently using the terminal.

---

# 📚 Topics Covered

- mkdir
- touch
- cat
- tac
- stat
- touch -a
- touch -m

---

# 1️⃣ mkdir Command

## Definition

`mkdir` stands for **Make Directory**.

It is used to create one or more new directories (folders).

---

## Syntax

```bash
mkdir directory_name
```

---

## Example

```bash
mkdir Projects
```

---

## Create Multiple Directories

```bash
mkdir Python Cpp DSA
```

---

## Create Nested Directories

```bash
mkdir -p College/MCA/Sem1
```

---

## Use Cases

- Create project folders
- Organize source code
- Create nested directory structures

---

# 2️⃣ touch Command

## Definition

The `touch` command is used to create empty files or update file timestamps.

---

## Syntax

```bash
touch filename
```

---

## Example

```bash
touch file1.txt
```

---

## Create Multiple Files

```bash
touch file1.txt file2.txt file3.txt
```

---

## Update Access Time

```bash
touch -a file.txt
```

Only updates the **Access Time** of the file.

---

## Update Modification Time

```bash
touch -m file.txt
```

Only updates the **Modification Time** of the file.

---

## Use Cases

- Create source code files
- Create README files
- Update timestamps
- Create configuration files

---

# 3️⃣ cat Command

## Definition

`cat` stands for **Concatenate**.

It is mainly used to display file contents.

---

## Syntax

```bash
cat filename
```

---

## Example

```bash
cat file1.txt
```

---

## Create a File Using cat

```bash
cat > notes.txt
```

Press **CTRL + D** after entering the content.

---

## Merge Multiple Files

```bash
cat file1.txt file2.txt > merged.txt
```

---

## Display Merged File

```bash
cat merged.txt
```

---

## Use Cases

- Read configuration files
- View logs
- Merge files
- Create text files directly from the terminal

---

# 4️⃣ tac Command

## Definition

`tac` is the reverse of `cat`.

It displays the contents of a file from the last line to the first.

---

## Syntax

```bash
tac filename
```

---

## Example

```bash
tac merged.txt
```

---

### Example Output

If the file contains:

```text
Line 1
Line 2
Line 3
```

`tac` displays:

```text
Line 3
Line 2
Line 1
```

---

## Use Cases

- Reverse log files
- Read files from bottom to top
- Debugging

---

# 5️⃣ stat Command

## Definition

The `stat` command displays detailed information about a file.

---

## Syntax

```bash
stat filename
```

---

## Example

```bash
stat merged.txt
```

---

## Information Displayed

- File Size
- Permissions
- Owner
- Group
- Access Time
- Modify Time
- Change Time
- Inode Number

---

## Use Cases

- Check file permissions
- Debug file issues
- View timestamps
- Inspect metadata

---

# 📂 Practical Commands Performed

## Created a Directory

```bash
mkdir Day_02
```

---

## Created Multiple Files

```bash
touch file1.txt file2.txt
```

---

## Added Content

```bash
cat > file1.txt

cat > file2.txt
```

---

## Merged Files

```bash
cat file1.txt file2.txt > merged.txt
```

---

## Displayed File

```bash
cat merged.txt
```

---

## Displayed File in Reverse

```bash
tac merged.txt
```

---

## Displayed File Information

```bash
stat merged.txt
```

---

## Updated Access Time

```bash
touch -a merged.txt
```

---

## Updated Modification Time

```bash
touch -m merged.txt
```

---

# 📊 Command Summary

| Command | Purpose |
|----------|----------|
| `mkdir` | Create directories |
| `touch` | Create files / Update timestamps |
| `cat` | Display or merge file contents |
| `tac` | Display file contents in reverse |
| `stat` | Show detailed file information |
| `touch -a` | Update Access Time |
| `touch -m` | Update Modification Time |

---

# 💼 Real-World Applications

### mkdir

- Create project folders
- Organize repositories
- Create application structure

---

### touch

- Create source code files
- Create README files
- Create configuration files

---

### cat

- Read log files
- Merge configuration files
- Display file contents

---

### tac

- Read logs in reverse order
- Debug applications

---

### stat

- Verify permissions
- Check timestamps
- Inspect file metadata

---

# 🧠 Interview Questions

### What does `mkdir` do?

Creates one or more directories.

---

### What is the purpose of the `touch` command?

Creates empty files or updates file timestamps.

---

### What is the difference between `cat` and `tac`?

- `cat` displays a file from top to bottom.
- `tac` displays a file from bottom to top.

---

### What information does `stat` provide?

- File size
- Permissions
- Owner
- Timestamps
- Inode number

---

### What is the difference between `touch -a` and `touch -m`?

- `touch -a` updates only the Access Time.
- `touch -m` updates only the Modification Time.

---

# 🎯 Key Takeaways

- Learned to create directories using `mkdir`.
- Learned to create multiple files using `touch`.
- Learned to display and merge files using `cat`.
- Learned to display files in reverse using `tac`.
- Learned to inspect file metadata using `stat`.
- Learned how to update access and modification timestamps.

---

# 📂 Folder Structure

```text
Day_02/
│
├── file1.txt
├── file2.txt
├── merged.txt
├── Practice_1.png
├── Practice_2.png
└── README.md
```

---

# 📈 Linux Progress

## Day 01 ✅

- cp
- mv
- rm
- find
- grep

---

## Day 02 ✅

- mkdir
- touch
- cat
- tac
- stat
- touch -a
- touch -m

---

# 🚀 Next Topics

- pwd
- cd
- ls (Advanced Options)
- head
- tail
- wc
- chmod
- chown
- history
- alias

---

# 🚀 CodeEveryday Challenge

Learning Linux one command at a time by practicing every concept directly from the terminal and documenting each command with examples, outputs, and real-world use cases.

**Learn • Practice • Document • Repeat** 🐧