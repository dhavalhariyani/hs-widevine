NicAudio.dll v2.0.6 (2012-08-27) - AviSynth Audio Plugins for MPEG Audio/AC3/DTS/LPCM and other uncompressed formats

AviSynth USAGE
--------------

Syntax:
   AC3:  NicAC3Source("FileName.ac3", int "Channels", int "DRC")
   DTS:  NicDTSSource("FileName.dts", int "Channels", int "DRC")
   MPA:  NicMPG123Source("FileName.mpa", bool "Normalize")
   LPCM: NicLPCMSource("FileName.lpcm", int "SampleRate", int "SampleBits", int "Channels")
   RAW:  RaWavSource("FileName.raw", int "SampleRate", int "SampleBits", int "Channels")

Where:
   "Channels"   Maximum number of channels to output (Downmix). Optional.
   "DRC"        Apply Dynamic Range Compression algorytm. 0  means nothing (default), 1 means Normal
   "Normalize"  Apply the max gain without clip signal. Default false.
   "Channels"   Necessary for lpcm and raw files. Max 8 channels.
   "SampleBits" Necessary for lpcm and raw files. Valid values 8/16/24/32 (also 33 (32 float) for raw)
                (lpcm also accept 20 and -8/-16/-24/-32. Negative values are for BluRay lpcm (big-endian))
   "SampleRate" Necessary for lpcm and raw files. In RaWavSource a value < 9 means a header with valid
                values for SampleRate/SampleBits/Channels and now means:
   IgnoreLength 1 force ignore the data size read in the header also in 64 bits formats.
                2 ignore the data size 32 bits read in the header if > 2GB. (default)
                4 ignore the data size 32 bits read in the header if > 4GB.

Supported files (all can be > 4GB):
   ac3          (TODO: support also eac3 files or Dolby Digital Plus)
   dts          also dtswav supported
   mpa          mpeg files: mp1, mp2 and mp3
   lpcm         from DVD Audio, from BluRay with -SampleBits
   raw          and uncompressed formats: WAV, WAVE_FORMAT_EXTENSIBLE, W64, BWF, RF64, AU, AIFF and CAF

Examples:

LoadPlugin("NicAudio.dll")
NicAC3Source("c:\File.ac3")

NicDTSSource("c:\File.dts", DRC=1)

NicMPG123Source("File.mp3")

NicLPCMSource("c:\File.lpcm", 48000, -24, 6)

RaWavSource("File.w64", 4)


CHANGE LOG
----------
27/08/2012 Tebasuna 2.0.6
ac3,dts  Solved some initialization issues with no-linear decode.
         http://forum.doom9.org/showthread.php?p=1587337
lpcm,raw Some minor improvements.

25/10/2011 Tebasuna 2.0.5
dts   Accepted special stereo dts modes Lt+Rt, A+B (dual mono)...

12/08/2009 Tebasuna 2.0.4
lpcm  Solved bug writing last block in some cases

25/06/2009 Tebasuna 2.0.3
mpa   Skip ID3v2,3,4 initial tag to avoid false sync frames.

24/09/2008 Tebasuna 2.0.2
mp3   Anoying message supress.
ac3   1MB (at least 13 sec) initial garbage assumed like delay instead reject the file.
      Now ac3 delayed with VirtualDub style are delayed acordly (same behaviour than standard players).
dts   Correct decode more amod+lfeon options instead automatic downmix. Support for padded dts.
      Core extraction in DTS HD. Seems work fine with DTS High Res. (CBR),
      still in beta stage with DTS Master Audio (VBR) please report any problem.
rawav Not needed first parameter, by default assumed ignorelength if > 2GB
      Improved w64 support.

09/04/2008 Tebasuna 2.0.1
mpg123-lib bugfix. Some message go by stdout instead stderr and corrupt the audio data output when using 'pipe' with Bepipe/Wavi.

29/02/2008 Tebasuna
ac3, bugfix 'dsurmod' http://forum.doom9.org/showthread.php?p=1071730#post1071730
ac3, bugfix some 'acmod' options http://forum.doom9.org/showthread.php?p=977363#post977363
lpcm, bugfix if 'count' > 'Left', BluRay option, and clean code (excluded wav).
mpg123, include last (WarpEnterprises) version http://forum.doom9.org/showthread.php?p=1102957#post1102957
rawav, to support uncompressed formats.
libmad, deprecated.
all, support for files > 4 GB, vfm deprecated.

21/08/2007 IanB
Cleaned up and derestricted LPCM code. Returns all channels to Avisynth in 16 or
24 bit integer format. Channel order as per LPCM source file.

12/08/2007 Nic
Added support for 24 bit LPCM wav files. Now will only covert 24 bit LPCM to 32 bit when
the number of channels is not 2 or 6.

13/08/2007 Nic
Fixed stupid bug where 24 bit wasn't getting output (thanks tebasuna51)

06/03/2006 Dimzon
Added DRC option and NicMPG123Source to support mp3 files (mpg123 lib)

04/07/2005 Nic
First version ?


CREDITS
-------
All credit should go to the excellent creator of these original filters
used in FilmShrink.sf.net - Attila T. Afra

Filters compiled and gathered together by Nic. All under the GPL.

patched by dimzon (dimzon541@gmail.com)

Nic patch for 44.1khz AC3 (by tebasuna51) + fixes for corrupt streams

patched by IanB, Aug 2007

patch by Tebasuna, Feb 2008: ac3, lpcm blu-ray, rawav, > 4 GB.

TODO
----
- eac3, mlp, truehd (ffmpeg)
- dts hd (now can extract only the core)
