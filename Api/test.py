import requests
import json
def course():
    url = "http://saral.navgurukul.org/api/courses"
    v = requests.get(url).text
    p = json.loads(v)
    a=p["availableCourses"]
    cc=1
    for i in a:
        print(f'{cc}.',i['name'])
        cc+=1 
    print(a[0]['id'])
    intt=int(input('enter the course : '))
    global iid
    iid=a[intt-1]['id']
    print('id of course : ',iid)
    return iid


def coursedetail():
    iid=course()
    url2=f"http://saral.navgurukul.org/api/courses/{iid}/exercises"
    vv=requests.get(url2).content
    pp=json.loads(vv)
    jj=open('coursedetail.json','w')
    json.dump(pp,jj,indent=4)
    jj.close()
    count=1
    global slugdic
    slugdic={}
    for  i in pp['data']:
        print(f'{count}.',i['name'])
        ccc=1
        slugdic.update({f'{count}':i['slug']})
        # sluglist.append(i['slug'])

        for j in i['childExercises']:
            print(f'\t{count}.{ccc}',j['name'])
            slugdic.update({f'{count}.{ccc}':j['slug']})
            ccc+=1
        count+=1
        
    # print(sluglist)
    # print(slugdic)
    # print(json.dumps(slugdic,indent=4))
    print()
    ipp=input('enter the qeustion no. : ')
    return ipp
coursedetail()
def question():
    s=coursedetail()
    url3=f"http://saral.navgurukul.org/api/courses/{iid}/exercise/getBySlug?slug={slugdic[s]}"
    cc=requests.get(url3).text
    # print(type(cc))
    sss=json.loads(cc)
    list1=(sss['content'])
    p=json.loads(list1)   
    for i  in p:
        print(i['value'])

        
    
question()
