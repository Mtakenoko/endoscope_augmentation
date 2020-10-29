# 眼科用内視鏡の深度画像データセット作成
## Data Augmentation
`/eyemodel_train_raw`に保存したRGB画像と深度画像の生のデータセットから画像のアフィン変換を行ったものを`/eyemodel_train`に保存。
```
python data_augmentation.py
```

## DenseDepth用CSVファイル作成
`/eyemodel_train`と`/eyemodel_test`に登録されたRGB画像と深度画像のデータセットから[DenseDepth](https://github.com/Mtakenoko/DenseDepth)用のcsvファイルを作成する。
```
python make_csv.py
```