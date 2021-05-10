File: Readme_UnDot.txt

//  UnDot - Simple Deringing Dot Remover
//	Copyright (C) 2002 Tom Barry  - trbarry@trbarry.com
//
//	This program is free software; you can redistribute it and/or modify
//	it under the terms of the GNU General Public License as published by
//	the Free Software Foundation; either version 2 of the License, or
//	(at your option) any later version.
//
//	This program is distributed in the hope that it will be useful,
//	but WITHOUT ANY WARRANTY; without even the implied warranty of
//	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//	GNU General Public License for more details.
//
//	You should have received a copy of the GNU General Public License
//	along with this program; if not, write to the Free Software
//	Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

Also, this program is "Philanthropy-Ware".  That is, if you like it and feel
the need to reward or inspire the author then please feel free (but not obligated) 
to consider joining or donating to the Electronic Frontier Foundation. This will 
help keep cyber space free of barbed wire and bullsh*t.  

See their web page at www.eff.org

***************

Okay, on to business. 

WARNING - This version only runs on the Avisynth 2.5 alpha release.

UnDot is a simple median filter for removing dots, that is stray orphan pixels and 
mosquito noise.  It basicly just clips each pixel value to stay within min and max
of its eight surrounding neigbors.


USAGE - To use it just:

1) Place the UnDot.dll in a directory somewhere. You can get it from 
   www.trbarry.com/UnDot.zip

2) In your Avisynth file use commands similar to 

    LoadPlugin("F:\UnDot\UnDot.dll")
    Avisource("D:\wherever\myfile.avi")
    UnDot()
	
Of course replace the file and directory names with your own.  There are no parameters.


KNOWN ISSUES AND LIMITATIONS

1) 	Requires either YUY2 or YV12 input.        

2)  Sorry, currently requires a P-III, Athlon, or higher. Needs SSEMMX support.

3)  So far it has only been tested on SSEMMX (P3 & P4) machines.

4)  In YV12 format it will filter both luma and chroma.  In YUY2 format it will
    only filter luma.

FILE LOCATIONS

For now, both source, this readme, and DLL should be at:
	
	www.trbarry.com/UnDot.zip

A copy of this Readme_UnDot.txt file should be at:
  	
	www.trbarry.com/Readme_UnDot.txt

***************

Change Log:


2003/01/18  V 0.0.1.1  Use AvisynthPluginInit2

2002/11/03  V 0.0.1.0  Initial test release for Avisynth 2.5 alpha only





























