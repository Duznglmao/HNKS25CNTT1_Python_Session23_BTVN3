Tại sao không nên dùng from math import *?

Làm ô nhiễm namespace vì toàn bộ hàm trong thư viện math được đưa vào phạm vi hiện tại.
Dễ xảy ra xung đột tên hàm hoặc biến.
Khó đọc code vì không biết hàm đang dùng đến từ đâu.
Khó bảo trì khi dự án lớn.

Nên sử dụng:
import math hoặc from math import ceil

BTVN3/
│
├── main.py
│
├── core/
│ ├── __init__.py
│ ├── logistics.py
│ └── manager.py
│
├── utils/
│ ├── __init__.py
│ ├── time_helper.py
│ └── file_helper.py
│
└── data/
├── __init__.py
└── flights_data.py
