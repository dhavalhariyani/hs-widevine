Warning! This is ALPHA version!


Syntax:
WavGainLimiter( Clip c, Float factor)
LinearLimiter( Clip c, Float factor)
ExpotencialLimiter( Clip c, Float factor)
	factor - proposed values are 1.0...5.0, default is 1.0
	! Higher factor values increases the effect but can produce atrifacts

SoftClipperFromAudX( Clip c, Float curve)
	curve - proposed values are 0.0...1.0, default is 0.7

Pupose:
To increase volume for silent sounds a lot, to increase volume for middle-volume sounds a little and to keep hi-volume sounds untoched.
This must help to increase volume for speech/dialog without increasing volume for shoots etc
Higher factor values increases the effect but can produce atrifacts. Recomended value between 1.0 and 5.0
This filter reques Normalized Float audio at input. 



Math explained
 for expotential:
	output = (input<0?-1:1)*(pow(10.0f, tanh( factor * log10(1 + abs(input)*9))/tanh(factor) ) - 1)/9
 for linear:
	output = tanh( factor * input) / tanh(factor)
		

############################################
Sample:


wavSource(...)
convertAudiotofloat()
normalize()
LinearLimiter(2)