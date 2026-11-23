# TuMag — 論文知識卡 (P4)

**完整題名：** FPGA Implementation of Image Ordering and Packing Algorithm for TuMag Camera  
**作者：** TuMag Camera research team  
**出處：** Electronics 2021, 10(14), 1706  
**原始論文 PDF：** https://riull.ull.es/xmlui/bitstream/handle/915/38782/FPGA_implementation_of_image_ordering_and_packing_algorithm_for_TuMag_camera.pdf?isAllowed=y&sequence=1  
**論文頁面：** https://www.mdpi.com/2079-9292/10/14/1706  
**系統層級：** FPGA reorder / crop / pack

## 研究問題與結論（依原文整理）
GSENSE400 相機資料由 8 通道輸出；FPGA 使用 FIFO 重新排列多通道資料，封包化後再輸出，並可裁切部分欄位 ROI 以減少往 DPU 送出的資料。

## 實作/技術機制
- Sensor 具備列方向 ROI 設定，欄方向裁切有限制
- swapping module 用 even / odd FIFO 與多工器重排
- image_tx 再依欄位 ROI 設定裁切，packer 適配 CoaXPress 輸出

## 容易混淆的概念與限制
由於部分裁切發生在 FPGA 重排之後，減少最終傳輸資料不必然等於前級 FIFO 寫入流量也等比例減少；文中不是任意多個不規則 ROI 的 foveated sensor。

## 可追溯位置
Section 2、4.1、4.2；Figures 8–11；Section 4.3。請在 Wiki 中以原始 PDF 為優先證據，遇到超出摘要的數字請回到原文對照。

## 適合教新手的問題
- 這篇方法處理的是影像取得、ISP、記憶體編碼、FPGA 重排，還是 line buffer？
- 此方法到底降低哪個環節的資料量？
- 有哪些限制，不能直接推廣到所有智慧相機？

> 本文件為根據原始 PDF 整理的中文知識卡。五篇 PDF 已在本機建置頁級索引，公開網站沒有即時 LLM 推論服務。


## 本次重新上傳 PDF 的核對資訊
- 原始來源：已實際讀取使用者上傳之 P4 PDF。
- 核對頁碼：PDF p.3, p.8–10, p.12–13（PDF 檢視器頁碼）。
- 重要辨析：輸出減少不等於重排 FIFO 前減少。
