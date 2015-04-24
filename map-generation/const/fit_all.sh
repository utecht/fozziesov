#!/usr/bin/bash
#
# Fit-canvas-to-drawing for all svgs in the current directory.
# Also sets up an Xvfb to handle the required inkscape gui output.
# This obviously requres Xvfb.
#

Xvfb :100 +extension RANDR -ac &
export DISPLAY=:100

for f in *.svg; do
    ./fit_canvas_to_drawing.sh "$f" 2> /dev/null
    echo "$f"
done

# Yeah, if you're running it elsehwere this will be bad
# so don't be.
killall Xvfb
