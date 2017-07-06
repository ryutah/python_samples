import pandas
from matplotlib import pyplot, rc

open_data = "http://www.city.yokohama.lg.jp/ex/stat/opendata/suikei01/e1yokohama1412.csv"
df = pandas.read_csv(open_data, index_col="市区名")
df.rename(columns={"全国地方公共団体コード": "Code"}, inplace=True)
print(df.head(3))

key_data = ["人口総数[人]", "男[人]", "女[人]"]
pp = df[df.Code != 141003][key_data]
print(pp.head(3))

font = {"family": "Ricty Diminished"}
rc("font", **font)
pyplot.style.use("ggplot")
pp.plot(kind="bar", figsize=(12, 6), y=["男[人]", "女[人]"], fontsize=17)
pyplot.show()

sorted_pp = pp.sort_values(by="人口総数[人]", ascending=False)
sorted_pp.plot(kind="bar", figsize=(12, 6), y="人口総数[人]", fontsize=17)
pyplot.show()
