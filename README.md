# Image-Compression-
利用將高度以色彩視覺化後的圖片。請設計一個基於Run-Length的壓縮方法，並計算三張圖的平均壓縮率(compression ratio)。 

操作環境：
window10
python 3.6
pycharm
openCV 4.5.2.52
 
程式說明：

>Encoding:
 1. imread()讀取圖片
 2. split()切成rgb通道  
 3. flatten()將rgb轉成1D array
 4. 利用Run-Length編碼
 5. 分別將rgb的list串接起來且前五項存起來
 6.輸出list成img_compress.2036
 
>Decoding:
 1. open()讀取.2036
 2. 將rgb資訊分別存入list
 3. 利用Run-Length的方式解碼
 4. np.array()將list轉成array並改為uint8
 5. reshape()將array轉成(height, width, channel)
 6. merge()將rgb合併成img
 7. imwrite()輸出

測試圖片&結果
![image](https://github.com/wupeeeeei/Image-Compression-/blob/main/%E5%9C%96%E7%89%872.png)
![image](https://github.com/wupeeeeei/Image-Compression-/blob/main/%E5%9C%96%E7%89%873.png)
