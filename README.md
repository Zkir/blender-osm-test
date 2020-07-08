# Test submodule for blender-osm
(c) Zkir 2020

## How does it work?

It runs blender-osm plug-in for sample OSM files, located in Samples directory,
and saves the results as x3d file, and then compares with etalons (samples).

If results match, everything is OK.
If plugin crashes or results are different, you should debug and find a error!
You can also see logs in the \output\ directory for each test.

## How to use it?
1. Set path to blender exe in config.py
2. Run test.py