# coding_test

알고리즘/자료구조 문제 풀이용 개인 워크스페이스입니다.  
문제별로 **카테고리 폴더**를 만들고 `{플랫폼}_{문제번호}.cpp` 형식으로 저장합니다.

## 디렉터리 구조 예시
```
coding_test/
├─ README.md                # 이 문서
└─ DAG/
   └─ leetcode_2192.cpp     # LeetCode 2192 (All Ancestors of a Node in a DAG)
```

## 네이밍 & 분류 규칙
- 파일: `leetcode_{문제번호}.cpp` (예: `leetcode_2192.cpp`)
- 폴더: 알고리즘/주제 단위로 생성 (예: `DAG`, `DP`, `Graph`, `Tree` …)

## 로컬 테스트 방법
`LOCAL_TEST` 매크로를 켜서 스몰케이스를 바로 실행합니다.

```bash
# 예시: DAG/leetcode_2192.cpp
cd /Users/mango/workspace/coding_test

g++ -std=c++17 -O2 -DLOCAL_TEST DAG/leetcode_2192.cpp -o run && ./run
```

- 제출 시에는 `-DLOCAL_TEST`를 제거하고 클래스/함수만 업로드합니다.

## 코드 스타일 (라이트 가이드)
- 가능한 한 **필요한 헤더**만 포함 (점진적으로 `<bits/stdc++.h>` 제거)
- 파일 상단에 **문제 링크 / 접근 / 복잡도**를 주석으로 간단히 기재
- 출력은 문제 요구사항에 맞게 **정렬/형식**을 엄수

---
