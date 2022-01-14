average_rate = 800
#평균 속도 800KB

download_time = 110
#다운로드 하는데 걸린시간이 110초라서 110으로 변수 선언

download_size = average_rate * download_time / 1000
#일단 용량은 평균 속도 * 다운로드 하는데 걸린시간을 해줬습니다.
#KB를 MB로 바꿔야 하기 때문에 나누기 1000 을 해줍니다.

print(download_size)
