# 🍀 fortune_IT — A Simple Python Fortune Generator

A lightweight Python recreation of the classic **fortune** program, fully customizable and easy to extend.  
This version includes **extremely vulgar Italian quotes and black humor** and supports **ASCII art entries**, both chosen randomly on each run.
Please note that these quotes are inside jokes between me and my colleagues and friends at university, so don't expect anything cultural.

---

## 📁 Project Structure

```
fortune_IT/
├── fortune.py # Main executable script
├── README.md # Documentation
├── ascii_art/ # ASCII art files (.txt)
└── phrases/
└── phrases.txt # Quote file with '%' as separators
```

---

## ✨ Features

- Random quote or ASCII-art selection  
- Fully text-based, works in any terminal  
- Easy to add new quotes or new ASCII art  
- No external dependencies (pure Python)

---

## 🔧 Installation

Clone the repository:
```bash
git clone https://github.com/GiuseppeAngenica/Fortune-IT.git
cd fortune_IT
```

Make sure Python 3 is installed:
```bash
python3 --version
```

(Optional) Make the script executable:
```bash
chmod +x fortune.py
```

---

## ▶️ Usage

Run it directly:
```bash
python3 fortune.py
```

Or, if executable:
```bash
./fortune.py
```

---

## ⚡ Create a Terminal Alias (recommended)

You can run the program with a simple command like `fortune` by creating an alias.

### **Bash / Zsh**

Edit your configuration file:

```bash
nano ~/.bashrc
# or
nano ~/.zshrc
```

Add:

```bash
alias fortune="python3 <your path>/fortune_IT/fortune.py"
```

Reload:

```bash
source ~/.bashrc
# or
source ~/.zshrc
```

Now you can simply run:

```bash
fortune
```
### **Fish shell**

```fish
set -U fish_user_paths /path/to/fortune_IT $fish_user_paths
alias fortune "python3 /path/to/fortune_IT/fortune.py"
```

---

## 🚀 Run Automatically on Terminal Startup

If you want a fortune to appear every time you open a terminal:

### Bash / Zsh

Add this line to your `~/.bashrc` or `~/.zshrc`:

```bash
python3 <your path>/fortune_IT/fortune.py
```

### Fish

Add to `~/.config/fish/config.fish`:

```bash
python3 <your path>/fortune_IT/fortune.py
```

---

## ✍️ Add Your Own Quotes

Quotes are stored in:

```
phrases/phrases.txt
```

Each quote must be separated by a line containing only:

```
%
```

Example:

```
La fortuna aiuta gli audaci.
%
Siamo ciò che facciamo ripetutamente.
%
```

---

## 🎨 Add ASCII Art

Place any ASCII art file inside:

```
ascii_art/
```

Each file should be:

* A `.txt` file
* UTF-8 encoded
* Containing only the artwork

Example:

```
ascii_art/
 ├─ cat.txt
 ├─ dragon.txt
 └─ smiley.txt
```

The program will automatically detect and use all files in this folder.

---

## 📜 Example Output

```
  _________________________
< La vita è una prigione. >
  -------------------------
     \
      \
     .--.
    |o_o |  🍺  "burp..."
    |:_/ |
   //   \ \
  (|     | )
  /'\_   _/`\
  \___)=(___/
```

---

## 🤝 Contributing

Feel free to open issues or submit pull requests with new quotes, ASCII art, or code improvements.

---

## 📄 License

MIT License — free to use and modify.
