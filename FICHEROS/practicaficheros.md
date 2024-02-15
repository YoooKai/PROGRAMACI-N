1. Write a Python program to read an entire text file.

```python
f = open ('fichero.txt', 'r')
f.read()
```

2. Write a Python program to read first n lines of a file.

```python
n = 6
with open('file_path', 'r') as file:
        for i in range(n): #va de 0 a 6-1, es decir, itera 6 veces
            line = file.readline().strip() # saca línea del archivo, y la limpia
            if not line:
                break  # Break si se acaban lines
            print(line) #imprime línea
```

3. Write a Python program to append text to a file and display the text.

```python
with open ('archivo.txt', 'w') as f:
    f.write('Holaa/n')
    f.write('hey heyy/n')
    f.write('Ya paro')

with open ('archivo.txt', 'r') as fmod:
    print(fmod.read())
```

5. Write a Python program to read a file line by line and store it into a list.

```python
listoflines = []

with open('archivo.txt', 'r') as f:
    for line in f:
        listoflines.append(line.strip())  # Agrega cada línea al final de la lista, eliminando los caracteres de nueva línea al final
    print(listoflines)
# or
with open('test.txt') as f:
    # Content_list is the list that contains the read lines.
    content_list = f.readlines()
    print(content_list)

```

6. Write a Python program to read a file line by line store it into a variable. (como string)

```python
with open(file_path, 'r') as file:
    content_variable = ""
    for line in file:
        content_variable += line
```

8. Write a python program to find the longest words.

```python

word_length_dict = {}

with open('archivo.txt', 'r') as f:
    # Separar líneas por espacios y añadir a un diccionario con su longitud
    for line in f:
        words = line.split()
        for word in words:
            word_length_dict[word] = len(word)

# Encontrar la palabra más larga y su longitud
longest_word = max(word_length_dict, key=word_length_dict.get)
max_length = word_length_dict[longest_word]

print("Diccionario de longitudes de palabras:", word_length_dict)
print("Palabra más larga:", longest_word)
print("Longitud de la palabra más larga:", max_length)

#or


filename = 'test.txt'  # Reemplaza con la ruta real de tu archivo

# Abre el archivo en modo lectura
with open(filename, 'r') as infile:
    # Lee el contenido del archivo y divide las palabras
    words = infile.read().split() #el .read devuelve cadena de texto y luego separa

# Encuentra la longitud máxima de las palabras en la lista
max_len = len(max(words, key=len))

# Filtra las palabras que tienen la longitud máxima
result = [word for word in words if len(word) == max_len]

# Imprime la lista de palabras más largas
print(result)


```

9. Write a Python program to count the number of lines in a text file.

```python
total_lines = 0
with open('archivo.txt', 'r') as f:
    for line in f:
        total_lines += 1

#or

filename = 'test.txt'  # Reemplaza con la ruta real de tu archivo

with open(filename) as f:
    for i, l in enumerate(f):
        # No se necesita ninguna acción aquí

num_lines = i + 1
print("Número de líneas en el archivo:", num_lines)
```

10. Write a Python program to count the frequency of words in a file.

```python
# separar por palabras
# añadirlas a diccio
#si ya está, sumar +1
# si no, cuenat = 1

content = {}
with open ('archivo.txt', 'r') as f:
    for line in f:
        words = line.split()
        for word in words:
            clean_word= word.strip().lower
            if clean_word in content:
                content[word] += 1
            else:
                content[word] = 1

#or

```

12. Write a Python program to write a list to a file.


```python
items = [1, 2, 3, 4, 5, 6, 7]

with open ('archivo.txt', 'w') as f:
    for item in items:
        f.write(str(items) + '/n')

```

13. Write a Python program to copy the contents of a file to another file .

```python
with open ('archive.txt', 'r') as f:
    with open ('archive2', 'w') as fw:
        for line in f:
            fw.write(line)
```

14. Write a Python program to combine each line from first file with the corresponding line in second file.

```python
with open('archive.txt', 'r') as file, open('archive2.txt', 'r') as file2, open('output.txt', 'w') as output_file:
    for line1, line2 in zip(file, file2):
        combined_line = f'{line1.strip()} {line2.strip()}\n'
        output_file.write(combined_line)
```

17. Write a Python program to remove newline (/n) characters from a file.

```python
with open('archive.txt', 'r') as file, open('archive2.txt', 'w') as file2:
    for line in file:
        cleaned_line = line.strip('\n')
        file2.write(cleaned_line)

```

18. Write a Python program that takes a text file as input and returns the number of words of a given text file.
    Note: Some words can be separated by a comma with no space.

```python
with open('archive.txt', 'r') as file:
    content = file.read() #devuelve un string
    # Reemplaza las comas con un espacio
    content = content.replace(',', ' ')
    # Divide el contenido en palabras
    words = content.split()
    num_words = len(words)

print("Número de palabras en el archivo:", num_words)

```

19. Write a Python program to extract characters from various text files and puts them into a list.

```python
# Lista de rutas de archivos que se quieren procesar
file_paths = ['file1.txt', 'file2.txt']

# Lista para almacenar los caracteres extraídos
characters_list = []

# Iterar sobre cada archivo en la lista de rutas de archivos
for file_path in file_paths:
    # Abrir el archivo en modo lectura ('r')
    with open(file_path, 'r') as file:
        # Leer el contenido completo del archivo
        content = file.read()

        # Extender la lista de caracteres con cada carácter del contenido
        characters_list.extend(content)

# Imprimir la lista de caracteres extraídos
print("Lista de caracteres extraídos:", characters_list)

```
