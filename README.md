# HyperionAnimations

Keyframe animation files for the Reanimation list of HyperionElite. The hub downloads `index.json` and shows every animation in it; a tap downloads that one file.

* `animations/<Category>/<Name>.lua`: one animation per file, data only: `return {["Name"]={ {Time=0,Data={["LeftFoot"]=CFrame.new(...)}}, ... }}` (the Keyframe Recorder's `local C=CFrame.new return{...}` form works too).
* `index.json`: rebuilt automatically on every push to `animations/` (GitHub Action `index`), or by `python tools/anim_repo.py index` on the owner's PC.
* To add animations: drop `.lua` files into `animations/<Category>/` (GitHub web page: Add file > Upload files) or run `python tools/anim_repo.py add <folder> --push`. The hub's list updates by itself within a few minutes.
* The hub only runs a downloaded file after it checks that the file contains nothing but keyframe data (numbers, strings, `CFrame.new`, `Time`, `Data`); anything else is ignored.

The files are community-collected avatar animation data; the sources carry no license. If you are the author of a file and want it removed, open an issue and it goes.
