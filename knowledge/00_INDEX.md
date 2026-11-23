# 知識庫索引｜從 Sensor 到 FPGA 的 ROI 資料流程

此資料夾為 5 篇文獻的**中文知識卡與檢索材料**，五篇 PDF 已在本機索引並完成頁碼查核；原始 PDF 與全文索引保存在完整作業的私人資料夾，不公開於 GitHub。這些摘要不是論文原文全文。

| ID | 論文 | 系統層級 | Wiki 卡片 |
|---|---|---|---|
| P1 | VisionMode (ICCV 2017) | Sensor / ISP | [P1](P1_VisionMode.md) |
| P2 | FOVEA (ICCV 2021) | Software resampling | [P2](P2_FOVEA.md) |
| P3 | Rhythmic Pixel Regions (ASPLOS 2021) | Sensor stream → SoC / DRAM | [P3](P3_RPR.md) |
| P4 | TuMag (Electronics 2021) | Sensor → FIFO → ROI / TX | [P4](P4_TuMag.md) |
| P5 | D-SWIM (Journal of Imaging 2019) | FPGA line buffer | [P5](P5_D-SWIM.md) |

## 需要嚴格區分的觀念

- **Pixel sampling 數量**：Sensor 是否實際讀出／ADC 轉換多少像素。
- **模型輸入**：影像取得後經過縮放或 foveated warp 的 tensor 大小。
- **DRAM traffic**：SoC 寫入記憶體的資料量；未必等於感測器傳出的資料量。
- **FPGA FIFO / line buffer**：串流中的暫存與排程成本，和 camera link 傳輸量是不同節點。

## Wiki 品質門檻

回答需附 [P#] 與章節/圖表，缺證據應標示待查核；跨論文數據不可直接混算。
