from pathlib import Path
import json
path = Path('sutudents.json')
students = {}
try:
    content = json.loads(path.read_text(encoding='utf-8'))
    students = content if content else {}
except FileNotFoundError:
    students = {}
menus = '''
    <=====学生成绩管理=====>
        1.查询        2添加
        3.删除        4修改
               5.退出
    '''
print(menus)
while True:
    opt = int(input('输入序号：'))
    if opt == 1 or 2 or 3 or 4 or 5:
        if opt == 1:
            while True:
                try:
                    number = int(input('输入"1"查询个人\输入"2"查询全部\输入"3"退出：'))
                    if number == 1:
                        while True:
                            name = input('被查询人名字\输入"no"退出：')
                            if name == 'no':
                                break
                            elif name not in students:
                                print(f'未查找到{name}')
                            elif name in students:
                                print(students[name])
                    elif number == 2:
                        print(students)
                    elif number == 3:
                        break
                    else:
                        print('请输入正确序号！！！')
                except ValueError:
                    print('请输入正确数字！！！')
        elif opt == 2:
            while True:
                name = input('请输入添加人名字\输入"no"退出：')
                if name == 'no':
                    break
                else:
                    try:
                        english = float(input('英语成绩：'))
                        math = float(input('数学成绩：'))
                        chinese = float(input('语文成绩：'))
                        physics = float(input('物理成绩：'))
                        chemistry = float(input('化学成绩：'))
                        biology = float(input('生物成绩：'))
                        geography = float(input('地理成绩：'))
                        history = float(input('历史成绩：'))
                        politics = float(input('政治成绩：'))
                        p_e = float(input('体育成绩：'))
                        average_score = (english + math + chinese + physics + chemistry + biology + geography + history + politics + p_e)/10
                        main_subject = [english,math,chinese]
                        minor_subject = [physics,chemistry,biology,geography,history,politics]
                        grade = 0
                        for score in main_subject:
                            if score >= 90:
                                grade = grade + 1
                        for score in minor_subject:
                            if score >= 60:
                                grade = grade + 1
                        if p_e >= 30:
                            grade = grade + 1
                        a = grade/10*100
                        rate = f"{a}%"
                        school_report = {'语文':chinese,'数学':math,'英语':english,'物理':physics,'化学':chemistry,'生物':biology,'地理':geography,'历史':history,'政治':politics,'体育':p_e,'平均分':average_score,'及格率':rate}
                        students[name] = school_report
                        path.write_text(json.dumps(students,ensure_ascii=False,indent=2) + '\n',encoding='utf-8')
                    except ValueError:
                        print('请输入数字！！！')
        elif opt == 3:
            while True:
                name = input('输入被删除人名字\输入"no"退出：')
                if name == 'no':
                    break
                elif name in students:
                    del students[name]
                    print(f'己删除{name}')
                    path.write_text(json.dumps(students,ensure_ascii=False,indent=2) + '\n' ,encoding='utf-8')
                else:
                    print('查无此人！！！')
        elif opt == 4:
            while True:
                name = input('输入被修改人名\输入"no"退出：')
                if name in students:
                    school_report = students[name]
                    subject = input('修改科目：')
                    if subject in school_report:
                        try:
                            score = float(input('成绩：'))
                            students[name][subject] = score
                            score = students[name]
                            grade = 0
                            for info in list(score.values())[:10]:
                                grade = int(info) + grade
                            average_score = grade/10
                            main_subject = []
                            for subject,score in students[name].items():
                                subject = score
                                main_subject.append(subject)
                            grade = 0
                            for score in main_subject[:3]:
                                if score >= 90:
                                    grade = grade + 1
                            for score in main_subject[4:9]:
                                if score >= 60:
                                    grade = grade + 1
                            if main_subject[10] >= 30:
                                grade = grade + 1
                            a = grade/10*100
                            rate = f"{a}%"
                            students[name]['平均分']=average_score
                            students[name]['及格率']=rate
                            path.write_text(json.dumps(students,ensure_ascii=False,indent=2) + '\n' ,encoding='utf-8')
                        except ValueError:
                            print('请输入数字')
                elif name == 'no':
                    break
                else:
                    print('查无此人！！！')
        elif opt == 5:
            break
    else:
        print('请输入正确序号！！！')
