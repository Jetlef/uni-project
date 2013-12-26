<pre><span style="color:CornflowerBlue">
 __  __     __   __     __    
/\ \/\ \   /\ "-.\ \   /\ \   
\ \ \_\ \  \ \ \-.  \  \ \ \  
 \ \_____\  \ \_\\"\_\  \ \_\ 
  \/_____/   \/_/ \/_/   \/_/ (DOT PY)</span></pre>

----------

Semi-comprehensive guide - may never be completed! - use at own risk!

(c) 2013-2014 Luca J. Pears, <[lucapiras66@gmail.com][mail]>

_None of the rights reserved._ [![Kopimi logo][kopimi-logo]][kopimi]

[mail]: mailto:lucapiras66@gmail.com
[kopimi-logo]: http://www.kopimi.com/kopimi/copyme1_black_bg.gif
[kopimi]: http://www.kopimi.com/kopimi


_Frustra fit per plura quod potest fieri per pauciora._  
_It is futile to do with more things that which can be done with fewer._ ~Ockham

_I really hope this works._ ~The Author/Developer

----------

# Uni Project -- Table of contents

* I - Introduction
    * I.a - Version log
    * I.b - Credits
* II - Usages
    * II.a - uni.py
* III - Implementation details
    * III.a - libuni.py
    * III.b - Plugins



# I - Introduction

The UNI Project aims to make the world a slightly better place, by creating a collection of scripts to batch encode media files in the highest quality possible.

All the code components of the UNI Project have been designed to be self-documenting, easy to extend, and simple.

Also, everything is licensed under the [WTFPL][] licence.

[wtfpl]: http://www.wtfpl.net/txt/copying/

## I.a - Version log
* Mk. I: _It's tough to simplify._  
  Created this document, documented uni.py.

##

# II.a - uni.py

### Usage
`uni.py <input> <output>` -- convert all `<input>` files found in the current working directory to `<output>`.

### Example
Convert all FLAC files to MP3: `uni.py flac mp3`
