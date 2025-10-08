# BOJ 10989 - 수 정렬하기 3 (Counting Sort)

- 문제 링크: [https://www.acmicpc.net/problem/10989](https://www.acmicpc.net/problem/10989)
- 해설: 입력 숫자의 등장 횟수를 카운팅 배열에 누적한 뒤, 1부터 10000까지 순차적으로 출력 횟수만큼 수를 내보내며 정렬을 완성한다. 제한된 값의 범위를 활용하여 O(N + K)의 시간과 O(K)의 추가 공간으로 동작한다.
- 실행 결과:
  ```text
  입력
  5
  3
  2
  1
  2
  3

  출력
  1
  2
  2
  3
  3
  ```
