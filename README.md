# unifont  
Used unifont version is 13.0.02  
Unifont to `*.fnt` experiments  

---
## Trying to create font `*.fnt`, which include glyphs from unifont, for use in libgdx game/app gui's  
Completed with few additional fixes.  
bmfont64.exe created `*.fnt` fail with some gui ethiopia symbols  
gdx-fontpack.jar created `*.fnt` success with:  
- create full unicode txt (using python `hex.py` , that extract hex and convert into html, then copy from html into txt)
- copypast into `edit` popup -> wait close to minute, text appear in window -> ok
- long lags 12 minutes on empty pc
- possibly `save` button alive after `system activity` manual stop java, then continue again + multiclicks
- after few minutes appear png's , then after few minutes appear `*.fnt` file
- libgdx fail to load because no space between id= and x= , after id=10000
- manually added space before `x=` uses vscode
- success, ethiopia display symbols, failed before, in tested gui from new unifont release(13.0.02)
- compression of png  

  - `FOcompressedFail` - png compressed using file optimizer. Looks good in viewers but libgdx display broken textures in font gui  
  - `Gimp` - `FOcompressedFail` files -> gimp2.10.14 -> image -> mode -> indexed -> use black and white (1bit palette) no checkboxes. Work correct in libgdx, but not so compressed as FO version  

---
## Trying to create font `*.fnt`, which include glyphs from 49 languages, for use in libgdx game/app gui's  
0-general  
languages:  
1-english  
20200523 not completed