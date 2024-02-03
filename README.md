## Saves audio and inference information (update 18 May 2021)

Run 'python gui_tester.py'

## Google Colab notebook for inference (update 18 May 2021)

Upload 'NVIDIA_Tacotron2_Waveglow.ipynb' to new Google Colab Notebook.

## GUI Work in Progress (update 4 August 2020)
GUI wrapper for synthesize. Allows CPU-only synthesis via a toggleable switch. Portable exe file is available (that runs on CPU only).

Also plays TTS donations alerts from Stream Elements.

Main UI | Stream Elements integration
------------ | -------------
<img src="https://i.imgur.com/xeT74vJ.png" height="430" align="left">|<img src="https://i.imgur.com/tjC2q6j.png" height="430" align="left">
# Overview
A machine learning based Text to Speech program with a user friendly GUI. Target audience include Twitch streamers or content creators looking for an open source TTS program. The aim of this software is to make tts synthesis accessible offline (No coding experience, gpu/colab) in a portable exe.

## Features
  * Reads donations from Stream Elements automatically
  * PyQt5 wrapper for NVIDIA/tacotron2 & /waveglow

## Download Link
A portable executable can be found at the [Releases](https://github.com/lokkelvin2/tacotron2-tts-GUI/releases) page, or directly [here](https://github.com/lokkelvin2/tacotron2-tts-GUI/releases/download/v0.3/nvidia_waveglow-v0.3.1_x86_64.exe). Download a pretrained *Tacotron 2* and *Waveglow* model from below.

Warning: the portable executable runs on CPU which leads to a >10x speed slowdown compared to running it on GPU. 

# Building from source
## Requirements
  * Python >=3.7
  * librosa
  * numpy
  * PyQt5==5.15.0
  * requests
  * tqdm
  * matplotlib
  * scipy
  * num2words
  * pygame
  
[PyTorch 1.0](https://pytorch.org/)
  
## To Run
``` 
python gui.py
```
## License
* NVIDIA/tacotron2 & waveglow: BSD-3-Clause License

## Notes
  * TTS code from [NVIDIA/tacotron2](https://github.com/NVIDIA/tacotron2)
  * Partial GUI code from [https://github.com/CorentinJ/Real-Time-Voice-Cloning](https://github.com/CorentinJ/Real-Time-Voice-Cloning) and layout inspired by u/realstreamer's Forsen TTS [https://www.youtube.com/watch?v=kL2tglbcDCo](https://www.youtube.com/watch?v=kL2tglbcDCo)


# Original Repo: 

# Tacotron 2 (without wavenet)

PyTorch implementation of [Natural TTS Synthesis By Conditioning
Wavenet On Mel Spectrogram Predictions](https://arxiv.org/pdf/1712.05884.pdf).

This implementation includes **distributed** and **automatic mixed precision** support
and uses the [LJSpeech dataset](https://keithito.com/LJ-Speech-Dataset/).

Distributed and Automatic Mixed Precision support relies on NVIDIA's [Apex] and [AMP].

Visit our [website] for audio samples using our published [Tacotron 2] and
[WaveGlow] models.

![Alignment, Predicted Mel Spectrogram, Target Mel Spectrogram](tensorboard.png)


## Pre-requisites
1. NVIDIA GPU + CUDA cuDNN

## Setup
1. Download and extract the [LJ Speech dataset](https://keithito.com/LJ-Speech-Dataset/)
2. Clone this repo: `git clone https://github.com/NVIDIA/tacotron2.git`
3. CD into this repo: `cd tacotron2`
4. Initialize submodule: `git submodule init; git submodule update`
5. Update .wav paths: `sed -i -- 's,DUMMY,ljs_dataset_folder/wavs,g' filelists/*.txt`
    - Alternatively, set `load_mel_from_disk=True` in `hparams.py` and update mel-spectrogram paths
6. Install [PyTorch 1.0]
7. Install [Apex]
8. Install python requirements or build docker image
    - Install python requirements: `pip install -r requirements.txt`

## Training
1. `python train.py --output_directory=outdir --log_directory=logdir`
2. (OPTIONAL) `tensorboard --logdir=outdir/logdir`

## Training using a pre-trained model
Training using a pre-trained model can lead to faster convergence
By default, the dataset dependent text embedding layers are [ignored]

1. Download our published [Tacotron 2] model
2. `python train.py --output_directory=outdir --log_directory=logdir -c tacotron2_statedict.pt --warm_start`

## Multi-GPU (distributed) and Automatic Mixed Precision Training
1. `python -m multiproc train.py --output_directory=outdir --log_directory=logdir --hparams=distributed_run=True,fp16_run=True`

## Inference demo
1. Download our published [Tacotron 2] model
2. Download our published [WaveGlow] model
3. `jupyter notebook --ip=127.0.0.1 --port=31337`
4. Load inference.ipynb

N.b.  When performing Mel-Spectrogram to Audio synthesis, make sure Tacotron 2
and the Mel decoder were trained on the same mel-spectrogram representation.


## Related repos
[WaveGlow](https://github.com/NVIDIA/WaveGlow) Faster than real time Flow-based
Generative Network for Speech Synthesis

[nv-wavenet](https://github.com/NVIDIA/nv-wavenet/) Faster than real time
WaveNet.

## Acknowledgements
This implementation uses code from the following repos: [Keith
Ito](https://github.com/keithito/tacotron/), [Prem
Seetharaman](https://github.com/pseeth/pytorch-stft) as described in our code.

We are inspired by [Ryuchi Yamamoto's](https://github.com/r9y9/tacotron_pytorch)
Tacotron PyTorch implementation.

We are thankful to the Tacotron 2 paper authors, specially Jonathan Shen, Yuxuan
Wang and Zongheng Yang.


[WaveGlow]: https://drive.google.com/open?id=1rpK8CzAAirq9sWZhe9nlfvxMF1dRgFbF
[Tacotron 2]: https://drive.google.com/file/d/1c5ZTuT7J08wLUoVZ2KkUs_VdZuJ86ZqA/view?usp=sharing
[pytorch 1.0]: https://github.com/pytorch/pytorch#installation
[website]: https://nv-adlr.github.io/WaveGlow
[ignored]: https://github.com/NVIDIA/tacotron2/blob/master/hparams.py#L22
[Apex]: https://github.com/nvidia/apex
[AMP]: https://github.com/NVIDIA/apex/tree/master/apex/amp
