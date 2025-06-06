import os
import wave
import whisper
from struct import pack

def transcribe(path, model):
    result = model.transcribe(path)
    return result["text"].strip()

def add_info_chunk(wav_path, transcription):
    with open(wav_path, "rb") as f:
        content = f.read()

    assert content[:4] == b'RIFF' and content[8:12] == b'WAVE', "Не WAV-файл"

    info_chunk = b''
    tag = b'ICMT'
    text = transcription.encode('utf-8') + b'\x00'
    size = len(text) + (len(text) % 2)
    info_chunk += tag + pack('<I', size) + text
    if len(text) % 2:
        info_chunk += b'\x00'

    list_chunk = b'LIST' + pack('<I', len(info_chunk) + 4) + b'INFO' + info_chunk
    new_riff_size = len(content) - 8 + len(list_chunk)
    new_content = b'RIFF' + pack('<I', new_riff_size) + content[8:] + list_chunk

    with open(wav_path, "wb") as f:
        f.write(new_content)

    print(f"✓ Метаданные добавлены в: {os.path.basename(wav_path)}")

def process_file(wav_path, model):
    transcription = transcribe(wav_path, model)
    add_info_chunk(wav_path, transcription)

def list_wav_files_in_dir(directory="."):
    return [f for f in os.listdir(directory) if f.lower().endswith(".wav")]

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*", help="WAV-файлы для обработки (по умолчанию — все в папке)")
    ap.add_argument("-m", "--model", default="base", help="Whisper-модель (по умолчанию: base)")
    args = ap.parse_args()

    model = whisper.load_model(args.model)

    # Если не указано ни одного файла — обработать все .wav
    if not args.files:
        args.files = list_wav_files_in_dir()
        if not args.files:
            print("❌ В этой папке нет .wav файлов.")
            exit(1)
        else:
            print("🔄 Обрабатываю все .wav файлы в текущей папке...")

    for path in args.files:
        if not os.path.isfile(path):
            print(f"⚠ Файл не найден: {path}")
            available = list_wav_files_in_dir()
            if available:
                print("🔍 Доступные .wav-файлы в этой папке:")
                for f in available:
                    print(f"  - {f}")
            continue

        try:
            process_file(path, model)
        except Exception as e:
            print(f"⚠ Ошибка при обработке {path}: {e}")
