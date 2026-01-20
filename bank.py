class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"ฝากเงิน {amount} บาท สำเร็จ")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"ถอนเงิน {amount} บาท สำเร็จ")
            return True
        else:
            print("ยอดเงินไม่พอหรือจำนวนเงินไม่ถูกต้อง")
            return False

    def transfer(self, amount, target_account):
        if self.withdraw(amount):
            target_account.deposit(amount)
            print(f"โอนเงินให้ {target_account.name} สำเร็จ")
        else:
            print("การโอนเงินล้มเหลว")

# ===== โปรแกรมหลัก =====
my_acc = Account("My Account", int(input("กรุณาใส่ยอดเงินเริ่มต้น: ")))
other_acc = Account("Other Account", 500)

while True:
    print(f"\n--- ยอดเงินปัจจุบัน: {my_acc.balance} บาท ---")
    print("1. ฝากเงิน")
    print("2. ถอนเงิน")
    print("3. โอนเงิน (ไปบัญชีอื่น)")
    print("4. ดูยอดเงินทั้งหมด")
    print("5. ออก")

    choice = input("เลือกเมนู (1-5): ")

    if choice == "1":
        amount = int(input("จำนวนเงินที่ต้องฝาก: "))
        my_acc.deposit(amount)

    elif choice == "2":
        amount = int(input("จำนวนเงินที่ถอน: "))
        my_acc.withdraw(amount)

    elif choice == "3":
        amount = int(input("จำนวนเงินที่ต้องการโอน: "))
        my_acc.transfer(amount, other_acc)

    elif choice == "4":
        print(f"บัญชีเรา: {my_acc.balance} | บัญชีปลายทาง: {other_acc.balance}")

    elif choice == "5":
        break
    else:
        print("เลือกเมนูไม่ถูกต้อง")