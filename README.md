# ccsae

Files for generating [HTML](./ccsae.html) to go with [*Coastal Climate Science &mdash; Activities and Experiments*](https://sites.google.com/view/coastal-climate-science) (CCSAE) [explainers](https://sites.google.com/view/coastal-climate-science/explainers).

## Version 0.1

The process of developing this `<div>` is as follows:

- Start with an [original image](./images/fseicdace-original.png) with 14 *buttons* and a list of 14 corresponding *URIs* (with their corresponding descriptions).
- After [Photoshop](https://www.adobe.com/products/photoshop.html)ping the [image](./images/fseicdace-740x850.png) to a 740 &#215; 850 format, make a [map](https://drive.google.com/file/d/1FprjDBazKrCQTaQn9zqDLBZvqCTdRRNK/) of coordinates of 14 *rectangles* corresponding to the 14 *buttons*.
- Write a [Python](https://docs.python.org/3/) [script](https://github.com/dcpetty/ccsae/blob/main/src/ccsae.py) to parse / compose the inputs and create the `<img>` [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map) and 14 [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area) elements where the *buttons* link to the *URIs*.

## Version 0.2

As a secondary process:

- Add some [JavaScript](https://typescriptlang.org/) functions for `onmouseover` and `onmouseout` that swap the images in and out for 14 [images](https://github.com/dcpetty/ccsae/tree/main/images) that have the additional letters *'a'* &ndash; *'n'* in their filenames &mdash; each of which has a transparent background for one of the *buttons*, so the `<img>` background color can show through. 

## Version 0.3

In the third version, the files with `740x850` in the filenames seem to have trouble being served to browsers with [AdBlockPlus](https://adblockplus.org/) &mdash; [apparently](https://stackoverflow.com/questions/17255493/how-to-stop-adblock-plus-blocking-images-in-html-page) certain (image) files with image sizes in the filenames are blocked.

*However*, that was not *my* problem&hellip; in my case, using [Arc](https://arc.net/) with [uBlock Origin](https://ublockorigin.com/), I had to whitelist [`sites.google.com`](https://sites.google.com/) to get the embedded `<div>` to load.

*Therefore*, I added back in `*780x850.png` to [`images`](https://github.com/dcpetty/ccsae/tree/main/images) so there are now *two* copies of each `.PNG` file with different filenames.

## Version 0.4

In order to allow for easier adjustments to the diagram, version 0.4 is a [p5.js](https://p5js.org/) sketch available at [https://dcpetty.dev/p5js/ccsae/](https://dcpetty.dev/p5js/ccsae/) (in the [p5js](https://github.com/dcpetty/p5js/) repo) based on this [map](https://drive.google.com/file/d/1FprjDBazKrCQTaQn9zqDLBZvqCTdRRNK/) and this [sheet](https://docs.google.com/spreadsheets/d/1rNqqxYPTbS7i4eP5O07fCUB0CsrdaG4itB4KsOd3UGo/) and editable on this [sketch](https://editor.p5js.org/dcpetty/sketches/x1MXpMMEI).

This is a <span style="font-variant: small-caps;">`Draft`</span>, with more work needed. The original approach using an `<img>` [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map) is still extant.

## Version 0.5

The fifth version of [https://dcpetty.dev/ccsae/ccsae.html](https://dcpetty.dev/ccsae/ccsae.html) using an `<img>` [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map) was updated to include images that reflect the latest from [https://sites.google.com/view/coastal-climate-science/](https://sites.google.com/view/coastal-climate-science/) and that now include *16* explainers.

## Code

The generated `<div>` suitable for embedding in a [Google site](https://sites.google.com/) can be found in raw form [here](https://raw.githubusercontent.com/dcpetty/ccsae/refs/heads/main/ccsae.html) and is shown below:

```html
<!-- https://dcpetty.dev/ccsae/ v0.5 -->
<div>
<map name="ccsae-map">
  <area shape="rect" coords="275,090,455,130" href="https://sites.google.com/view/coastal-climate-science/explainers/increasing-co2" alt="increasing co2 in the atmosphere"
    onmouseover="light('a')" onmouseout="dark()" />
  <area shape="rect" coords="385,195,530,225" href="https://sites.google.com/view/coastal-climate-science/explainers/warmer-air" alt="warmer air and the greenhouse effect"
    onmouseover="light('b')" onmouseout="dark()" />
  <area shape="rect" coords="120,255,220,305" href="https://sites.google.com/view/coastal-climate-science/explainers/ocean-acidification" alt="ocean acidification"
    onmouseover="light('c')" onmouseout="dark()" />
  <area shape="rect" coords="245,280,365,320" href="https://sites.google.com/view/coastal-climate-science/explainers/warmer-ocean" alt="warmer ocean water"
    onmouseover="light('d')" onmouseout="dark()" />
  <area shape="rect" coords="440,275,535,335" href="https://sites.google.com/view/coastal-climate-science/explainers/more-water-vapor" alt="more water vapor in the air"
    onmouseover="light('e')" onmouseout="dark()" />
  <area shape="rect" coords="555,280,675,320" href="https://sites.google.com/view/coastal-climate-science/explainers/melting-glaciers" alt="melting glaciers and ice sheets"
    onmouseover="light('f')" onmouseout="dark()" />
  <area shape="rect" coords="585,375,705,415" href="https://sites.google.com/view/coastal-climate-science/explainers/water-salinity" alt="regional changes in water salinity"
    onmouseover="light('g')" onmouseout="dark()" />
  <area shape="rect" coords="460,435,540,490" href="https://sites.google.com/view/coastal-climate-science/explainers/More-clouds " alt="more clouds and turbulence"
    onmouseover="light('h')" onmouseout="dark()" />
  <area shape="rect" coords="375,475,450,515" href="https://sites.google.com/view/coastal-climate-science/explainers/sea-level" alt="rising sea level"
    onmouseover="light('i')" onmouseout="dark()" />
  <area shape="rect" coords="550,470,650,520" href="https://sites.google.com/view/coastal-climate-science/explainers/water-density" alt="changes in water density"
    onmouseover="light('j')" onmouseout="dark()" />
  <area shape="rect" coords="200,545,265,615" href="https://sites.google.com/view/coastal-climate-science/explainers/less-dissolved-oxygen" alt="less dissolved oxygen in water"
    onmouseover="light('k')" onmouseout="dark()" />
  <area shape="rect" coords="285,560,370,610" href="https://sites.google.com/view/coastal-climate-science/explainers/algal-blooms" alt="harmful algal blooms (habs)"
    onmouseover="light('l')" onmouseout="dark()" />
  <area shape="rect" coords="450,540,575,600" href="https://sites.google.com/view/coastal-climate-science/explainers/extreme-weather" alt="extreme and changing weather"
    onmouseover="light('m')" onmouseout="dark()" />
  <area shape="rect" coords="560,615,660,675" href="https://sites.google.com/view/coastal-climate-science/explainers/ocean-circulation" alt="changes to atlantic ocean circulation"
    onmouseover="light('n')" onmouseout="dark()" />
  <area shape="rect" coords="280,755,380,810" href="https://sites.google.com/view/coastal-climate-science/explainers/harm-to-marine" alt="harm to marine life"
    onmouseover="light('o')" onmouseout="dark()" />
  <area shape="rect" coords="460,785,600,835" href="https://sites.google.com/view/coastal-climate-science/explainers/harm-to-human" alt="harm to human and terrestrial life"
    onmouseover="light('p')" onmouseout="dark()" />
</map>
<img id="ccsae" style="display: block; margin: auto; background-color: gold;"
  usemap="#ccsae-map" src="https://dcpetty.dev/ccsae/images/fseicdace.png" alt="ccsae" />
<script>
  const uri = `https://dcpetty.dev/ccsae/images/fseicdace`, ext = `.png`;
  const img = document.querySelector(`img#ccsae`);
  // console.log(img);
  function light(id) { img.src = `${uri}-${id}${ext}`; }
  function dark() { img.src = `${uri}${ext}`; }
</script>
</div>
```

<hr>

[&#128279; permalink](https://dcpetty.github.io/ccsae/) and [&#128297; repository](https://github.com/dcpetty/ccsae/) for this page.
