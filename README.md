# baritone
Oh Grandma! What a deepVoice you have

A ready-to-use, voice to text, wrapper library based on a pretrained version of Mozilla and Baidu's DeepSpeech architecture. Made this to reduce the manual labour needed to run these models on personal projects. Wanted to make this as easy to use as possible so that anyone can download and use, all within a few minutes.

[Work in progress as of 2/4/20]

What I plan on doing (and have done): 
- Direct Youtube video-to-text support
- Local MP3,MP4,WAV,M4A files supported
- Caching to prevent redoing urls you've already processed
- Automatic download and setup of pretrained model
- Real time audio stream compatible
- A no-bullshit library, that you can just import and run state of the art voice to text in, without worrying about the hassles of file conversions, downloads, pretrained/training models, etc.
- Dockerfile included
- Support for pip
- ... and more feautures that I'll think of while making this in the next few weeks


Feel free to:
- Add support for popular podcast platforms
- Add more file type compatibilty
- Add some sort of a caching system. Have been thinking of trying this out but I doubt I'll ever get to it, but basically trying to index audio files somehow such that you can reduce the usage of resources if you've come across a certain audio segment before. (URL and file caching is easy, wanted something that works irrespective of that)
