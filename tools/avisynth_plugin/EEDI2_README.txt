
                        EEDI2 v0.9.2 (June 07, 2006) -- README



INFO:


    ** Only YV12 and YUY2 colorspaces are currently supported

      EEDI2 resizes an image by 2x in the vertical direction by copying the existing
   image to 2*y(n) and interpolating the missing field.  It is intended for edge-directed
   interpolation for deinterlacing (i.e. not really made for resizing a normal image, but
   can do that as well).


   syntax =>  EEDI2(int mthresh, int lthresh, int vthresh, int estr, int dstr, int maxd,
                       int field, int map, int nt, int pp)



Parameters:


   mthresh/lthresh/vthresh -

       These all control edge detection used for building the initial edge map.  mthresh
       is the edge magnitude threshold... its range is from 0 to 255, lower values will
       detect weaker edges.  lthresh is the laplacian threshold... its range is 0 to 510,
       lower values will detect weaker lines.  vthresh is the variance threshold... its
       range is 0 to a large number, lower values will detect weaker edges.  Use the "map"
       option to tweak these settings as needed.

       default -  mthresh = 10  (int)
                  lthresh = 20  (int)
                  vthresh = 20  (int)


   estr, dstr -

       These are used for dilation and erosion of the edge map.  estr sets the required
       number of edge pixels (<=) in a 3x3 area, in which the center pixel has been
       detected as an edge pixel, for the center pixel to be removed from the edge map.
       dstr sets the required number of edge pixels (>=) in a 3x3 area, in which the
       center pixel has not been detected as an edge pixel, for the center pixel to be
       added to the edge map.  Use the "map" option to tweak these settings as needed.

       default -   estr = 2  (int)
                   dstr = 4  (int)


   maxd -

       Sets the maximum pixel search distance for determining the interpolation direction.
       Larger values will be able to connect edges and lines of smaller slope but can
       lead to artifacts.  Sometimes using a smaller maxd will give better results than
       a larger setting.  The maximum possible value for maxd is 29.

       default -  24  (int)


   field -

       Controls which field in the resized image the original image will be copied too.
       When using avisynth's internal parity value top field first (tff) = 1 and bottom
       field first (bff) = 0.  Possible options:

         -2 = alternates each frame, uses avisynth's internal parity value to start
         -1 = uses avisynth's internal parity value
          0 = bottom field
          1 = top field
          2 = alternates each frame, starts with bottom
          3 = alternates each frame, starts with top

       default -  -1  (int)


   map -

       Allows one of three possible maps to be shown.  Possible settings:

          0 - no map
          1 - edge map
                 Edge pixels will be set to 255 and non-edge pixels
                 will be set to 0.
          2 - original scale direction map
          3 - 2x scale direction map

       default -  0  (int)


   nt -

       Defines a noise threshold between pixels in the sliding vectors, this is used to
       set initial starting values.  Lower values should reduce artifacts but sacrifice
       edge reconstruction... while higher values should improve edge recontruction but
       lead to more artifacts.  The possible range of values is 0 to 256.

       default -  50  (int)


   pp -

       Enables two optional post-processing modes aimed at reducing artifacts by identifying
       problems areas and then using plain vertical linear interpolation in those parts.
       The possible settings are:

          0 - no post-processing
          1 - check for spatial consistency of final interpolation directions
          2 - check for junctions and corners
          3 - do both 1 and 2

       Using the pp modes will slow down processing and can cause some loss of edge
       directedness.

       default -  1  (int)



CHANGE LIST:


   06/07/2006  v0.9.2

       + various internal changes to help reduce artifacts around repeated
            patterns and to improve construction of lines/edges with small
            slope
       - Changed map from bool to int
       - Changed default maxd value from 12 to 24
       - Changed default pp value from 0 to 1
       - a few minor bugfixes


   04/03/2006  v0.9.1

       + Added pp parameter and pp modes 1, 2, and 3
       - A few minor internal changes
       - Fixed some documentation errors (field parameter)
       - do a vi.SetFieldBased(false) in constructor
       - fixed a bug causing reads past the last line and incorrect interpolation
            of the very top or very bottom line in some cases


   11/29/2005  v0.9

       - Initial release


TODO:


   - add generalized resize version (resize to any resolution in one step).
        Should provide much better results on resizing of progressive images
        than chaining multiple eedi2() calls together.



contact:   forum.doom9.org  nick = tritical  or  email:  kes25c@mizzou.edu
