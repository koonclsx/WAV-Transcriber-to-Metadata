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
- 🚫 Does **not** create `.txt` or `.srt` files — modifies WAV files directly

---

## 📦 Installation

1. Install Python 3.8 or later  
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Download the ffmpeg compilation.
Go to the official website with ready-made builds.:
https://www.gyan.dev/ffmpeg/builds/

In the "Release builds" section, download ffmpeg-release-essentials.zip (approximately 60-70 MB)

4. Unpack the archive
Unpack the downloaded file .zip to a convenient folder, for example:
C:\ffmpeg

Inside there will be a folder ffmpeg-xxxx-win64-static — inside it there is a bin folder with a file ffmpeg.exe

5. Add ffmpeg to the system PATH
Open the Start menu, enter "Environment Variables" and select "Change Environment variables for this account" or "Change Environment Variables" (depends on the Windows version)

In the window that opens, click the "Environment Variables" button

In the "User environment variables" block (or system variables, if you want for everyone), find a variable named Path, highlight it and click "Edit"

Click "Create" and enter the full path to the bin folder, for example:

vbnet
Copy
Edit
C:\ffmpeg\ffmpeg-xxxx-win64-static\bin
(replace xxxx with a specific version in the folder name)

Click OK in all windows to save

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

