from data.flights_data import flights
from core.logistics import display_flights
from core.manager import add_flight
from utils.time_helper import calculate_eta
from utils.file_helper import create_log_folder


def display_menu() -> None:
    """Menu chính"""
    print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
    print("1. Hiển thị lịch trình và Thống kê hậu cần")
    print("2. Tiếp nhận chuyến bay mới")
    print("3. Tính thời gian hạ cánh dự kiến (ETA)")
    print("4. Khởi tạo thư mục lưu trữ log hệ thống")
    print("5. Thoát chương trình")
    print("=" * 50)


def main() -> None:
    """Hiển thị menu và xử lý lựa chọn người dùng với bẫy lỗi"""
    while True:
        display_menu()

        try:
            choice = int(input("Nhập lựa chọn của bạn: "))

            if choice == 1:
                display_flights(flights)
            elif choice == 2:
                add_flight(flights)
            elif choice == 3:
                calculate_eta(flights)
            elif choice == 4:
                create_log_folder()
            elif choice == 5:
                print("Cảm ơn kỹ sư đã sử dụng hệ thống!")
                break
            else:
                print("Vui lòng nhập từ 1 đến 5.")

        except ValueError:
            print("Vui lòng nhập từ 1 đến 5.")


if __name__ == "__main__":
    main()
