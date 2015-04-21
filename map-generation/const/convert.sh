#!/usr/bin/bash

for f in *.svg; do
    fit_canvas_to_drawing.sh $f
done
