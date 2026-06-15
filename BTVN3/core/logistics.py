import math


def display_flights(flight_list) -> None:
    """Hiển thị danh sách tất cả chuyến bay với thống kê"""
    print("\n----- DANH SÁCH CHUYẾN BAY & HẬU CẦN -----")

    for index, flight in enumerate(flight_list, start=1):
        water_boxes = math.ceil(flight["passengers"] / 10)
        print(f"{index}. Mã: {flight['flight_id']} | Khởi hành: {flight['depart_time']} | Số khách: {flight['passengers']} | Dự phòng: {water_boxes} thùng nước.")
