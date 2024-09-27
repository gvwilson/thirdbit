---
title: "Virtualization vs. Web Services"
date: 2009-01-26
---
I'm at <a href="http://www.caltech.edu">CalTech</a> listening to physicists talk about the software side of the new <a href="http://neutrons.ornl.gov/aboutsns/aboutsns.shtml">Spallation Neutron Source</a> at Oak Ridge.  One of their major headaches is the difficulty of deploying their code: a typical application has dozens of complicated modules, each with dozens or hundreds of dependencies.  Their solution is to host a web service rather than try to deploy on end users' machines, which has got me thinking: are web services and virtualization competing solutions for non-data-intensive applications?  (Non-data-intensive because if your app needs to grind a few terabytes to produce an answer, you're not shipping copies of it around.)  Does anyone know of any studies/comparisons of the tradeoffs between "here's the over-the-web API" and "here the VM"?
