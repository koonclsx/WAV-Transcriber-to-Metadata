# 🎙️ WAV Transcriber to Metadata

### Language

[![RU](https://img.shields.io/badge/lang-ru-red)](https://github.com/koonclsx/WAV-Transcriber-to-Metadata/blob/main/README.md)
[![EN](https://img.shields.io/badge/lang-en-green)](https://github.com/koonclsx/WAV-Transcriber-to-Metadata/blob/main/README.en.md)

This script automatically recognizes speech in `.wav` files and embeds the transcription into the **metadata (Comment field)** of the audio file.

---

## 🛠 Features

- ✅ Processes all `.wav` files in the folder
- ✅ Speech recognition using [Whisper](https://github.com/openai/whisper)
- ✅ Transcription is stored in the **`Comment` (ICMT)** metadata field
- ✅ **Visible in Windows Explorer** (if the “Comments” column is enabled)
- ✅ Progress indicator
- 🚫 Does **not** create `.txt` or `.srt` files — modifies WAV files directly

---

## 📦 Installation

1. Install Python 3.8 or later  
2. Install dependencies:

```bash
pip install -r requirements.txt
```

> ⚙️ If `ffmpeg` is not installed — the script will attempt to download and configure it automatically.

---

## ▶️ Usage

1. Place your `.wav` files in the same folder as the script  
2. Run the script:

```bash
python wav_transcribe_to_metadata.py
```

---

## 🧾 How to view the result

### 📁 In Windows Explorer:

1. Open the folder with your files  
2. Right-click the column header → “More...”  
3. Enable **“Comments”** — a column will appear showing the transcription text

### 📊 Using ffmpeg:

```bash
ffmpeg -i yourfile.wav
```

---

## 🌍 How to change recognition language

By default, Whisper automatically detects the spoken language.  
To manually set it:

1. Find this line in the code:

```python
result = model.transcribe(str(wav_path))
```

2. Replace it with, for example, for Russian:

```python
result = model.transcribe(str(wav_path), language="ru")
```

Or for English:

```python
result = model.transcribe(str(wav_path), language="en")
```

---

## 📄 requirements.txt

```txt
openai-whisper
ffmpeg-python
tqdm
```

---

## 📌 Notes

- Whisper uses PyTorch — ensure your system is compatible  
- On CPU, transcription may take ~1–5 minutes per file  
- Windows Explorer might not refresh the comment field immediately — press F5 to update

---

## 📜 License

MIT — free to use and modify.

