for f in *.svg; do
    inkscape --verb=FitCanvasToDrawing --verb=FileSave --verb=FileClose --verb=FileQuit $f
done
