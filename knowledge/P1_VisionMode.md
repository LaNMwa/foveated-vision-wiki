# VisionMode — 論文知識卡 (P1)

**完整題名：** Reconfiguring the Imaging Pipeline for Computer Vision  
**作者：** Mark Buckler, Suren Jayasuriya, Adrian Sampson  
**出處：** ICCV 2017  
**原始論文 PDF：** https://openaccess.thecvf.com/content_ICCV_2017/papers/Buckler_Reconfiguring_the_Imaging_ICCV_2017_paper.pdf  
**論文頁面：** https://openaccess.thecvf.com/content_iccv_2017/html/Buckler_Reconfiguring_the_Imaging_ICCV_2017_paper.html  
**系統層級：** Sensor / ISP

## 研究問題與結論（依原文整理）
提出可切換的 photography mode 與低功耗 vision mode；可透過較低解析度、較低量化精度與略過 ISP 階段降低影像管線能耗。

## 實作/技術機制
- 可調精度 ADC 與 pixel subsampling
- 提出 power-gated selective readout
- 實驗以可逆感測/ISP 模擬評估不同設定對電腦視覺任務的影響

## 容易混淆的概念與限制
文中節能數據來自論文提出的系統設計與模擬評估，不等於任何市售相機都能直接達到；也不等於任意形狀 ROI 混合解析度已由其硬體完整實現。

## 可追溯位置
Abstract；Section 1 Introduction；Contributions。請在 Wiki 中以原始 PDF 為優先證據，遇到超出摘要的數字請回到原文對照。

## 適合教新手的問題
- 這篇方法處理的是影像取得、ISP、記憶體編碼、FPGA 重排，還是 line buffer？
- 此方法到底降低哪個環節的資料量？
- 有哪些限制，不能直接推廣到所有智慧相機？

> 本文件為根據原始 PDF 整理的中文知識卡。五篇 PDF 已在本機建置頁級索引，公開網站沒有即時 LLM 推論服務。


## 本次重新上傳 PDF 的核對資訊
- 原始來源：已實際讀取使用者上傳之 P1 PDF。
- 核對頁碼：PDF p.1（PDF 檢視器頁碼）。
- 重要辨析：感測端與 ISP 設計層級。
