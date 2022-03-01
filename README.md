# Sample Data Generator

## 相關資訊

- 開發時間：03/01/2022
- 開發語言：Python3

## 使用教學

### 生成測資

以下兩種方式皆可正常運作

- 直接打開 `main.py` ，並 run 或 debug ，測資就會自動生成
- 打開終端機並 navigate 到此工作目錄，輸入指令 `main.py` (Windows); `./main.py` (MacOS)

### 設定檔

可以在工作目錄找到 `config.json` 檔案，裡面包含個自訂選項。

以下將對每個選項做細部說明。

```
{
    "output_folder_path": 檔案輸出資料夾之相對檔案位置,
    "delimiter": 單行數字間之間隔符號,
    "delimiters": 若下一個選項
    設定為 true ，則這裡可以放置多種間隔符號，生成測資時，每個間隔符號將從此處隨機選取一個,
    "multiple_delimiters": 是否有多種間隔符號,
    "number_cnt_per_line": 每行測資數字個數,
    "line_cnt": 測資行數,
    "upper_bound": 數字上界,
    "lower_bound": 數字下界,
    "number_type": 數字種類（0：整數；1：浮點數）,
    "number_step": 數字間隔,
    "decimal_cnt": 小數點後顯示至幾位
}
```