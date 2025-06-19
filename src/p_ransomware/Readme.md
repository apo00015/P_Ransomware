# 🛡️ Ransomware Simulation Script

Este script simula el comportamiento de un ransomware con fines educativos. Cifra archivos en un directorio específico utilizando una clave derivada de una contraseña, y posteriormente muestra un mensaje simulando un ataque de ransomware exitoso.

⚠️ **Advertencia**: Este script modifica archivos de manera irreversible (sobrescribiendo su contenido con versiones cifradas). Úsalo únicamente en entornos controlados y con archivos de prueba.

## 📄 Descripción

El script realiza las siguientes acciones:

1. **Genera una clave simétrica** derivada de una contraseña usando SHA-256.
2. **Busca archivos** con extensiones específicas (`.pdf`, `.json`, `.csv`, `.png`, `.txt`) en el directorio `files/`.
3. **Cifra cada archivo** utilizando la biblioteca `cryptography.fernet`.
4. **Sobrescribe los archivos** con sus versiones cifradas.
5. **Muestra un mensaje final** indicando que el "ataque" fue exitoso.

## Creación del archivo ejecutable en el ssitem aoperativo Linux

Para poder crear un ejecutable para un S-O Linux, bastará con levantar los contenedores con los siguientes comandos

```bash
docker build -t ransonware-builder .
docker run --rm -v $(pwd)/output:/output ransonware-builder
```

Este comando creará un ejecutable en la carpeta Output.

## 🧬 Funcionamiento del Script

A continuación se detalla el flujo de ejecución del script:

1. **Inicio (main):**
   - Se define una contraseña fija (`mi_contraseña_segura`).
   - Se genera una clave segura con `generate_key_from_password()` y se crea un objeto `Fernet`.

2. **Obtención de archivos:**
   - Se listan todos los archivos dentro de la carpeta `files/` cuya extensión sea `.pdf`, `.json`, `.csv`, `.png` o `.txt`.

3. **Proceso de cifrado:**
   - Para cada archivo:
     - Se lee el contenido en modo binario.
     - Se cifra usando el objeto `Fernet`.
     - El archivo original se sobrescribe con su versión cifrada.

4. **Mensaje final:**
   - Se intenta mostrar un cuadro de diálogo usando `tkinter`.
   - Si falla (por falta de entorno gráfico), se imprime un mensaje en consola.
   - 