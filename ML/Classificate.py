
Farming = [1, 2, 3]
Mining = [5, 6, 7, 8]
Manufacturing = []
for i in range(10,34):
    Manufacturing.append(i)
Electricity = [35, 36]
Waste = [37, 38, 39]
Construction = [41, 42]
Wholesale = [45, 46, 47]
Transportation = [49, 50, 51, 52]
Accommodation = [55, 56]
Publication = [58, 59, 60, 61, 62, 63]
Finance = [64, 65, 66]
Realestate=[68, 69]
Science=[70, 71, 72, 73]
BusinessFacilities=[74, 75]
PublicAdministration=[84]
Education=[85]
Health=[86, 87]
Sports=[90, 91]
Association=[94, 95, 96]
SelfConsumption=[97, 98]
International=[99]

def Classi(code,sheet,cnt):
    try:
        code = int(code[:2])
        if code in Farming:
            sheet.write(cnt, 2, '농업, 임업 및 어업')
        if code in Mining:
            sheet.write(cnt, 2, '광업')
        if code in Manufacturing:
            sheet.write(cnt, 2, '제조업')
        if code in Electricity:
            sheet.write(cnt, 2, '전기, 가스, 증기 및 수도사업')
        if code in Waste:
            sheet.write(cnt, 2, '하수-폐기물 처리, 원료재생 및 환경 복원업')
        if code in Construction:
            sheet.write(cnt, 2, '건설업')
        if code in Wholesale:
            sheet.write(cnt, 2, '도매 및 소매업')
        if code in Transportation:
            sheet.write(cnt, 2, '운수업')
        if code in Accommodation:
            sheet.write(cnt, 2, '숙박 및 음식점업')
        if code in Publication:
            sheet.write(cnt, 2, '출판, 영상, 방송통신 및 정보서비스업')
        if code in Finance:
            sheet.write(cnt, 2, '금융 및 보험업')
        if code in Realestate:
            sheet.write(cnt, 2, '부동산업 및 임대업')
        if code in Science:
            sheet.write(cnt, 2, '전문, 과학 및 기술 서비스업')
        if code in BusinessFacilities:
            sheet.write(cnt, 2, '사업시설관리 및 사업지원 서비스업')
        if code in PublicAdministration:
            sheet.write(cnt, 2, '공공행정, 국방 및 사회')
        if code in Education:
            sheet.write(cnt, 2, '교육 서비스업')
        if code in Health:
            sheet.write(cnt, 2, '보건업 및 사회복지 서비스업')
        if code in Sports:
            sheet.write(cnt, 2, '예술, 스포츠 및 여가관련 서비스업')
        if code in Association:
            sheet.write(cnt, 2, '협회 및 단체, 수리 및 기타 개인 서비스업')
        if code in SelfConsumption:
            sheet.write(cnt, 2, '가구내 고용활동 및 달리 분류되지 않은 자가소비 생산활동')
        if code in International:
            sheet.write(cnt, 2, '국제 및 외국기관')
    except:
        pass
