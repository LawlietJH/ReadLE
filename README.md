# ReadLE
 Lector de archivos RLE (para "El Juego de la Vida" de John Conway)

### Ejemplos:

Podemos leer directamente un patrón.

Código:
```py
rle = '''
    2o$bo$bobo13b3o$2b2o3bo8bo3bo$6bob2o6bo4bo$5bo4bo6b2obo$
    6bo3bo8bo3b2o$7b3o13bobo$25bo$25b2o!
'''
pattern = getPattern(rle)
prettyPat(pattern)            # Pattern: 36p22
```

También es posible leer directamente un archivo .rle
```py
rle2 = readRLE('patterns/36p22.rle')
pattern = getPattern(rle2)
prettyPat(pattern)
```

Resultado:
```py
0: [■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  -5
1:  · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  -4
2:  · [■] · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■][■] ·  ·  ·  ·  ·  ·  ·  -3
3:  ·  · [■][■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  -2
4:  ·  ·  ·  ·  ·  · [■] · [■][■] ·  ·  ·  ·  ·  · [■] ·  ·  ·  · [■] ·  ·  ·  ·  ·  -1
5:  ·  ·  ·  ·  · [■] ·  ·  ·  · [■] ·  ·  +  ·  ·  · [■][■] · [■] ·  ·  ·  ·  ·  ·   0
6:  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■][■] ·  ·  +1
7:  ·  ·  ·  ·  ·  ·  · [■][■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] · [■] ·  +2
8:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] ·  +3
9:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■] +4
   -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0  +1 +2 +3 +4 +5 +6 +7 +8 +9+10+11+12+13

x = 27, y = 10
```

Se puede obtener de forma limpia el patrón:

Código:
```py
rle2 = readRLE('patterns/36p22.rle')
pattern = getPattern(rle2)
prettyPat(pattern, clean=True)
```

Resultado:
```py
[■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · 
 · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · 
 · [■] · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■][■] ·  ·  ·  ·  ·  ·  · 
 ·  · [■][■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  ·  ·  · 
 ·  ·  ·  ·  ·  · [■] · [■][■] ·  ·  ·  ·  ·  · [■] ·  ·  ·  · [■] ·  ·  ·  ·  · 
 ·  ·  ·  ·  · [■] ·  ·  ·  · [■] ·  ·  +  ·  ·  · [■][■] · [■] ·  ·  ·  ·  ·  · 
 ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■][■] ·  · 
 ·  ·  ·  ·  ·  ·  · [■][■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] · [■] · 
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] · 
 ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■]

x = 27, y = 10
```

También es posible obtener la matriz de valores:

Código:
```py
rle2 = readRLE('patterns/36p22.rle')
pattern = getPattern(rle2)

for p in pattern:
    print(p)

xy = getXY(rle['rle'])

print(f'\n x = {xy[0]}, y = {xy[1]}')
```

Resultado:
```py
[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
[0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

 x = 27, y = 10
```

### Info:

[Run Length Encoded](https://www.conwaylife.com/wiki/Run_Length_Encoded)

El formato de archivo Run Length Encoded (o RLE para abreviar) se usa comúnmente
para almacenar patrones grandes. Es más críptico que algunos otros formatos de archivo
como texto plano y Life 1.06, pero sigue siendo bastante legible. Muchas características
del formato de archivo RLE están incorporadas en el formato de archivo MCell.
Los archivos RLE se guardan con una extensión de archivo .rle.

#### Descripción de formato

La primera línea es una línea de encabezado, que tiene la forma
```py
x = m, y = n
```
donde m y n son el ancho y el alto del patrón, respectivamente.
El patrón en sí comienza en la siguiente línea y está codificado como una secuencia
de elementos de la forma ```<run_count><tag>```, donde ```<run_count>``` es el número
de apariciones de ```<tag>``` y ```<tag>``` es uno de los siguientes tres caracteres

```py
<tag>  descripción
  b     dead cell
  o     alive cell
  $     end of line
  !     end
```

Ejemplos

 El siguiente es un planeador (glider) en formato RLE:
```py
#C This is a glider.
x = 3, y = 3
bo$2bo$3o!
```
 
Cómo leerlo:
```py
RLE: bo$2bo$3o! --> bo$, 2bo$, 3o!

bo$  -->  [b, o]    $  --> break ($)
2bo$ -->  [b, b, o] $  --> break ($)
3o!  -->  [o, o, o] !  --> End (!)
```

Visual: ```x = 3, y = 3```
```py
1  ·  ■  ·
2  ·  ·  ■
3  ■  ■  ■
   1  2  3
```

El siguiente es el cañón planeador Gosper (Gosper glider gun) en formato RLE:
```py
#N Gosper glider gun
#C This was the first gun discovered.
#C As its name suggests, it was discovered by Bill Gosper.
x = 36, y = 9, rule = B3/S23
24bo$22bobo$12b2o6b2o12b2o$11bo3bo4b2o12b2o$2o8bo5bo3b2o$
2o8bo3bob2o4bobo$10bo5bo7bo$11bo3bo$12b2o!
```

Figura:
```py
0:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  -4
1:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  -3
2:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■] ·  ·  ·  ·  ·  · [■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■] -2
3:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  · [■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■] -1
4: [■][■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  ·  ·  · [■] ·  +  · [■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·   0
5: [■][■] ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] · [■][■] ·  ·  ·  · [■] · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  +1
6:  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  ·  ·  · [■] ·  ·  ·  ·  ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  +2
7:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■] ·  ·  · [■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  +3
8:  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  · [■][■] ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  ·  +4
   -18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1 0  +1 +2 +3 +4 +5 +6 +7 +8 +9+10+11+12+13+14+15+16+17

 x = 36, y = 9
```
