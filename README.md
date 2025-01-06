# ccsae

Files for generating [HTML](./ccsae.html) to go with [*Coastal Climate Science &mdash; Activities and Experiments*](https://sites.google.com/view/coastal-climate-science) (CCSAE) [explainers](https://sites.google.com/view/coastal-climate-science/explainers).

The process of developing this `<div>` is as follows:

- Start with an [image](./images/fseicdace-740x850.png) with 14 *buttons* and a list of 14 corresponding *URIs* (with their corresponding descriptions).
- After [Photoshop](https://www.adobe.com/products/photoshop.html)ping the [image](./images/fseicdace-740x850.png) to a $740 \times 850$ format, make a [map](https://drive.google.com/file/d/1FprjDBazKrCQTaQn9zqDLBZvqCTdRRNK/) of coordinates of 14 *rectangles* corresponding to the 14 *buttons*.
- Write a [Python](https://docs.python.org/3/) [script](./src/ccsae.py) to parse / compose the inputs and create the `<img>` [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map) and [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements where the *buttons* link to the *URIs*.

As a secondary process, add some [JavaScript](https://typescriptlang.org/) functions for `onmouseover` and `onmouseout` that swap the images in and out for 14 [images](https://github.com/dcpetty/ccsae/tree/main/images) that have the additional letters *'a'* &ndash; *'n'* in their filenames &mdash; each of which has a transparent background for one of the buttons, so the `<img>` background color can show through. 

## Code

The generated `<div>` suitable for embedding in a [Google site](https://sites.google.com/) can be found [here](https://raw.githubusercontent.com/dcpetty/ccsae/refs/heads/main/ccsae.html) and is shown below:

```html

<div>
<map name="ccsae-map">
<area shape="rect" coords="280,075,430,125" href="https://sites.google.com/view/coastal-climate-science/explainers/increasing-co2" alt="Increasing CO2 in the atmosphere"
  onmouseover="light('a')" onmouseout="dark()" />
<area shape="rect" coords="410,165,560,215" href="https://sites.google.com/view/coastal-climate-science/explainers/warmer-air" alt="Warmer air and the greenhouse effect"
  onmouseover="light('b')" onmouseout="dark()" />
<area shape="rect" coords="270,265,420,315" href="https://sites.google.com/view/coastal-climate-science/explainers/warmer-ocean" alt="Warmer ocean water"
  onmouseover="light('c')" onmouseout="dark()" />
<area shape="rect" coords="460,270,560,320" href="https://sites.google.com/view/coastal-climate-science/explainers/more-water-vapor" alt="More water vapor in the air"
  onmouseover="light('d')" onmouseout="dark()" />
<area shape="rect" coords="560,270,660,320" href="https://sites.google.com/view/coastal-climate-science/explainers/melting-glaciers" alt="Melting glaciers and ice sheets"
  onmouseover="light('e')" onmouseout="dark()" />
<area shape="rect" coords="095,245,245,295" href="https://sites.google.com/view/coastal-climate-science/explainers/ocean-acidification" alt="Ocean acidification"
  onmouseover="light('f')" onmouseout="dark()" />
<area shape="rect" coords="350,460,500,510" href="https://sites.google.com/view/coastal-climate-science/explainers/sea-level" alt="Rising sea level"
  onmouseover="light('g')" onmouseout="dark()" />
<area shape="rect" coords="545,365,695,415" href="https://sites.google.com/view/coastal-climate-science/explainers/water-salinity" alt="Regional changes in water salinity"
  onmouseover="light('h')" onmouseout="dark()" />
<area shape="rect" coords="500,460,650,510" href="https://sites.google.com/view/coastal-climate-science/explainers/ocean-circulation" alt="Changes to Atlantic Ocean circulation"
  onmouseover="light('i')" onmouseout="dark()" />
<area shape="rect" coords="515,570,665,620" href="https://sites.google.com/view/coastal-climate-science/explainers/extreme-weather" alt="Extreme and changing weather"
  onmouseover="light('j')" onmouseout="dark()" />
<area shape="rect" coords="190,580,310,630" href="https://sites.google.com/view/coastal-climate-science/explainers/less-dissolved-oxygen" alt="Less dissolved oxygen in water"
  onmouseover="light('k')" onmouseout="dark()" />
<area shape="rect" coords="310,580,430,630" href="https://sites.google.com/view/coastal-climate-science/explainers/algal-blooms" alt="Harmful algal blooms (HABs)"
  onmouseover="light('l')" onmouseout="dark()" />
<area shape="rect" coords="250,715,400,765" href="https://sites.google.com/view/coastal-climate-science/explainers/harm-to-marine" alt="Harm to marine life"
  onmouseover="light('m')" onmouseout="dark()" />
<area shape="rect" coords="385,785,535,835" href="https://sites.google.com/view/coastal-climate-science/explainers/harm-to-human" alt="Harm to human and terrestrial life"
  onmouseover="light('n')" onmouseout="dark()" />
</map>
<img id="ccsae" style="display: block; margin: auto; background-color: gold;"
  usemap="#ccsae-map" src="https://dcpetty.dev/ccsae/images/fseicdace-740x850.png" alt="ccsae" />
<script>
const uri = `https://dcpetty.dev/ccsae/images/fseicdace-740x850`, ext = `.png`;
const img = document.querySelector(`img#ccsae`);
console.log(img);
function light(id) { img.src = `${uri}-${id}${ext}`; }
function dark() { img.src = `${uri}${ext}`; }
</script>
</div>
```

<hr>

[&#128279; permalink](https://dcpetty.github.io/ccsae/) and [&#128297; repository](https://github.com/dcpetty/ccsae/) for this page.
