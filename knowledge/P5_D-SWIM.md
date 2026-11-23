# D-SWIM — 論文知識卡 (P5)

**完整題名：** High-Throughput Line Buffer Microarchitecture for Arbitrary Sized Streaming Image Processing  
**作者：** Runbin Shi, Justin S. J. Wong, Hayden K.-H. So  
**出處：** Journal of Imaging 2019, 5(3), 34  
**原始論文 PDF：** https://pdfs.semanticscholar.org/b75b/ad133477ca3079f8a86550acdea62496ead5.pdf  
**論文頁面：** https://www.mdpi.com/2313-433X/5/3/34  
**系統層級：** FPGA line buffer

## 研究問題與結論（依原文整理）
設計可動態程式化的 FPGA line buffer 微架構，使串流影像處理面對運行時不同影像寬度時，可快速改變緩衝設定。

## 實作/技術機制
- 以記憶體交錯與資料對齊支援多像素串流
- 透過更新控制設定處理不同寬度
- 以 FPGA 的 BRAM、時脈與影像吞吐量評估

## 容易混淆的概念與限制
針對的是可變尺寸的串流 line buffer，並非實作 sensor 端 selective readout 或完整的高低解析度影像合成系統。

## 可追溯位置
Abstract；Section 2.2；Methods；Conclusions。請在 Wiki 中以原始 PDF 為優先證據，遇到超出摘要的數字請回到原文對照。

## 適合教新手的問題
- 這篇方法處理的是影像取得、ISP、記憶體編碼、FPGA 重排，還是 line buffer？
- 此方法到底降低哪個環節的資料量？
- 有哪些限制，不能直接推廣到所有智慧相機？

> 本文件為根據原始 PDF 整理的中文知識卡。五篇 PDF 已在本機建置頁級索引，公開網站沒有即時 LLM 推論服務。


## 本次重新上傳 PDF 的核對資訊
- 原始來源：已實際讀取使用者上傳之 P5 PDF。
- 核對頁碼：PDF p.1–2, p.8–13（PDF 檢視器頁碼）。
- 重要辨析：不是 Sensor-level selective readout。
