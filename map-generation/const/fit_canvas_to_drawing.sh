#!/usr/bin/bash
#
# Use inkscape to fit an svg canvas to the drawing (as with the verbs below)
# Note: this cannot be done without the GUI opening for each file, which 
# means it is VERY slow. If you omit the FileQuit verb it will appear faster
# at first, but then it leaves a window open for every file converted,
# so once you get past 10 or 20 the whole thing craps out.
#
# You could use Xvfb or use vncserver or some such to supress the GUI otuput.
#

inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose --verb=FileQuit "$1"
