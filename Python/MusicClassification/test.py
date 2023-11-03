import librosa

# 读取音频文件
audio_path = "path_to_audio_file.wav"
waveform, sample_rate = librosa.load(audio_path)

# 提取音频特征
features = librosa.feature.mfcc(waveform, sr=sample_rate)

# 将特征存储在列表中
feature_list = features.tolist()

# 打印特征列表
print(feature_list)