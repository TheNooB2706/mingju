<!-- Add banner here -->

# 中学生背名句
Mingju is one of the hardest but easiest to score part in SPM Chinese examination. Hardest because it involves memorising of a bunch of idioms, but easiest because well it is the only section that you can prepare for the exam and be sure that it will come out, thus becoming a must score section. As a person who absolutely hate memorising stuff, I created this tool to aid the memorising process, and hopefully also help anyone who struggles with the same problem. This tool is intended to help you memorise mingju without asking your friend to test your progress (or when you don't have friends :().

Currently it has to ability to help you memorise the mingju itself (fill in the blank, which is the easiest of all), zhushi as well as hanyi (by computing similarity score using difflib).

# Demo-Preview

<!-- Add a demo for your project -->

![Demo](https://i.ibb.co/4RGyGp2/mingjudemo.gif)

# Table of contents
- [Project Title](#project-title)
- [Demo-Preview](#demo-preview)
- [Table of contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [Contribute](#contribute)
- [License](#license)
- [Footer](#footer)

# Installation
[(Back to top)](#table-of-contents)  

**Download releases.**
1. Download [release](https://github.com/TheNooB2706/mingju/releases) for your system.  
   **Windows**  
   Download `mingju_windows_XXX.exe` file. x86 for 32bit system, x86_64 for 64bit system  
   **Linux**  
   Download `mingju_linux_XXX` file. x86 for 32bit system, x86_64 for 64bit system. Then make it executable: `chmod +x mingju_linux_XXX`  
   **Mac**
   Pending
2. Run.  
   **Windows**  
   Double click on the file downloaded. It should be launched.  
   **Linux**
   Open terminal in the directory you put the file, then execute it: `./mingju_linux_XXX`
   **Mac**
   Pending

**Installation instruction for Android phones**
1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=en&gl=US).
2. Open Termux app.
3. Install git and python.
```
pkg install git python
```
4. Clone the repository.
```
git clone git://github.com/TheNooB2706/mingju.git
```
5. Change directory to "mingju".
```
cd mingju
```
6. Install requirements.
```
pip install -r requirements.txt
```
7. Run the program.
```
python mingju.py
```

**"Build" from source** *Well you know, tihs is written in python, so you don't need to build anything*
1. Clone the repo (install git first). **Alternatively** you can download the repo as zip file at top right corner.  
```
git clone git://github.com/TheNooB2706/mingju.git
```  
2. Install python.
3. Install the requirements
```
cd mingju
pip install -r requirements.txt
```  
4. Run the code.
```
python mingju.py
```

# Usage
[(Back to top)](#table-of-contents)  

After executing the program, you should be inside the "mingju shell".
![Mingjushell](https://i.ibb.co/s63246X/Screenshot-20201116-125243.png)
Now you can use the program by various commands.

List of commands:
1. `help`  
  `help` to list available commands, `help <command>` for help of specified command.
2. `train`  
  Launch training. Training will begin with infinite loop on the selected mingju until you press Ctrl-C to exit. Questions that are answered wrongly will show up more frequent.  
  USAGE: `train {form4|form5|all} [<start>] [<end>] [--p]`  
  `<start>` and `<end>` is used to specify scope of Mingju to select. (TYPE=integer)  
  `<start>` is the index of first mingju, whereas `<end>` is the index of last mingju. All mingju between these two will be taken.  
  --p is an option to enable probabilistic mode. The probability of a question that never came out in SPM showing up is higher than that came out, and older questions will have a higher probability of showing up than newer questions.  
  **Examples:**  
  ![traintype](https://i.ibb.co/w7VMJrZ/mingjutrainf4f5.gif)
  *`train` followed by either `form4`, `form5` or `all` to select specific category of mingju*  
  ![trainindex](https://i.ibb.co/5FPR9Hf/mingjutrainindex.gif)
  *`train <category> <x> <y>` to select only xth to yth mingju in the selected category. In the above gif example, only the 10th to 20th mingju from form5 will be selected for training.*  
  ![trainp](https://i.ibb.co/QDxCsYy/mingjutrainp.gif)
  *Use `--p` to enable probabilistic mode, where the frequency of mingju coming out is based on past year analysis. You can use together with index, just make sure to append it last.*  
3. `quiz`  
  Launch quiz. Ctrl-C to quit. `quiz` differs from train in terms of:  
    1) `quiz` will not provide any answer at the time of answering.  
    2) One question will only appear once.  
    3) Score will be shown once quiz is finished.  
  USAGE: `quiz {form4|form5|all} [<start>] [<end>]`  
  `<start>` and `<end>` is used to specify scope of Mingju to select. (TYPE=integer)  
  `<start>` is the index of first mingju, whereas `<end>` is the index of last mingju. All mingju between these two will be taken.  
  **Examples:**  
  The usage is similar to `train`, except there are no probabilistic mode in `quiz`. Please refer to the example of `train` command.
4. `zhushi`  
  Training mode for zhushi. Loop infinitely until you press Ctrl+C to quit. Questions that are answered wrongly will show up more frequent.  
  USAGE: `zhushi {form4|form5|all} [--p]`  
  `--p` enable probabilistic training.  
  **Examples:**  
  The usage is similar to `train`, except there are no index.  
5. `hanyi`  
  Training mode for hanyi. Ctrl-C to quit.  
  USAGE: `hanyi {form4|form5|all} [<start>] [<end>] [--p]`  
  `<start>` and `<end>` is used to specify scope of Mingju to select. (TYPE=integer)  
  `<start>` is the index of first mingju, whereas `<end>` is the index of last mingju. All mingju between these two will be taken.  
  `--p` enable probabilistic training.  
  **Examples:**  
  The usage is exactly same as `train`. Refer examples at `train`.  
6. `list`  
  List mingju according to the arguments provided.  
  USAGE: `list {form4|form5|all} [<start>] [<end>] [-z] [-h]`  
  `<start>` and `<end>` is used to specify scope of Mingju to select. (TYPE=integer)  
  `<start>` is the index of first mingju, whereas `<end>` is the index of last mingju. All mingju between these two will be taken.  
  Use `-z` to print zhushi, `-h` to print hanyi, or both to print both of them.  
  **Examples:**  
  The usage is similar to train, with extra `-z` and `-h` options.  
  ![listcat](https://i.ibb.co/6vdNVRb/mingjulistcat.gif)
  *`list <category>`, similar to train*
  ![listz](https://i.ibb.co/k9SGPq5/mingjulistz.gif)
  *Append `-z` to include zhushi*
  ![listh](https://i.ibb.co/WkGjmyn/mingjulisth.gif)
  *Append `-h` to include hanyi*
  ![listzh](https://i.ibb.co/z8z4qmB/mingjulistzh.gif)
  *Or both to include both*

# Contribute
[(Back to top)](#table-of-contents)  

Features request? Found bugs? Typo? Open an [issue](https://github.com/TheNooB2706/mingju/issues). Or if you don't have a GitHub account, email me at `noobchannel2706@gmail.com`.

Also a Chinese README translation would be nice. I have tried translating myself, but it is too weird so I gave up.

# License
[(Back to top)](#table-of-contents)

[GNU General Public License version 3](https://opensource.org/licenses/GPL-3.0)

# Footer
[(Back to top)](#table-of-contents)

Find me on instagram @py.i.nc and subscribe me at youtube: https://www.youtube.com/channel/UC2YiviEyZGj0NfaaY4y7cHQ
