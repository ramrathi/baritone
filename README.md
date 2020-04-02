# baritone
Oh Grandma! What a deepVoice you have

A ready-to-use, voice to text, wrapper library based on a pretrained version of Mozilla and Baidu's DeepSpeech architecture. Made this to reduce the manual labour needed to run these models on personal projects. Wanted to make this as easy to use as possible so that anyone can download and use, all within a few minutes.

[Work in progress as of 2/4/20]

What I plan on doing (and have done): 
- Direct Youtube video-to-text support
- Local MP3,MP4,WAV,M4A files supported
- Ultimate caching using audio fingerprinting so that if the system has heard something before, it doesn't have to go throught the whole proccess again and just retrieves from the DB. (Thanks [Dejavu](https://github.com/worldveil/dejavu) )
- Automatic download and setup of pretrained model
- Real time audio stream compatible
- A no-bullshit library, that you can just import and run state of the art voice to text in, without worrying about the hassles of file conversions, downloads, pretrained/training models, etc.
- Dockerfile included
- Support for pip
- ... and more feautures that I'll think of while making this in the next few weeks


Feel free to:
- Add support for popular podcast platforms
- Add more file type compatibilty
