import os


def create_log_folder() -> None:
    """Tạo thư mục lưu trữ log hệ thống"""
    print("\n----- KHỞI TẠO THƯ MỤC HỆ THỐNG -----")

    folder_name = "aviation_logs"

    if not os.path.exists(folder_name):
        print("[SYSTEM] Thư mục 'aviation_logs' chưa tồn tại.")
        print("[SYSTEM] Đang tiến hành khởi tạo...")
        os.mkdir(folder_name)
        print("[SYSTEM] Tạo thư mục thành công!")
    else:
        print("Thư mục đã tồn tại, bỏ qua bước khởi tạo.")
