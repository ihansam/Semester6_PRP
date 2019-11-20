import random, math
import matplotlib.pyplot as plt             

# functions -------------------------------------------------------
def transform(x,lamda):                     # equation(3) Uniform RV를 Exponential RV로 변환하는 함수
    y = -math.log(1-x)/lamda
    return y

def Count_Num_in_Interval(s, e, l):         # list l에서 s이상 e미만인 데이터의 개수를 반환하는 함수
    count = 0
    for i in l:
        if i>=s and i<e:
            count += 1
    return count        

def theorycal_exponential(y, lamda):        # 이론적인 exponential PDF에서 density를 반환하는 함수
    return lamda*(2.718281828**(-lamda*y))          

### main ----------------------------------------------------------
random.seed(int(input("input random seed: ")))
interval = float(input("input interval: ")) # RV를 나눌 간격
trial = 100                                 # 생성할 RV의 개수
exponential_RVs = []

# step 1,2,3: uniform RV 100개를 생성해 exponential RV로 변환한다.
print("- Exponential Random Variable")      
for i in range(0,trial):                    
    u = random.random()                      
    a = transform(u,1)                      # lambda = 1
    exponential_RVs.append(a)
    print('%.6f' %a, end="  ")

# step 4: exponentail RV를 interval 크기의 k개 구간으로 나눈다.
print("\n- Number of Trials")                           
k = int(max(exponential_RVs)/interval)+1    

# step 5,6: k개로 나눈 구간마다 확률을 계산하고, 이를 이론적인 값과 비교한다.
x_axis = []             # 각 구간의 오른쪽 경계값(예를 들어 [0.1, 0.2, ...])
pdf_list = []           # 프로그램 실행을 통해 얻은 각 구간마다의 확률 값
theo_pdf = []           # 이론적으로 계산한 각 구간마다의 확률 값
for i in range(0,k):
    start = (i)*interval
    end = (i+1)*interval
    x_axis.append(end)
    frequency = Count_Num_in_Interval(start, end, exponential_RVs)
    print('[%.2f~%.2f] :%2d     '%(start, end, frequency), end="")
    probability = frequency/trial
    density = probability/interval                                       
    pdf_list.append(density)
    theo_pdf.append(theorycal_exponential(end,1))   # lambda = 1
    
# 그래프를 그려 비교하는 부분
plt.plot(x_axis, pdf_list, label='Experimental')        
plt.plot(x_axis, theo_pdf, label='Theoretical')
plt.legend()
plt.xlabel('Random Variable')
plt.ylabel('Density')
plt.title('Compare Experimental Results and Theoretical PDF')
plt.show()

# 실험 결과와 이론 값의 오차의 표준편차를 구하는 부분
"""
deviation2= [(pdf_list[i]-theo_pdf[i])**2 for i in range(0, len(x_axis))]
print("\n표준편차: ", (sum(deviation2)/len(deviation2))**0.5)
"""