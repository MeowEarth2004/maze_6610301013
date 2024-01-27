import os

# ฟังชั่นตรวจสอบ Directory ที่ระบุมีอยู่จริงหรือไม่
def rename_files(directory, file_extension='.jpg'):
    if not os.path.exists(directory):
        print(f"Directory '{directory}' ไม่พบ")
        return

    # สร้าง list ของไฟล์ทั้งหมดใน Directory ที่มีนามสกุล file_extension
    files = [f for f in os.listdir(directory) if f.endswith(file_extension)]

    # เรียงลำดับไฟล์ตามชื่อ
    files.sort()

    # ตัวนับเพื่อให้ไฟล์ที่ Rename มีเลขเรียงลำดับ
    count = 1

    # Loop ผ่านไฟล์และ Rename
    for file_name in files:
        # สร้างชื่อใหม่
        new_name = f"{count:03d}{file_extension}"
        
        # สร้าง path ของไฟล์เดิมและไฟล์ใหม่
        old_path = os.path.join(directory, file_name)
        new_path = os.path.join(directory, new_name)

        # Rename ไฟล์
        os.rename(old_path, new_path)

        # นับต่อไป
        count += 1

    print("Rename เสร็จสิ้น")

# เรียกใช้ฟังก์ชัน
rename_files("/path/to/your/directory", ".jpg")