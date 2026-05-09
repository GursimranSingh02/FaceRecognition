# Prerequisites for Windows

Before running the project, install the required C++ build tools and CMake.

## Install Visual Studio Build Tools

1. Download [Visual Studio Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/?utm_source=chatgpt.com)

2. Run the installer.

3. Select:

* **Desktop development with C++**

4. Ensure the following components are checked:

* MSVC C++ Build Tools
* Windows 10/11 SDK
* C++ CMake tools for Windows
* C++ Build Tools core features

---

## Verify Installation

Open Command Prompt and run:

### Verify MSVC Compiler

```bash id="srpj7i"
cl
```

You should see Microsoft C/C++ compiler information.

### Verify CMake

```bash id="4s3vwf"
cmake --version
```

You should see the installed CMake version.

---

## Why This Is Required

The project uses libraries such as `insightface` that require native C++ compilation during installation.

Without these tools, installation may fail with errors like:

```text id="ysjxyv"
fatal error C1083: Cannot open include file: 'stdio.h'
```

or

```text id="o6r4po"
Failed building wheel for insightface
```


## Running Qdrant Using Docker
```bash
docker run -p 6333:6333 -p 6334:6334 -v ${PWD}/qdrant_storage:/qdrant/storage qdrant/qdrant
```


## Run the server
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080


uvicorn app.main:app --reload

```
