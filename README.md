htmler
======

Write HTML in simple way using pure Python


Usage
=====

```
>>> from htmler.fun import div, img, br
>>> print div(div(br(), img(alt="alt text", src="image.png")))
<div><div><br>
<img src="image.png" alt="alt text">
</div>
</div>
```

Installation
============

```
pip install -e "git+https://github.com/andrewboltachev/htmler.git#egg=htmler"
```
