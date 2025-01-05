# ccsae

Files for generating HTML to go with [*Coastal Climate Science &mdash; Activities and Experiments*]() (CCSAE) [explainers](https://sites.google.com/view/coastal-climate-science/explainers).

## Code

The generated `<div>` suitable for embedding in a [Google site](https://sites.google.com/) can be found [here](https://raw.githubusercontent.com/dcpetty/ccsae/refs/heads/main/ccsae.html) and is rendered below:

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
function light(id) {
  e = document.querySelector(`img#ccsae`);
  e.src = `https://dcpetty.dev/ccsae/images/fseicdace-740x850-${id}.png`;
  // console.log(e);
}
function dark() {
  e = document.querySelector(`img#ccsae`);
  e.src = `https://dcpetty.dev/ccsae/images/fseicdace-740x850.png`;
  // console.log(e);
}
</script>
</div>

<hr>

[&#128279; permalink](https://dcpetty.github.io/ccsae/) and [&#128297; repository](https://github.com/dcpetty/ccsae/) for this page.
