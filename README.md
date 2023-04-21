**node-snowball-italian**

***This module is built as a fork of the original node-snowball to have a lighter italian-only package for a specific use-case***

This stemming module for Node.js provides stemming capability for the italian language using Dr. M.F. Porter's Snowball API.
That allow you to get from a word a reduced, inflected (or sometimes derived) word from the original word stem, base or root.


This library is using bindings to the [libstemmer](http://snowball.tartarus.org/download.html) C library.
It's support

More about Stemming:
- [Stemming wikipedia](http://en.wikipedia.org/wiki/Stemming)
- [Racinisation wikipedia](http://fr.wikipedia.org/wiki/Racinisation)

## Install
```
npm install node-snowball-italian
```

## Usage

```javascript
var snowball = require('node-snowball-italian');

// You can only use italian language with this module
snowball.stemword('richiesta', 'italian'); // 'richiest'

// Or using Array of string
snowball.stemword(['parola', 'libro'], 'italian'); // ['parol', 'libr']
```

## Quick Doc

``` javascript
snowball.stemword(
    word || words, // The word or group of words that you need the stemming from
    language,      // The language (required, the only available is "italian")
    encoding       // The text encoding (optional, default is "UTF-8")
);
```

### Supported language second argument:

 * italian

### Supported encoding third argument:

 * UTF-8
 * ISO-8859-1
 * ISO-8859-2

## To compile, run

Supported NodeJS versions: 10.x, 11.x, 12.x

```
npm build .
npm test
```

## License

(MIT License)

Copyright (c) 2014 Harold Thetiot <hthetiot@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
