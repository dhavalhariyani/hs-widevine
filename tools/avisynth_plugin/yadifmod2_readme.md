#yadifmod2
## Yet Another Deinterlacing Filter mod  for Avisynth2.6/Avisynth+

	yadifmod2 = yadif + yadifmod

### Info:

	version 0.0.4

### Requirement:
	- Avisynth2.6.0final/Avisynth+r1576 or greater.
	- WindowsVista SP2 or later.
	- Visual C++ Redistributable Packages for Visual Studio 2015.

### Syntax:

	yadifmod2(clip, int "order", int "field", int "mode", clip "edeint", int "opt")

####	clip -

		All planar formats( YV24 / YV16 / YV12 / YV411 / Y8 ) are supported.

####	order -

		Set the field order.

		-1(default) = use avisynth's internal parity value
		 0 = bff
		 1 = tff

####	field -

		Controls which field to keep when using same rate output.

		-1 = set eqal to order.(default)
		 0 = keep bottom field.
		 1 = keep top field.

		This parameter doesn't do anything when using double rate output.

####	mode -

		Controls double rate vs same rate output, and whether or not the spatial interlacing check is performed.

		0 = same rate, do spatial check.(default)
		1 = double rate, do spatial check.
		2 = same rate, no spatial check.
		3 = double rate, no spatial check.

####	edeint -

		Clip from which to take spatial predictions.

		If this is not set, yadifmod2 will generate spatial predictions itself as same as yadif.

		This clip must be the same width, height, and colorspace as the input clip.
		If using same rate output, this clip should have the same number of frames as the input.
		If using double rate output, this clip should have twice as many frames as the input.

####	opt -

		Controls which cpu optimizations are used.

		 0 = Use C routine.
		 1 = Use SSE2 routine.
		 2 = Use SSE2 + SSSE3 routine if possible. When SSSE3 can't be used, fallback to 1.
		 3 = Use AVX2 routine if possible. When AVX2 can't be used, fallback to 2.(default)

### Note:

		- yadifmod2_avx2.dll is for AVX2 supported CPUs.(it is compiled with /arch:AVX2).


### Changelog:

	0.0.0(20160305)
		initial release

	0.0.1(20160308)
		Chage default value of 'opt' to -1 and remove wrong description.
		This filter does not require 32byte alignment.

	0.0.2(20160318)
		Fix wrong calculation of spatial predictions when opt > 1.
		Thanks to Fizick the report.

	0.0.3(20160320)
		Add missing prediction score update.
		Also, fix previous frame position when n == 0.
		now, the outputs of yadifmod2 w/o edeint clip are almost same as yadif1.7 except edge part of image.

	0.0.4(20160527)
		Set filter mode as MT_NICE_FILTER automatically on Avisynth+MT.
		Disable AVX2 code if /arch:AVX2 is not set.


###Source code:

	https://github.com/chikuzen/yadifmod2/

