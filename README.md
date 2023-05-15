# Mihari

![](https://onimai.jp/assets/img/character/mihari_face05.png)

## Compile

### Windows

```bash
nuitka --windows-disable-console --standalone --onefile --output-dir=build -o mihari --windows-icon-from-ico="icon.ico" main.py
```

### Linux

```bash
nuitka --disable-console --standalone --onefile --output-dir=build -o mihari --linux-onefile-icon="icon.ico" main.py
```
