Это мой маленький селфхостед проект. 

Работоспособность не гарантируется.

[Модель SambaLingo-Russian-Base](https://huggingface.co/sambanovasystems/SambaLingo-Russian-Base)

Установка:

0. nvidia драйвера
    - ```sudo apt install nvidia-driver nvidia-cuda-dev nvidia-cuda-toolkit```
    - проверка: `nvidia-smi`
1. conda
    - ```wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh```
    - ```./Miniconda3-latest-Linux-x86_64.sh```
2. зависимости
    - ```conda install conda-forge::transformers```
    - ```conda install sentencepiece protobuf AutoModelForCausalLM```
    - ```conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia```
3. запуск
    - ```python3 bot.py```

возможно тут пропущено еще много чего критичного но этот проект я делаю для себя.