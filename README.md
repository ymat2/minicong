# MiniConG
<u>Mini</u>mal hands-on for <u>Com</u>parative <u>G</u>enomics

Slide url: https://ymat2.github.io/slides/minicong/minicong.html

## Requirements
- Unix-like environment
	- `git`, `wget`
- Python3 (>= 3.9.0)
- homebrew
	- blast

## Pipeline
```bash
git clone https://github.com/ymat2/minicong.git
cd minicong
sh src/get_sequence.sh
sh src/run_blastp.sh

## optionally
# python3 src/summarize_results.py -i result/Canis_lupus_dingo.ASM325472v1.blastp -n Dingo -o result/Dingo.res.txt
# python3 src/summarize_results.py -i result/Canis_lupus_familiaris.ROS_Cfam_1.0.blastp -n Dog -o result/Dog.res.txt
```
