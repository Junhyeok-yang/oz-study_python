#삼성화재 실비보험 공제금액 계산기 (이건 내 실비보험용)

def reimbursable_input():
    value = input("급여 금액을 입력하세요.")
    return int(value)

def non_reimbursable_input():
    value = input("비급여 금액을 입력하세요.")
    return int(value)

def reimbursable(reimbursable_money):
    apply_deduction = reimbursable_money * 0.1
    if apply_deduction > 10000:
        return apply_deduction
    else:
        return 10000
    
def non_reimbursable(non_reimbursable_money):
    apply_deduction = non_reimbursable_money * 0.2
    if apply_deduction > 10000:
        return apply_deduction
    else:
        return 10000
    
def total_deduction(reimbursable_money, non_reimbursable_money):
    return non_reimbursable(non_reimbursable_money) + reimbursable(reimbursable_money)