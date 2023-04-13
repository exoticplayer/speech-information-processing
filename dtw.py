
# import numpy
# import librosa
# from basic_operator import *
# import matplotlib


# yes1 = "yes1.wav"
# no2  =  "no2.wav"
# yes3 =  "yes3.wav"
# def mfcc(path):
#     data,fs=librosa.load(path)
#     # print(data)
#     # print(data.shape)
#     # print(fs)
#     step1   =   pre_emphasis(data) 
#     # print(step1)
#     # print(step1.shape)
#     step2   =   framing(step1,fs) 
#     # print(step2)
#     # print(step2.shape)
#     step3   =   add_window(step2,fs)
#     # print(step3)
#     # print(step3.shape)
#     step4   =   stft(step3) 
#     # print(step4)
#     # print(step4.shape)
#     step5   =   mel_filter(step4, fs) 
#     # print(step5)
#     # print(step5.shape)
#     fbank   =   log_pow(step5) 
#     # print(fbank)
#     # print(fbank.shape)
#     mfcc  = discrete_cosine_transform(fbank)
#     # print(mfcc.shape)
#     return mfcc
#     # print(mfcc)
    

# def fbank(path):
#     data,fs=librosa.load(path)
#     # print(data)
#     # print(data.shape)
#     # print(fs)
#     step1   =   pre_emphasis(data) 
#     # print(step1)
#     # print(step1.shape)
#     step2   =   framing(step1,fs) 
#     # print(step2)
#     # print(step2.shape)
#     step3   =   add_window(step2,fs)
#     # print(step3)
#     # print(step3.shape)
#     step4   =   stft(step3) 
#     # print(step4)
#     # print(step4.shape)
#     step5   =   mel_filter(step4, fs) 
#     # print(step5)
#     # print(step5.shape)
#     fbank   =   log_pow(step5) 
#     # print(fbank)
#     # print(fbank.shape)
    
#     return fbank
#     # print(mfcc)
#     # print(mfcc.shape)

# """
# DTWDistance(s1, s2) is copied from:
# http://alexminnaar.com/2014/04/16/Time-Series-Classification-and-Clustering-with-Python.html
# """
 
# def DTWDistance(s1, s2):
#     DTW={}
#     index1=[]
#     index2=[]
#     len1=s1.shape[0]
#     len2=s2.shape[0]
#     dist = np.zeros((len1,len2))
  
#     for i in range(len1):
#         for j in range(len2):
#             dist[i][j]=(sum((s1[i][:]-s2[j][:])*(s1[i][:]-s2[j][:])))

 
#     for i in range(len1):
#         DTW[(i, -1)] = float('inf')
#     for i in range(len2):
#         DTW[(-1, i)] = float('inf')
#     DTW[(-1, -1)] = 0
#     # index1.append(0)
#     # index2.append(0)
#     for i in range(len1):
#         for j in range(len2):
#             DTW[(i,j)]=dist[i][j]+min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])
#     # i,j=len1-1,len2-1
#     # while not(i==0 and j==0):
#     #     index1.append(i)
#     #     index2.append(j)
#     #     if DTW[(i-1,j)]<DTW[(i, j-1)]:
#     #         if DTW[(i-1,j)]<DTW[(i-1, j-1)]:
#     #             index1.append(i-1)
#     #             index2.append(j)
#     #             i-=1
#     #         else:
#     #             index1.append(i-1)
#     #             index2.append(j-1)
#     #             i-=1
#     #             j-=1
#     #     else:
#     #         if DTW[(i,j-1)]<DTW[(i-1, j-1)]:
#     #             index1.append(i)
#     #             index2.append(j-1)
#     #             j-=1
#     #         else:
#     #             index1.append(i-1)
#     #             index2.append(j-1)
#     #             i-=1
#     #             j-=1
#     # index1.append(0)
#     # index2.append(0)



#             #     continue
#             # elif(min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])==DTW[(i, j-1)]):
#             #     continue
#             # else:
                
#             # TODO1
#             # 理解dtw算法，此处写入递推公式
#     index1.reverse()
#     index2.reverse()
 
#     return np.sqrt(DTW[len1-1, len2-1]),index1,index2
 


# # TODO2
# # 导入wav文件，计算mfcc，用mfcc计算两个wav文件的dtw距离
# # 提示：导入文件可以使用 librosa.load('文件路径')

# path1="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/yes1.wav"
# path2="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/no2.wav"
# path3="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/yes3.wav"

# s1=mfcc(path1)
# s2=mfcc(path2)
# s3=mfcc(path3)
# d13,index1,index2=DTWDistance(s1,s3)
# # print(index1)
# # print(len(index1))
# plt.plot(index1,index2)
# plt.show()


# d12,index1,index2=DTWDistance(s1,s2)
# print("d12: %f,d13: %f" %(d12,d13))



# # TODO3
# # 将yes1和yes3两个音频，每一帧之间的对应关系用图表的形式画出来
# # yes1作为x轴，yes3作为y轴
# # 提示：在动态规划算法之中，保存算入最终dtw距离的两帧的索引index1和index2，以index1为x轴，index2为y轴画图

import numpy
import librosa
from basic_operator import *


yes1 = "yes1.wav"
no2  =  "no2.wav"
yes3 =  "yes3.wav"
def mfcc(path):
    data,fs=librosa.load(path)
    # print(data)
    # print(data.shape)
    # print(fs)
    step1   =   pre_emphasis(data) 
    # print(step1)
    # print(step1.shape)
    step2   =   framing(step1,fs) 
    # print(step2)
    # print(step2.shape)
    step3   =   add_window(step2,fs)
    # print(step3)
    # print(step3.shape)
    step4   =   stft(step3) 
    # print(step4)
    # print(step4.shape)
    step5   =   mel_filter(step4, fs) 
    # print(step5)
    # print(step5.shape)
    fbank   =   log_pow(step5) 
    # print(fbank)
    # print(fbank.shape)
    mfcc  = discrete_cosine_transform(fbank)
    return mfcc
    # print(mfcc)
    # print(mfcc.shape)

def fbank(path):
    data,fs=librosa.load(path)
    # print(data)
    # print(data.shape)
    # print(fs)
    step1   =   pre_emphasis(data) 
    # print(step1)
    # print(step1.shape)
    step2   =   framing(step1,fs) 
    # print(step2)
    # print(step2.shape)
    step3   =   add_window(step2,fs)
    # print(step3)
    # print(step3.shape)
    step4   =   stft(step3) 
    # print(step4)
    # print(step4.shape)
    step5   =   mel_filter(step4, fs) 
    # print(step5)
    # print(step5.shape)
    fbank   =   log_pow(step5) 
    # print(fbank)
    # print(fbank.shape)
    
    return fbank
    # print(mfcc)
    # print(mfcc.shape)

"""
DTWDistance(s1, s2) is copied from:
http://alexminnaar.com/2014/04/16/Time-Series-Classification-and-Clustering-with-Python.html
"""
 
def DTWDistance(s1, s2):
    DTW={}
    len1=s1.shape[0]
    len2=s2.shape[0]
    dist = np.zeros((len1,len2))
  
    for i in range(len1):
        for j in range(len2):
            dist[i][j]=(sum((s1[i][:]-s2[j][:])*(s1[i][:]-s2[j][:])))

 
    for i in range(len1):
        DTW[(i, -1)] = float('inf')
    for i in range(len2):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0
 
    for i in range(len1):
        for j in range(len2):
            # TODO1
            # 理解dtw算法，此处写入递推公式
            DTW[(i, j)] = dist[i][j] + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)]) 
 
    return np.sqrt(DTW[len1-1, len2-1])
 


# TODO2
# 导入wav文件，计算mfcc，用mfcc计算两个wav文件的dtw距离
# 提示：导入文件可以使用 librosa.load('文件路径')



# TODO3
# 将yes1和yes3两个音频，每一帧之间的对应关系用图表的形式画出来
# yes1作为x轴，yes3作为y轴
# 提示：在动态规划算法之中，保存算入最终dtw距离的两帧的索引index1和index2，以index1为x轴，index2为y轴画图
path1="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/yes1.wav"
path2="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/no2.wav"
path3="D:/语音信息处理/实验二/dtw-main/dtw-main/dtw/yes3.wav"

s1=mfcc(path1)
s2=mfcc(path2)
s3=mfcc(path3)
d13=DTWDistance(s1,s3)
d12=DTWDistance(s1,s2)
print(d12)
print(d13)