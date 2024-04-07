This is my little self-hosted project.

Performance is not guaranteed.

[Model SambaLingo-Russian-Base](https://huggingface.co/sambanovasystems/SambaLingo-Russian-Base)

Installation:

0. nvidia drivers
    - ```sudo apt install nvidia-driver nvidia-cuda-dev nvidia-cuda-toolkit```
    - checking: `nvidia-smi`
1. conda
    - ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```
    - ```./Miniconda3-latest-Linux-x86_64.sh```
2. Dependencies
    - ```conda install conda-forge::transformers```
    - ```conda install sentencepiece protobuf AutoModelForCausalLM```
    - ```conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia```
3. Launch
    - ```python3 bot.py```

Perhaps there are many more critical things missing here, but I am doing this project for myself.