import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager


file_path = r'c:/Web/6_npsInvestment/data/investment.csv'
file_data = pd.read_csv(file_path, encoding='euc-kr')

data = file_data[['번호','종목명','자산군 내 비중(퍼센트)']]
top_10_data = data.sort_values(by='자산군 내 비중(퍼센트)', ascending=False).head(10)
print(top_10_data)

# 한글 폰트 설정 (Windows에서 기본적으로 제공되는 Malgun Gothic 사용)
font_path = "C:/Windows/Fonts/malgun.ttf"  # 한글 폰트 경로 (Windows)
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.family'] = font_prop.get_name()

# 상위 10개 종목을 원 그래프로 시각화
plt.figure(figsize=(8, 8))
plt.pie(top_10_data['자산군 내 비중(퍼센트)'], labels=top_10_data['종목명'], autopct='%1.1f%%', startangle=90)
plt.title('상위 10개 종목의 자산군 내 비중')
plt.axis('equal')  # 원을 둥글게 만듦
plt.tight_layout()

# 그래프를 이미지로 저장
plt.savefig('top_10_pie_chart.png')
plt.close()