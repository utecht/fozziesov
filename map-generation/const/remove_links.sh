#!/usr/bin/bash
#
# Replace all a tags with g tags in all svgs in the current directory.
# This requires the a tags to be on a line by themselves, and probably
# is only useful for these dotlan map svgs.
#

echo "Removing links from all svgs..."
sed -i 's/<a.*$/<g>/g;s/<\/a>/<\/g>/g' *.svg
