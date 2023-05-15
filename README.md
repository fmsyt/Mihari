# Mihari

## Compile

### Windows

```bash
nuitka --windows-disable-console --standalone --onefile --output-dir=build -o mihari --windows-icon-from-ico="icon.ico" main.py
```

### Linux

```bash
nuitka --standalone --onefile --output-dir=build -o mihari --linux-onefile-icon="icon.ico" main.py
```
