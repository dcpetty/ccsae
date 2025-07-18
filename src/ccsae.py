#!/usr/bin/env python3
#
# ccsae.py
#
# CCSAE map on https://sites.google.com/view/coastal-climate-science/explainers.
#
# Assumptions:
# - rects is a list of N 4-tuples with upper left (x, y) and right (x, y)
# - links is a list of 2N strings where the first of the pair is alt text describing
#   the second of the pair link.
#
# Function:
# - Create a <div> element with other elements, including a <map> element:
#   <div>
#     <map name="ccsae-map">
#       <!-- ... -->
#     </map>
#     <!-- ... -->
#   </div>
# - create N <area> elements within the <map> element, for example:
#   <area shape="rect" coords="275,090,455,130"
#     href="https://sites.google.com/view/coastal-climate-science/explainers/increasing-co2"
#     alt="increasing co2 in the atmosphere"
#     onmouseover="light('a')" onmouseout="dark()" />
# - Add an <img> element after the <map> element:
#   <img id="ccsae" style="display: block; margin: auto; background-color: gold;"
#     usemap="#ccsae-map" src="https://dcpetty.dev/ccsae/images/fseicdace.png"
#     alt="ccsae" />
# - Add an <script> element after the <img> element:
#   <script>
#     const uri = `https://dcpetty.dev/ccsae/images/fseicdace`, ext = `.png`;
#     const img = document.querySelector(`img#ccsae`);
#     // console.log(img);
#     function light(id) { img.src = `${uri}-${id}${ext}`; }
#     function dark() { img.src = `${uri}${ext}`; }
#   </script>
#   The <script> element includes two functions: light(id) and dark(). These are
#   triggered by the onmouseover and onmouseout <area> events. They change the src
#   <img> property to images that reflect the mouse position associated with the area.
# - Write the completed <div> to output_path.
#

import os.path as op

# Constant parameters for the image.
# DW, DH    default width & height from top-left corner to bottom-right corner
# DX, DY    adjustments to every (X, Y) coordinate   
# COLOR     show-through color for transparent .PNG files
# WIDTH     for use with f"https://drive.google.com/thumbnail?sz=w{WIDTH}"
# SEP       .CSV separator
# VER       CCSAE explainer image version
DW, DH, DX, DY, COLOR, WIDTH, SEP, VER = 120, 40, 0, 0, 'gold', 740, '\t', '0.5', 
image_base = 'https://dcpetty.dev/ccsae/images/fseicdace'   # base URI of images
image_ext = '.png'                                          # URI image extension
output_path = '../ccsae.html'                               # output path for .HTML

# Rectangle coordinates (a list of 16 4-tuples) for the image map areas A - P.
rects = [ (t[0] + DX, t[1] + DY, t[2] + DX, t[3] + DY, ) if len(t) == 4
    else (t[0] + DX, t[1] + DY, t[0] + DX + DW, t[1] + DY + DH, )
        for t in (
(275,  90, 455, 130, ), # A
(385, 195, 530, 225, ), # B
(120, 255, 220, 305, ), # C
(245, 280, ),           # D
(440, 275, 535, 335, ), # E
(555, 280, ),           # F
(585, 375, ),           # G
(460, 435, 540, 490, ), # H
(375, 475, 450, 515, ), # I
(550, 470, 650, 520, ), # J
(200, 545, 265, 615, ), # K
(285, 560, 370, 610, ), # L
(450, 540, 575, 600, ), # M
(560, 615, 660, 675, ), # N
(280, 755, 380, 810, ), # O
(460, 785, 600, 835),   # P
) ]

# A list of description followed by URI for 16 image map areas from text.
links = [ l for l in """
Increasing CO2 in the atmosphere
https://sites.google.com/view/coastal-climate-science/explainers/increasing-co2
Warmer air and the greenhouse effect
https://sites.google.com/view/coastal-climate-science/explainers/warmer-air
Ocean acidification
https://sites.google.com/view/coastal-climate-science/explainers/ocean-acidification
Warmer ocean water
https://sites.google.com/view/coastal-climate-science/explainers/warmer-ocean
More water vapor in the air
https://sites.google.com/view/coastal-climate-science/explainers/more-water-vapor
Melting glaciers and ice sheets
https://sites.google.com/view/coastal-climate-science/explainers/melting-glaciers
Regional changes in water salinity
https://sites.google.com/view/coastal-climate-science/explainers/water-salinity
More clouds and turbulence
https://sites.google.com/view/coastal-climate-science/explainers/More-clouds 
Rising sea level
https://sites.google.com/view/coastal-climate-science/explainers/sea-level
Changes in water density
https://sites.google.com/view/coastal-climate-science/explainers/water-density
Less dissolved oxygen in water
https://sites.google.com/view/coastal-climate-science/explainers/less-dissolved-oxygen
Harmful algal blooms (HABs)
https://sites.google.com/view/coastal-climate-science/explainers/algal-blooms
Extreme and changing weather
https://sites.google.com/view/coastal-climate-science/explainers/extreme-weather
Changes to Atlantic Ocean circulation
https://sites.google.com/view/coastal-climate-science/explainers/ocean-circulation
Harm to marine life
https://sites.google.com/view/coastal-climate-science/explainers/harm-to-marine
Harm to human and terrestrial life
https://sites.google.com/view/coastal-climate-science/explainers/harm-to-human
""".split('\n') if l ]
# print(links)

# Create .CSV rows.
lr, ll = len(rects), len(links) // 2
assert lr == ll, f"#rects ({lr}) \u2260 #links ({ll})"
rows = [SEP.join(
    [ chr(ord('a') + i) ] + [ str(c) for c in r ]
        + [ links[2 * i + 1] ] + [ links[2 * i] ])
    for i, r in enumerate(rects) ]
# print('\n'.join(rows))

# HTML templates for area, map, and doc.
html_area_temp = """  <area shape="rect" coords="{coords}" href="{href}" alt="{alt}"
    onmouseover="light('{id}')" onmouseout="dark()" />"""
html_map_temp = f"""<map name="ccsae-map">
{{rects}}
</map>"""
html_doc_temp = """<!-- https://dcpetty.dev/ccsae/ v{ver} -->
<div>
{imap}
<img id="ccsae" style="display: block; margin: auto; background-color: {stc};"
  usemap="#ccsae-map" src="{uri}{ext}" alt="ccsae" />
<script>
  const uri = `{uri}`, ext = `{ext}`;
  const img = document.querySelector(`img#ccsae`);
  // console.log(img);
  function light(id) {{ img.src = `${{uri}}-${{id}}${{ext}}`; }}
  function dark() {{ img.src = `${{uri}}${{ext}}`; }}
</script>
</div>
"""

# Create HTML for areas, map, and doc.
html_areas = '\n'.join([
    html_area_temp.format(coords=','.join(f"{c:03d}" for c in rects[i]),
        href=links[2 * i + 1], alt=links[2 * i].lower(), id=chr(ord('a') + i))
            for i in range(len(rects))
])
# print(html_areas)

html_map = map=html_map_temp.format(rects=html_areas)
# print(html_map)

html_doc = html_doc_temp.format(
    ver=VER, imap=html_map, stc=COLOR, uri=image_base, ext=image_ext)
# print(html_doc)

# Write html_doc to path.
path = op.realpath(op.join(op.dirname(op.realpath(__file__)), output_path))
with open(path, 'w') as f:
    print(f"Writing {path}...")
    f.write(html_doc)
"""
# Print links in original order 'AFBCDEHGIKLJMNOP', then alt text in original order.
print()
for i in range(len(links)):
    if i % 2 == 0: print(links[i])
print()
for i in range(len(links)):
    if i % 2 == 1: print(links[i])
"""
# A Google Drive image link format is:
# image_uri = f"https://drive.google.com/thumbnail?sz=w{WIDTH}&id=1ar4V1rMkHv4eR4sxu3aK1VeCSMSKssRM"

