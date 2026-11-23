# FOVEA — 論文知識卡 (P2)

**完整題名：** FOVEA: Foveated Image Magnification for Autonomous Navigation  
**作者：** Chittesh Thavamani, Mengtian Li, Nicolas Cebron, Deva Ramanan  
**出處：** ICCV 2021  
**原始論文 PDF：** https://openaccess.thecvf.com/content/ICCV2021/papers/Thavamani_FOVEA_Foveated_Image_Magnification_for_Autonomous_Navigation_ICCV_2021_paper.pdf  
**論文頁面：** https://openaccess.thecvf.com/content/ICCV2021/html/Thavamani_FOVEA_Foveated_Image_Magnification_for_Autonomous_Navigation_ICCV_2021_paper.html  
**系統層級：** Software resampling

## 研究問題與結論（依原文整理）
以注意力導向的非均勻影像重取樣，讓有限大小的模型輸入畫布保留重要物件的細節，並將物件框結果映射回原始座標。

## 實作/技術機制
- 使用前一影格偵測或資料先驗產生 saliency
- 透過 spatial transformer 執行非均勻 warping
- 偵測後進行 backward mapping 還原原始空間的 bounding boxes

## 容易混淆的概念與限制
主要是已取得影像後的演算法處理；不能據此聲稱影像感測器在讀取階段已省下相同數量的像素傳輸。

## 可追溯位置
Figure 1、Figure 2；Section 3 Approach。請在 Wiki 中以原始 PDF 為優先證據，遇到超出摘要的數字請回到原文對照。

## 適合教新手的問題
- 這篇方法處理的是影像取得、ISP、記憶體編碼、FPGA 重排，還是 line buffer？
- 此方法到底降低哪個環節的資料量？
- 有哪些限制，不能直接推廣到所有智慧相機？

> 本文件為根據原始 PDF 整理的中文知識卡。五篇 PDF 已在本機建置頁級索引，公開網站沒有即時 LLM 推論服務。


## 本次重新上傳 PDF 的核對資訊
- 原始來源：已實際讀取使用者上傳之 P2 PDF。
- 核對頁碼：PDF p.1–2（PDF 檢視器頁碼）。
- 重要辨析：軟體處理；不證明 Sensor 少讀像素。
