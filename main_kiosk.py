######################################
## CNU 버거 키오스크 프로그램
## 일지 : 2021.10.12
## 작성자 : 김민주
## 내용 : Console 기반의 햄버거를 판매하는 키오스크 프로그램

# 조건
# 사용자는 최대로 버거1개, 사이드 1개, 음료 1개만 주문할 수 있습니다.


#메뉴와 가격표
import choice_menu as cm
burger_name = {1 : '치즈버거',2 : '불고기버거',3 : '불고기버거'}
side_name = {1 : '프렌치프라이',2 : '치킨너겟'}
drink_name = {1 : '코카콜라',2 : '커피',3 : '주스'}

burger_price = {1 : 3500, 2 : 3000, 3 : 2500}
side_price = {1 : 1500, 2 : 2000}
drink_price = {1 : 1000, 2 : 1200, 3 : 1500}

while 1:

    # 고객 주문 기록 저장
    menu_save = {} # 고객 주문 메뉴 기록
    price_save = {} # 고객 주문 금엑 기록


    #######################
    # >> View단 : 메뉴 선택 #
    #######################

    menu_num = cm.choice_menu()

    ###########################
    # >> View단 : 세부메뉴 선택 #
    ###########################


    if menu_num == 1:       # 햄버거 세트
        choice_num = cm.choice_burger()
        menu_save['burger'] = burger_name[choice_num]
        price_save['burger'] = burger_price[choice_num]
        choice_num2 = cm.choice_side()
        menu_save['side'] = side_name[choice_num2]
        price_save['side'] = side_price[choice_num2]
        choice_num3 = cm.choice_drink()
        menu_save['drink'] = drink_name[choice_num3]
        price_save['drink'] = drink_price[choice_num3]


    elif menu_num == 2:     # 햄버거 단품
        choice_num = cm.choice_burger()
        menu_save['burger'] = burger_name[choice_num]
        price_save['burger'] = burger_price[choice_num]

    elif menu_num == 3:     # 사이드 메뉴
        choice_num2 = cm.choice_side()
        menu_save['side'] = side_name[choice_num2]
        price_save['side'] = side_price[choice_num2]

    elif menu_num == 4:     # 음료
        choice_num3 = cm.choice_drink()
        menu_save['drink'] = drink_name[choice_num3]
        price_save['drink'] = drink_price[choice_num3]


    ############################
    # 주문 메뉴, 금액 정산 및 출력 #
    ############################

    # Total 주문 금액 계산
    total_price = 0

    for price in price_save.values():
        total_price += price

    print('=========================================')
    print('         [고객님이 주문하신 메뉴는]          ')
    for i, menu in enumerate(menu_save.values()):
        print('-> {}. {}'.format(i+1, menu))
    print('으로 총 주문 금액은 [{}]원 입니다.'.format(total_price))
    print('=========================================')
    print('이용해주셔서 감사합니다. 또 방문해 주세요 :)')
    print('=========================================')
