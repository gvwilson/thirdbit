---
title: "Maybe AJAX Can Actually *Solve* a Problem"
date: 2009-06-08
---
Over on the Basie blog, Florian has posted an idea about using AJAX to get around one of the most annoying problems in DrProject: timeouts during lengthy batch creation of projects and/or users.  Basically, his plan is to have the browser send one create request at a time, instead of sending a batch to the server and asking it to do them all at once (which often led to timeouts, since each creation can take about one second, and classes often have a hundred students or more).  It's theoretically less efficient (more network traffic, and N rewrites of the .htaccess file instead of one), but "slower and always works" is better than "faster and sometimes fails". He'd welcome your comments…
