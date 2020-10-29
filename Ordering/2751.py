"""
def quickSort(list, start, end):
    if start>=end: #원소가 1개인 경우
        return
    key=start
    i=start+1
    j=end
    #엇갈리기 전까지 반복
    while(i<=j):
        # i index 증가
        while (i<=end and list[i]<=list[key]):
            i+=1
        # j index 감소
        while (j>start and list[j]>=list[key]):
            j-=1
        # i, j 엇갈렸다면
        if (i>j):
            #list[j], list[key] 서로 바꾸기
            list[j], list[key]=list[key], list[j]
        # i, j 엇갈린게 아니면 i랑 j를 교환
        else:
            list[j], list[i]=list[i], list[j]
    #재귀호출 (list 길이가 1일때까지)
    quickSort(list, start, j-1)
    quickSort(list, j+1, end)

"""
def quickSort(list):
    def sort(low, high):
        if low >=high: #원소 1개면
            return
        #pivot index 반환
        mid=partition(low, high)
        #pivot 값 기점으로 작은 요소들 정렬
        sort(low, mid-1)
        #pivot 값 기점으로 큰 요소들 정렬
        sort(mid, high)

    #pivot값의 최종 위치값을 반환하는 함수
    def partition(low, high):
        pivot=list[(low+high)//2]
        while low<=high:
            #pivot보다 low값 작을 때 까지 low index 증가
            while list[low]<pivot:
                low+=1
            # pivot보다 high값 클 때 까지 high index 감소
            while list[high]>pivot:
                high-=1
            #low와 high 엇갈리기 전까지는
            if low<=high:
                #low와 high를 교환
                list[low], list[high]=list[high], list[low]
                # 값 교환 후 index 증감
                low, high=low+1, high-1
        #low와 high 교차된 경우 low위치가 다음 분할의 기준 시작점
        return low

    return sort(0,len(list)-1)



"""
병합정렬
def mergeSort(unsorted_list):
    # 배열 크기가 0이거나 1이면 분할 종료
    if len(unsorted_list) <= 1:
        return unsorted_list
    mid = len(unsorted_list) // 2
    # 두 개의 부분 배열로 나눠서 정렬
    left_sorted_list = mergeSort(unsorted_list[:mid])
    right_sorted_list = mergeSort(unsorted_list[mid:])
    # 하나의 정렬된 배열로 합치기
    return merge(left_sorted_list, right_sorted_list)


def merge(left_sorted_list, right_sorted_list):
    i = 0
    j = 0
    sorted_list = []  # 정렬한 리스트 넣을 새로운 배열

    # 인덱스 i, j가 left, right 배열 길이보다 작을동안 반복
    while (i < len(left_sorted_list) and (j < len(right_sorted_list))):
    # 두 개의 값 비교해서 작은 값을 새로운 배열에 추가
        if (left_sorted_list[i] > right_sorted_list[j]):
            sorted_list.append(right_sorted_list[j])
            j+=1
        else:
            sorted_list.append(left_sorted_list[i])
            i+=1
    # 두 부분 배열 중 하나가 끝나면 나머지 배열 복사해서 새로운 배열에 추가
    while (i < len(left_sorted_list)):
        sorted_list.append(left_sorted_list[i])
        i += 1
    while (j < len(right_sorted_list)):
        sorted_list.append(right_sorted_list[j])
        j += 1
    return sorted_list

n=int(input())
num=[]

for _ in range(n):
    num.append(int(input()))

num=mergeSort(num)

for i in num:
    print(i)

"""