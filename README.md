# Sample Data Generator

## 相關資訊

- 開發時間：03/01/2022
- 開發語言：Python3

## 使用教學

### 生成測資

以下兩種方式皆可正常運作

- 直接打開 `main.py` ，並 run 或 debug
- 打開終端機並 navigate 到此工作目錄，輸入指令 `main.py` (Windows); `./main.py` (MacOS)

以上兩種方法之一正確執行後，測資會自動依據設定檔內的各項設定，生成符合要求的測資在設定好的輸出資料夾（預設為工作目錄中的 `ouputs` 資料夾），檔名為測資生成之時間。

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

#### 設定檔範例一

##### 設定檔
```
{
    "output_folder_path": "outputs",
    "delimiter": ", ",
    "delimiters": [
        "+",
        "-",
        "*",
        "/"
    ],
    "multiple_delimiters": true,
    "number_cnt_per_line": 3,
    "line_cnt": 10,
    "upper_bound": 100,
    "lower_bound": -100,
    "number_type": 1,
    "number_step": 0.01,
    "decimal_cnt": 2
}
```
##### 生成測資

```
-19.57+53.63+-46.22
-10.61/-94.05/-86.14
87.82+35.49+55.21
58.40/-73.80/16.24
17.99/-69.05/-30.67
-98.53*-65.08*97.63
-63.56*-19.52*73.07
-26.73+-95.83+13.40
3.93*-46.31*-31.38
14.79*96.33*58.89

```

#### 設定檔範例二

##### 設定檔

```
{
    "output_folder_path": "outputs",
    "delimiter": "+",
    "delimiters": [
        "+",
        "-",
        "*",
        "/"
    ],
    "multiple_delimiters": false,
    "number_cnt_per_line": 3,
    "line_cnt": 10,
    "upper_bound": 100,
    "lower_bound": -100,
    "number_type": 1,
    "number_step": 0.01,
    "decimal_cnt": 2
}
```

##### 生成測資

```
20.07+37.26+30.00
91.77+76.75+-73.42
41.57+-58.44+-99.88
15.21+1.84+46.30
-86.92+8.49+0.84
-59.46+19.87+5.47
40.26+11.21+0.75
48.87+52.20+15.65
13.93+-97.77+-4.49
14.55+22.88+-94.75

```