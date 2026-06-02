
# PHÂN TÍCH INPUT / OUTPUT:
#
# Input:
# - Người dùng nhập lựa chọn menu: dạng chuỗi string
#   Vì nếu nhập chữ mà ép int ngay thì chương trình dễ bị lỗi.
#
# - Khi thêm sản phẩm:
#   + Mã sản phẩm: string
#   + Tên sản phẩm: string
#   + Số lượng: string nhập từ bàn phím, sau đó kiểm tra rồi ép int
#   + Đơn giá: string nhập từ bàn phím, sau đó kiểm tra rồi ép int
#
# - Khi cập nhật số lượng:
#   + Mã sản phẩm: string
#   + Số lượng mới: int sau khi kiểm tra hợp lệ
#
# - Khi xóa sản phẩm:
#   + Mã sản phẩm: string
#
# Output:
# - Hiển thị danh sách sản phẩm trong giỏ hàng
# - Hiển thị tổng số lượng sản phẩm
# - Hiển thị tổng tiền giỏ hàng
# - Thông báo thêm, cập nhật, xóa thành công
# - Thông báo lỗi nếu dữ liệu không hợp lệ
#
# ĐỀ XUẤT GIẢI PHÁP:
#
# - Dùng nested list để lưu giỏ hàng.
# - Mỗi sản phẩm có dạng:
#   [mã sản phẩm, tên sản phẩm, số lượng, đơn giá]
#
# - Dùng while True để menu chạy liên tục.
# - Dùng for để duyệt từng sản phẩm trong giỏ hàng.
# - Dùng append() để thêm sản phẩm mới.
# - Dùng remove() để xóa sản phẩm khỏi giỏ hàng.
# - Dùng index để truy cập và cập nhật số lượng.
#
# THIẾT KẾ THUẬT TOÁN:
#
# Bước 1: Khởi tạo danh sách cart_items.
# Bước 2: Hiển thị menu trong vòng lặp while.
# Bước 3: Người dùng nhập lựa chọn.
# Bước 4:
#   - Nếu chọn 1: duyệt giỏ hàng, tính tổng số lượng và tổng tiền.
#   - Nếu chọn 2: nhập sản phẩm, kiểm tra dữ liệu, nếu trùng mã thì cộng số lượng, nếu chưa có thì append.
#   - Nếu chọn 3: nhập mã và số lượng mới, kiểm tra rồi cập nhật.
#   - Nếu chọn 4: nhập mã sản phẩm, nếu tìm thấy thì remove.
#   - Nếu chọn 5: thoát chương trình.
#   - Nếu nhập sai: báo lỗi và quay lại menu.


cart_items = [
    ["P001", "Dien thoai iPhone 15", 1, 25000000],
    ["P002", "Op lung Silicon", 2, 150000]
]


while True:
    print("\n===== HỆ THỐNG QUẢN LÝ GIỎ HÀNG SHOPEE =====")
    print("1. Xem chi tiết giỏ hàng và tổng tiền")
    print("2. Thêm sản phẩm mới hoặc tăng số lượng")
    print("3. Cập nhật số lượng sản phẩm")
    print("4. Xóa sản phẩm khỏi giỏ hàng")
    print("5. Thoát chương trình")
    print("============================================")

    choice = input("Nhập lựa chọn của bạn (1-5): ").strip()

    if choice == "1":
        print("\n===== CHI TIẾT GIỎ HÀNG =====")

        if len(cart_items) == 0:
            print("Giỏ hàng hiện đang trống.")
        else:
            total_quantity = 0
            total_price = 0

            print(f"{'STT':<5}{'Mã SP':<10}{'Tên sản phẩm':<30}{'Số lượng':<12}{'Đơn giá':<15}{'Thành tiền'}")
            print("-" * 90)

            for index in range(len(cart_items)):
                product_id = cart_items[index][0]
                product_name = cart_items[index][1]
                quantity = cart_items[index][2]
                price = cart_items[index][3]

                sub_total = quantity * price

                total_quantity += quantity
                total_price += sub_total

                print(f"{index + 1:<5}{product_id:<10}{product_name:<30}{quantity:<12}{price:<15,}{sub_total:,}")

            print("-" * 90)
            print(f"Tổng số lượng sản phẩm: {total_quantity}")
            print(f"Tổng tiền giỏ hàng: {total_price:,} VNĐ")

    elif choice == "2":
        print("\n===== THÊM SẢN PHẨM / TĂNG SỐ LƯỢNG =====")

        product_id_input = input("Nhập mã sản phẩm: ").strip().upper()
        product_name_input = input("Nhập tên sản phẩm: ").strip()

        quantity_input = input("Nhập số lượng: ").strip()
        price_input = input("Nhập đơn giá: ").strip()

        # isdigit() dùng để kiểm tra chuỗi có phải toàn số hay không.
        # Cách này giúp tránh lỗi khi người dùng nhập chữ như abc.
        if quantity_input.isdigit() == False or price_input.isdigit() == False:
            print("[Lỗi] Số lượng và đơn giá phải là số hợp lệ.")
        else:
            quantity = int(quantity_input)
            price = int(price_input)

            # Theo đề: số lượng phải > 0, đơn giá không được âm.
            if quantity <= 0 or price < 0:
                print("[Lỗi] Số lượng phải lớn hơn 0 và đơn giá không được âm.")
            else:
                found = False

                for index in range(len(cart_items)):
                    if cart_items[index][0] == product_id_input:
                        found = True

                        # Nếu mã sản phẩm đã tồn tại thì không tạo dòng mới.
                        # Hệ thống chỉ cộng dồn số lượng.
                        cart_items[index][2] += quantity

                        print("Sản phẩm đã tồn tại, hệ thống đã tăng số lượng.")
                        break

                if found == False:
                    new_product = [product_id_input, product_name_input, quantity, price]
                    cart_items.append(new_product)
                    print("Thêm sản phẩm mới vào giỏ hàng thành công.")

    elif choice == "3":
        print("\n===== CẬP NHẬT SỐ LƯỢNG SẢN PHẨM =====")

        product_id_input = input("Nhập mã sản phẩm cần cập nhật: ").strip().upper()
        quantity_input = input("Nhập số lượng mới: ").strip()

        if quantity_input.isdigit() == False:
            print("[Lỗi] Số lượng phải là số hợp lệ.")
        else:
            new_quantity = int(quantity_input)

            if new_quantity <= 0:
                print("[Lỗi] Số lượng phải lớn hơn 0.")
            else:
                found = False

                for index in range(len(cart_items)):
                    if cart_items[index][0] == product_id_input:
                        found = True

                        # Vị trí [2] là số lượng của sản phẩm.
                        cart_items[index][2] = new_quantity

                        print("Cập nhật số lượng sản phẩm thành công.")
                        break

                if found == False:
                    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "4":
        print("\n===== XÓA SẢN PHẨM KHỎI GIỎ HÀNG =====")

        product_id_input = input("Nhập mã sản phẩm cần xóa: ").strip().upper()

        found = False

        for product in cart_items:
            if product[0] == product_id_input:
                found = True

                # remove() dùng để xóa trực tiếp phần tử khỏi list.
                cart_items.remove(product)

                print("Xóa sản phẩm khỏi giỏ hàng thành công.")
                break

        if found == False:
            print("Mã sản phẩm không tồn tại trong giỏ hàng.")

    elif choice == "5":
        print("Thoát chương trình. Cảm ơn bạn đã sử dụng hệ thống!")
        break

    else:
        print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 5!")
