import streamlit as st

class CurrentAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}.New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawed {amount}.New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account=CurrentAccount()
st.title("ETC BANK")
st.subheader("Cureent Account")

st.sidebar.header("MENU")
chioce= st.sidebar.selectbox("Choose an option",["Deposit","Withdraw","Check Balance"])
if chioce == "Deposit":
    amount= st.sidebar.number_input("Amount")
    if st.button("Deposit"):
        st.write(account.deposit(amount))

elif chioce == "Withdraw":
    amount= st.number_input("Amount")
    if st.button("Withdraw"):
        st.write(account.withdraw(amount))

elif chioce == "Check Balance":
    if st.button("Check Balance"):
        st.write(account.check_balance())
