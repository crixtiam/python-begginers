# Guía Básica de Git

## 1. Configuración Inicial
Antes de empezar a usar Git, es importante configurarlo con tu nombre y correo electrónico:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_email@example.com"
```

## 2. Comandos básicos
Iniciar un repositorio en la carpeta actual
```bash
git init
```
## 3. Clonar un repositorio

Para clonar un repositorio remoto usamos el siguiente comando

```bash
git clone <url-repositorio>
```

## 4. Flujo de trabajo

Ver estado de un repositorio.

```bash
git status
```
## 5. Añadir archivos al área de staging

```bash
git add <archivo>
## anadir todos los archivos
git add .
```

## 6. Hacer un commit
Guarda los cambios en el historial de un repositorio

```bash
git commit -m "Mensaje descriptivo de los cambios"
```

## 7. Ver historial de cambios
```bash
git log
```
---
## 8. Trabajando con ramas 

Crear una nueva rama y cambiar a ella.
```bash
git checkout -b <nombre-rama>
```

Cambiar a una rama existente
```bash
git checkout <nombre-rama>
```

## 9. Fusionar ramas

```bash
git merge <nombre-rama>
```

## 10. Trabajo con repositorios remotos

```bash
git remote add origin <url-del-repositorio-remoto>
```

## 11. Ver repositorios remotos configurados

```bash
git remote -v
```

## 12. Enviar cambios a un repositorio remoto

```bash
git push origin <nombre-rama>
```

## 13. Actualizar repositorio local

```bash
git pull origin <nombre-rama>
```


---

## Creación de cuenta en Github
- https://github.com/

