import cv2
from filters import to_gray, blur, edge, cartoon

def main():
    # Lee Hyewon 폴더 안의 images/sample.jpeg 사용
    img_path = "images/sample.jpeg"
    img = cv2.imread(img_path)

    if img is None:
        print("이미지를 찾을 수 없어요. images/sample.jpeg가 있는지 확인해 주세요.")
        return

    print("=== Simple Image Filter ===")
    print("1: 흑백 필터")
    print("2: 블러 필터")
    print("3: 엣지 필터")
    print("4: 카툰 필터")
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        result = to_gray(img)
        name = "gray"
    elif choice == "2":
        result = blur(img)
        name = "blur"
    elif choice == "3":
        result = edge(img)
        name = "edge"
    elif choice == "4":
        result = cartoon(img)
        name = "cartoon"
    else:
        print("잘못된 선택입니다.")
        return

    out_path = f"images/output_{name}.png"
    cv2.imwrite(out_path, result)
    print(f"필터 적용 완료! 결과 파일: {out_path}")

if __name__ == "__main__":
    main()