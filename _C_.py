from _Lib_._Lib_ import *
from instabot import Bot
import string
#-D-A-T-A-------------------------------------------------------------
import _DataStuff_.PostsLinks
import _DataStuff_.DailyMemory
import _DataStuff_.Targets
import _DataStuff_.DoneTargets
import _DataStuff_.Followed


class Telegram:
    
    def __init__(self):
        self.Bot_Token='BOT_TOKEN'
        self.Chat_Id="CHAT_ID"
    
    def SendMessage(self,bot_message,e=""):
        
        Init="""
        
        📛Initialized📛
        
        """
        
        
        Ban="""
        💩💩💩💩💩💩💩💩

        So...
            We Are All Screwed !!!
            _(ツ)_
            
                The Bot AutoMaticly Stopped But It Should Be Checked If There Is A BUG In Code 
                
                    Or
                
                The Instagram Account Is Banned By Reaching Instagram Goddamn Limits  (▀̿Ĺ̯▀̿ ̿)
                
        🔴📛⛔🔴📛⛔🔴📛
        
        """
        
        Count="""
        💩💩💩💩💩💩💩💩

        Can Not Get Count Of Followers
        
        🔴📛⛔🔴📛⛔🔴📛
        
        """
        
        TryExcept="""
        🛡️⚔️🛡️⚔️🛡️⚔️🛡️⚔️🛡️⚔️

        So...
            We Are Having Some Issues Due to Unfollow System !!!
            ̿'̿'\̵͇̿̿\з=( ͠° ͟ʖ ͡°)=ε/̵͇̿̿/'̿̿ ̿ ̿ ̿ 
            
            The System Will Ignore it And Continue Working!
                
        
        🔴📛⛔🔴📛⛔🔴
                
        """

        Fine="""
        ☢️☣️☢️☣️☢️☣️☢️☣️☢️☣️☢️☣️

        EveryThing Is Fine and Working !~!
                
        """
        
        HelpMessage={"Ban":Ban,"TryExcept":TryExcept,"Fine":Fine,'Count':Count,"Init":Init}
        Message= HelpMessage[bot_message]
        Message+='''
        
        '''+e
        
        
        bot_token = self.Bot_Token
        bot_chatID = self.Chat_Id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + Message
        response = requests.get(send_text)
        print (response)
        print ("Notification >>> "+str(bot_message)+"   "+str(e))

    def SendNakedText(self,Message):
        bot_token = self.Bot_Token
        bot_chatID = self.Chat_Id
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + Message
        response = requests.get(send_text)

    def sendWhoHasBeenUnFollowed(self,UserName):
        Time=str((":".join(map(str, DataStuff().Time()))))
        Enter=(string.whitespace)*2
        Message="Successfully Unfollowed"+Enter+'-- '+UserName+' --'+Enter+"Time : "+Time 
        Telegram().SendNakedText(Message)
    
    def SendPhoto(self,Path):
        token = self.Bot_Token
        chat_id = self.Chat_Id
        file = Path
        url = f"https://api.telegram.org/bot{token}/sendPhoto"
        files = {}
        files["photo"] = open(file, "rb")
        requests.get(url, params={"chat_id": chat_id}, files=files)

class Agriculture:
    
    def __init__(self,UserName="",Password="",SetDriver=True,SetBot=True,HeadLess=True):

        def SetUpDriver(HeadLess=True):
            options = webdriver.ChromeOptions()
            if HeadLess:
                options.add_argument('headless')
            options.add_argument('--no-sandbox')
            options.add_argument("start-maximized")
            options.add_argument("disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--user-agent=Mozilla/5.0 (Linux; Android 10; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36')
            Drive = webdriver.Chrome(chrome_options=options)
            return Drive

        if SetDriver:
            self.Drive=SetUpDriver(HeadLess)
         
        if SetBot:
            bot = Bot()
            bot.login(username=UserName, password=Password ,use_cookie=False)
            self.bot=bot  
    
    def LogIn(self,UserName,Password):
        self.Drive.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        InputElements=self.Drive.find_elements_by_class_name("zyHYP")
        UsernameInput=InputElements[0]
        PasswordInput=InputElements[1]
        UsernameInput.send_keys(str(UserName))
        PasswordInput.send_keys(str(Password))
        Click=self.Drive.find_elements_by_class_name("y3zKF")
        Click[-1].click()
        sleep(10)
        try:
            self.Drive.find_element_by_class_name("HoLwm").click()
        except:
            None

    def SaveCookie(self,UserName):
        CN=UserName+"_Cookies.pkl"
        pickle.dump(self.Drive.get_cookies() , open(CN,"wb"))

    def LogInInstagramByCookie(self,UserName):
        CN=UserName+"_Cookies.pkl"
        CN="/Cookies/"+CN
        CN=DataStuff().Pwd()+CN
        self.Drive.get('https://www.instagram.com/')
        for cookie in pickle.load(open((CN), "rb")):
            if 'expiry' in cookie:
                del cookie['expiry']
            self.Drive.add_cookie(cookie)
        print ("DONE Logging In")

    def DownloadPost(self,InstaUrl,DirName="Downloaded_Instagram_Pictures"):
        def dl(url):
            req = urllib.request.Request(url, headers = {'User-Agent':'Mozilla/5.0'})

            try:
                response = urllib.request.urlopen(req)

            except urllib.error.URLError as e:
                None

            except:
                exit('Error downloading data')

            return response

        if not re.match('(https://)?(www.)?instagram.com/p/\S+/?', InstaUrl):
            exit('Error {} not an instagram url'.format(InstaUrl))

        '''if args.quiet:
            sys.stdout = sys.stderr = open(os.devnull, 'w')'''
        if not(os.path.isdir(DirName)):
            os.makedirs(DirName)  

        print('Downloading')
        file_path = os.path.abspath(DirName) 

        url_id = InstaUrl.rstrip('/').split('/')[-1]

        url_response = dl(InstaUrl)

        html_lines = url_response.read().decode().splitlines()

        for html_line in html_lines:
            if '_sharedData = ' in html_line:
                json_data = json.loads(html_line.split('_sharedData = ')[1][:-10])

        if not 'json_data' in locals():
            exit('Error no data found')


        json_data = json_data['entry_data']['PostPage'][0]['graphql']['shortcode_media']

        json_content = []

        if 'edge_sidecar_to_children' in json_data:
            for e in json_data['edge_sidecar_to_children']['edges']:
                json_content.append(e['node'])

        else:
            json_content.append(json_data)
            
        Amount=0
        ListOfNames=[]
        Type=""
        for i, c in enumerate(json_content):
            Amount=i+1
            
            file_url = c['video_url'] if c['is_video'] else c['display_url']
            file_ext = 'mp4' if c['is_video'] else 'jpg'
            file_num = str(-(i+1)) if len(json_content) > 1 else ''
            file_name = '{}/{}{}.{}'.format(file_path, url_id, file_num, file_ext)

            url_response = dl(file_url)

            with open(file_name, 'wb') as f:
                f.write(url_response.read())
            ListOfNames.append(file_name)
            print('Saved {}'.format(file_name))
        if len(ListOfNames)>1:
            Type="Collection"
        elif (ListOfNames[0].split("."))[-1]=="mp4":
            Type="Video"
        else:
            Type="Image"
        return {"Amount":Amount,"Paths":ListOfNames,"Type":Type}
    
    def Post(self,Path,Caption):
        print ("---Posting---")
        self.bot.upload_photo(Path, caption=Caption)

    def Direct(self,UserName,Text):
        self.Drive.get("https://www.instagram.com/direct/new/")
        TypeTarget=self.Drive.find_element_by_class_name("M5V28")
        TypeTarget.send_keys(str(UserName))
        sleep(3)
        Choices=self.Drive.find_elements_by_class_name("soMvl")
        RawNames_=self.Drive.find_elements_by_class_name("uL8Hv")
        #RawNames_=RawNames_[1:]
        Names=[]
        for Name in RawNames_:
            Names.append(Name.text)
        if 'No account found.' in Names:
            return Names
        
        IndexTarget=Names.index(UserName)
        
        Choices[IndexTarget].click()
        self.Drive.find_element_by_class_name("cB_4K").click()
        sleep(3)
        TextArea=self.Drive.find_element_by_xpath("/html/body/div[1]/section/div[2]/div/div/div[2]/div/div/div/textarea")
        TextArea.send_keys(str(Text))
        Send=self.Drive.find_elements_by_class_name("y3zKF")
        Send[-1].click()
        return True

    def ReplyStory(self,UserName,Text):
        self.Drive.get("https://www.instagram.com/"+UserName)
        try:
            StoryButton=self.Drive.find_element_by_class_name("h5uC0")
        except:
            return {"Story":False,"Reply":False}
        
        StoryButton.click()
        sleep(3)
        try:
            TextArea=self.Drive.find_element_by_xpath("/html/body/div[1]/section/div/div/section/div[2]/footer/div/div/div[1]/div[1]/textarea")
        except:
            return {"Story":True , "Reply":False}
        
        TextArea.send_keys(Text)
        sleep(0.2)
        for _ in range(2):
            (self.Drive.find_elements_by_class_name("_4EzTm"))[-1].click()
            sleep(0.1)        
        return {"Story":True , "Reply":True}
    
    def CommentOnSpecificPost(self,Link,text):
        if Link[-1]!="/":
            self.Drive.get(Link+"/comments")
        else:
            self.Drive.get(Link+"comments")
            
        #self.Drive.find_element_by_class_name("_15y0l").click()
        textArea=self.Drive.find_element_by_class_name("Ypffh")
        textArea.send_keys(str(text))
        self.Drive.find_element_by_class_name("y3zKF").click()

    def Follow(self,UserName,Agriculture_All_Set_Up):
        Agriculture_All_Set_Up.GoToAccount(UserName)
        try:
            Follow=self.Drive.find_element_by_class_name("BY3EC")
        except:
            print (">>> Target Has Been Already Followed >>>  "+str(UserName)+"  <<<")
            return False
        sleep(2)
        Follow.click()
        sleep(2)
        print (">>> Followed >>>  "+str(UserName)+"  <<<")
        return True
    
    def UnFollow(self,UserName,Agriculture_All_Set_Up):
        Agriculture_All_Set_Up.GoToAccount(UserName)
        sleep(2)
        try:
            UnFollow=self.Drive.find_element_by_class_name("_6VtSN")
            try:
                Verificaton=self.Drive.find_element_by_class_name("BY3EC")
                print (">>> Target Has not Been Followed >>>  "+str(UserName)+"  <<<")
                return False
            except:
                pass
        except:
            try:
                UnFollow=self.Drive.find_element_by_class_name("_8A5w5")
            except:
                print (">>> Target Has not Been Followed >>>  "+str(UserName)+"  <<<")
                return False

        
        UnFollow.click()
        sleep(2)
        Confirm=self.Drive.find_element_by_class_name("-Cab_")
        Confirm.click()
        print (">>> UnFollowed >>>  "+str(UserName)+"  <<<")
        return True
   
    def CloseDriver(self):
        self.Drive.close()

    def GoToAccount(self,UserName):
        self.Drive.get("https://www.instagram.com/"+UserName)
        print ("Currntly We Are In >> "+str(UserName))
        
    def UnFollow_WhenYouAreInTargetAccount(self,UserName,Delay):
        def OpenFollowers():
            Followers = self.Drive.find_elements_by_class_name("g47SY")
            Followers[2].click()
            sleep(2)

            
        def ScrollDown():
            self.Drive.find_element_by_class_name("_1XyCr").click()
            body = self.Drive.find_element_by_css_selector('body')
            for i in range (1):
                body.send_keys(Keys.PAGE_DOWN)
                print ("---Scroll---")
                print (len(self.Drive.find_elements_by_class_name("_8A5w5"))-1)
                sleep(1)
        
        def HowMuchWeFound():
            return (int(len(self.Drive.find_elements_by_class_name("_8A5w5"))-1))
               
        OpenFollowers()
        sleep(3)
        print ("Found >>> "+str(HowMuchWeFound()))
        #ScrollDown()
        self.Drive.save_screenshot("SCREEN.png")
        Telegram().SendPhoto("SCREEN.png")
        os.remove("SCREEN.png")

        for i in range (HowMuchWeFound()):
            ListOfUnfollowChoices=self.Drive.find_elements_by_class_name("_8A5w5")
            ListOfNames=self.Drive.find_elements_by_class_name("_0imsa")
            ListOfUnfollowChoices[1].click()
            sleep(1)
            (self.Drive.find_elements_by_class_name("aOOlW"))[0].click()
            print (">>>SuccessFully UnFollowed<<< at time  ",(":".join(map(str, DataStuff().Time()))))
            Telegram().sendWhoHasBeenUnFollowed(str(ListOfNames[i].text))
            if i>=20:
                break
            sleep(Delay)
            
      
    def CountFollowingAndFollowers(self,Target):
        url = 'https://www.instagram.com/' + Target
        r = requests.get(url).text

        followers = re.search('"edge_followed_by":{"count":([0-9]+)}',r).group(1)
        followings = re.search('"edge_follow":{"count":([0-9]+)}',r).group(1)
        return [followers,followings]

    def MinePostLinks_WhenYouAreInTargetAccount_OldVersion(self,ListOfPosts):
        sleep(5)
        Links=[]
        sleep(5)
        Posts=self.Drive.find_elements_by_class_name("FFVAD")
        for i in ListOfPosts:
            if i>len(Posts):
                print ("--- Post UnAvaiable ---")
                return False
        print ('--Start Mining Posts---')
        for PostIndex in ListOfPosts:
            #print (Posts[PostIndex].get_at)
            pass
        
    def MinePostLinks_WhenYouAreInTargetAccount(self,ListOfPosts):
        sleep(5)
    
        Links=[]
        SelectedLinks=[]
        print ('--Start Mining Posts---')
        for i in(self.Drive.find_elements_by_xpath("//a")):
            Link=(i.get_attribute("href"))
            Test=Link.split("/")
            if "p" in Test:
                Links.append(Link)
                
        for i in ListOfPosts:
            if i>len(Links):
                print ("--- Post UnAvaiable ---")
                return False 
            SelectedLinks.append(Links[int(i)-1])       
        #print (SelectedLinks)
        return SelectedLinks
            



        print ("Done Mining , Got _ "+str(len(Links))+" _Posts")
        return Links
    
    def Repost(self,Agriculture_All_Set_Up,UserName,Password,Caption="Temporally"):
        ContentTarget=(DataStuff().ContentTarget())
        for Target in ContentTarget:
            Agriculture_All_Set_Up.GoToAccount(Target)
            
            ListOfPostNames=Agriculture_All_Set_Up.MinePostLinks_WhenYouAreInTargetAccount([1,2,3])
            #print (ListOfPostNames)
            if ListOfPostNames!=False:
                for PostOfThree in ListOfPostNames:
                    if PostOfThree not in (DataStuff().ReturnPostsLinks()):
                        print (PostOfThree)
                        Data=Agriculture_All_Set_Up.DownloadPost(PostOfThree)
                        print (Data)
                        if Data["Type"]=="Image":
                            Agriculture_All_Set_Up.Post(*(Data["Paths"]),Caption)
                            DataStuff().AddPostsLinks(PostOfThree)
                            for Path in Data["Paths"]:
                                DataStuff().DeleteFile(str(Path)+".REMOVE_ME")
                            return True
                        else:
                            print (">Damn , The Post Wasnt an IMAGE")
                            for Path in Data["Paths"]:
                                DataStuff().DeleteFile(Path)   
                    else:
                        print (">Damn , That Has Been Already Posted")
        return False
    
    def AutoFollow(self,Agriculture_All_Set_Up,AmounMinutesToTry=9**9**2):
        Secs=AmounMinutesToTry*60
        OneRawTarget=DataStuff().ReturnRawTargets(1)
        if OneRawTarget==False:
            print (">>> Quit Auto Follow , Not One Raw Target <<<")
            return False
        Before=time()
        while not(Agriculture_All_Set_Up.Follow(OneRawTarget[0],Agriculture_All_Set_Up)):
            OneRawTarget=DataStuff().ReturnRawTargets(1)
            if OneRawTarget==False:
                print (">>> Quit Auto Follow , Not One Raw Target <<<")
                return False
            if time()-Before>=Secs:
                print (" Cant Follow Due To Time ")
                return False
            
        DataStuff().AddToDoneTargets(OneRawTarget[0])
        DataStuff().AddToFollowed(OneRawTarget[0])
        
        return True
             
    def AutoUnFollow(self,Agriculture_All_Set_Up,DaysLimit=2):
        FollowData=DataStuff().ReturnFollowed()
        if len(FollowData)==0:
            print (">>> Followings Are 0 <<<")
            return False     
        SuitableCases=[]
        for EachFollowing in FollowData:
            DateFollowed=EachFollowing["Date"]
            DateNow=DataStuff().Date()
            DaysFollowed=(DateNow[0] - DateFollowed[0])*365 + (DateNow[1] - DateFollowed[1])*30 + (DateNow[2] - DateFollowed[2])
            if DaysFollowed>=DaysLimit:
                SuitableCases.append([DaysFollowed,EachFollowing["UserName"]])
        
        SuitableCases.sort()
        if len(SuitableCases)==0:
            return False
        SuitableCases.reverse()
        for Case in SuitableCases:
            UserNameCase=Case[1]
               
            if Agriculture_All_Set_Up.UnFollow(UserNameCase,Agriculture_All_Set_Up):
                print ("Days : "+str(Case[0]))
                DataStuff().DeleteFromFollowed(UserNameCase)
                return True  
    
    def AutoReplyStory(self,Agriculture_All_Set_Up,AmounMinutesToTry=9**9**2):
        Secs=AmounMinutesToTry*60
        Before=time()
        for UserName in DataStuff().ReturnRawTargets():
            Response=Agriculture_All_Set_Up.ReplyStory(UserName,DataStuff().ReplyGenerator())
            if Response["Story"]==True and Response["Reply"]==True:
                print (UserName)
                DataStuff().AddToDoneTargets(UserName)
                return True
            if time()-Before>=Secs:
                print (" Cant Find any Story Due To Time ")
                return False
        return False
    
    def AutoDirect(self,Agriculture_All_Set_Up,AmounMinutesToTry=9**9**2):
        

        Secs=AmounMinutesToTry*60
        Before=time()
        while True:
            Case=DataStuff().ReturnRawTargets(1)
            Case=Case[0]
            #Case="sjhudusifgsufgwetgwdwew"
            Verification=Agriculture_All_Set_Up.Direct(Case,DataStuff().DirectGenerator())
            if not('No account found.' in str(Verification)):
                DataStuff().AddToDoneTargets(Case)
                return True
            if time()-Before>=Secs:
                print (" Cant Find any Story Due To Time ")
                return False
        
    def AutoAction(self,Action,Agriculture_All_Set_Up):
        ActionsDict={
            'Direct':[Agriculture_All_Set_Up.AutoDirect,(Agriculture_All_Set_Up,5)],
            'ReplyStory':[Agriculture_All_Set_Up.AutoReplyStory,(Agriculture_All_Set_Up,5)],
            'Follow':[Agriculture_All_Set_Up.AutoFollow,(Agriculture_All_Set_Up,5)],
            'Direct':[Agriculture_All_Set_Up.AutoDirect,(Agriculture_All_Set_Up,2)],
        }
        if Action not in ActionsDict:
            return False
        ActionsDict[Action][0](*ActionsDict[Action][1])
        if not(DataStuff().IsDailyMemoryForToday()):
            DataStuff().ReplaceFile()
        DataStuff().AutoAddValue(Action)
        
class DataStuff:
    
    def ActionLimits(self,TheKey):
        Limits={
            'Direct':15 ,
            'DirectPerDay':50 , 
            'Follow':7 , 
            'FollowPerDay':100 , 
            'UnFollow':7 , 
            'UnFollowPerDay':100 , 
            'ReplyStory':60 , 
            'ReplyStoryPerDay':10 , 
        }
        
        try:
            return Limits[TheKey]
        except:
            return False
    
    def ReturnWhatCanWeDoNow(self):
        if not(DataStuff().IsDailyMemoryForToday()):
            DataStuff().ReplaceFile()
            print ("Memory Updated")
        
        Dict=DataStuff().GetDailyMemory()
        Actions=[]
        for Key in Dict:
            if not( len(Dict[Key]) >= DataStuff().ActionLimits(str(Key)+"PerDay") ):
                ListOfActions=Dict[Key]
                if ListOfActions==[]:
                    Actions.append([1,str(Key)])
                else:
                    ListOfActions.sort()
                    LastActionTime=ListOfActions[-1]
                    MinLastAction=LastActionTime[0]*60+LastActionTime[1]
                    TimeNow=DataStuff().Time()
                    MinTimeNow=TimeNow[0]*60+TimeNow[1]
                    if MinTimeNow<MinLastAction:
                        MinTimeNow=24*60
                    Space=MinTimeNow-MinLastAction
                    if Space>DataStuff().ActionLimits(Key):
                        Actions.append([1/(Space-DataStuff().ActionLimits(Key)),Key])
                    elif Space==DataStuff().ActionLimits(Key):
                        Actions.append([1,Key])

        if Actions==[]:
            return False

        Actions.sort()
        BestAction=Actions[0]
        SimilarBestActions=[]
        for Action in Actions:
            if Action[0]==BestAction[0]:
                SimilarBestActions.append(Action)
            else:
                break
        RandomBestAction=(random.choice(SimilarBestActions))
        KeyOfBestAction=RandomBestAction[1]
        #return KeyOfBestAction,Actions
        Actions.remove(RandomBestAction)
        KeyActions=[]
        for Action in Actions:
            KeyActions.append(Action[1])
        return {'BestAction':KeyOfBestAction , 'AllActionsExceptBestAction':KeyActions}     
        
    def IsDailyMemoryForToday(self):
        Dict=DataStuff().GetDailyMemory() 
        if Dict["Date"] == DataStuff().Date():
            return True
        else:
            return False
    
    def AutoAddValue(self,TheKey):
        if TheKey=="Date":
            return False
        
        Dict=DataStuff().GetDailyMemory() 
        try:
            Dict[TheKey].append(DataStuff().Time())
        except:
            return False
        DataStuff().ReplaceFile(Dict)
        
        print (">>>SuccessFully Updated<<<")
        return True
    
    def ReplaceFile(self,FileData="None",NameFile="DailyMemory.py",NameData="DailyReport"):
        if FileData=="None":
            FileData=DataStuff().RawDictionaryOfData()
        DataStuff().DeleteFile(NameFile)
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+NameFile
        with open (NameFile,"w") as f:
            f.write(str(str(NameData)+"=")+str(FileData))
            f.close()
        print (">>> "+str(NameData)+" SuccussFully Replaced <<<")
        
    def GetDailyMemory(self):
        DailyMemory_ = reload(_DataStuff_.DailyMemory)
        DailyMemory_ = _DataStuff_.DailyMemory.DailyReport
        return DailyMemory_
    
    def GetTargets(self):
        AllTargets_ = reload(_DataStuff_.Targets)
        AllTargets_ = _DataStuff_.Targets.AllTargets
        return AllTargets_
    
    def GetDoneTargets(self):  
        DoneTargets_ = reload(_DataStuff_.DoneTargets)
        DoneTargets_ = _DataStuff_.DoneTargets.DoneTargets
        DoneTargets_ = list(DoneTargets_)
        DoneTargets_.remove("UserName")
        return DoneTargets_
    
    def RawDictionaryOfData(self):
        Dict={
            
            "Date" : DataStuff().Date(),
            
            "Direct" : [],
            
            "Follow" : [],
            
            "UnFollow" : [],
            
            "ReplyStory" : [],
            
        }
    
        return Dict

    def Date(self):
        Raw=str(datetime.datetime.now())
        Raw=Raw.split(" ")
        Raw=Raw[0]
        Raw=Raw.split("-")
        for i in range (len(Raw)):
            Raw[i]=int(Raw[i])
        
        return Raw
       
    def Time(self):
        Raw=str(datetime.datetime.now())
        Raw=Raw.split(" ")
        Raw=Raw[1]
        Raw=Raw.split(":")
        for i in range (len(Raw)):
            Raw[i]=float(Raw[i])
        for i in range (len(Raw)):
            Raw[i]=int(Raw[i])
        
        return Raw[0:2]
      
    def CaptionGenerator(self):
        
        Text="""
        !
            
             
                
            (▀̿Ĺ̯▀̿ ̿)
            
             
        اگر در اکسپلور هستید , بفرمایید.
         
           
            
             
              
               
               
        ===============
        ===============
        ===============
        """
        HashTags=['#گیمر_حرفه_ای ', '#فیفا ', '#پلی_استیشن4 ', '#پلستیشن4 ', '#گیمرهای_ایرانی ', '#د_لست_اف_اس2 ', '#بازی_ویدیویی ', '#گیمز ', '#گیمرها ', '#گیمر ', '#ایکس_باکس', '#نوستالژی ', '#گیمرهای_پیر ', '#گیمینگ ', '#گیمر_حرفه_ای', '#ایکس_باکس ', '#گیمرها', '#بازی_قدیمی ', '#پلستیشن5 ', '#گیمر_ایرانی ', '#گیم ', '#فیفا۲۰ ', '#گیمرای_ایران ', '#پلی_استیشن ', '#گیمرایرانی ', '#سگا ', '#د_لست_اف_اس']

        return Text+(" ".join(HashTags))
    
    def DirectGenerator(self):
        
        Text="""
        چرا این همه پیج گیم رو فالو کردی؟
            
            
            
        (▀̿Ĺ̯▀̿ ̿)
        @Game_Revisto
        کامل ترین مرجع جمع آوری ترند های گیم و فان
            
        """
        Text.replace("        ","")
        Text.replace("      ","")
        return Text
  
    def ReplyGenerator(self):
        Text="""
        چرا این همه پیج گیم رو فالو کردی؟ 
        @Game_Revisto 
        """
        
        return Text 
  
    def ContentTarget(self):
        List=['donyaye.game', 'gametester.ir', 'zula_club', 'funtrol', 'gameroidsetups', 'donsgame', 'digi__game', 'gameofsen', 'resane_game', 'farsitoons', 'pandagaming.ir', 'game__soul', 'valhalla.assassinscreed', 'gta_san_andreas_fanpage', 'akhbar_bazii_jadid', 'caffeplay.ir', 'baziips4', 'baazi.tori', 'orinokogamingunion', 'richthofen774_gm', 'maddgamers', 'gamersdreampark', 'game_._cut', 'hazardoushtv', 'gam3r.ir', 'nsworld.ir', 'irgame_fun', 'bazi_gram', 'key_mart_ir', 'shadowgame_fa', 'gameplayiran', 'keoxic.plays', 'magnetgame', 'kourosh_toupia', 'zhangoolak', 'game.shop_ir', 'looketo', 'persiian_text', 'mr_gameclub', 'box.bazi', 'controlzed.ir']
        List_=[]
        while len(List)!=0:
            RandomChoice=random.choice(List)
            List.remove(RandomChoice)
            List_.append(RandomChoice)
        return List_
        #return ["nsworld.ir"]
        
    def ReturnPostsLinks(self):
        NewLinks = reload(_DataStuff_.PostsLinks)
        NewLinks = NewLinks.LinksPosted
        return NewLinks
    
    def AddPostsLinks(self,Link):
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+'PostsLinks.py'
        with open(NameFile , 'a+') as f:
            f.write('"'+str(Link)+'"'+",")
            f.close()

    def DeleteFile(self,Path):
        try:
            os.remove(Path)
            print ("Successfully Removed")
            return True
        except:
            try:
                Pwd=DataStuff().Pwd()
                NameFile=Pwd+'/_DataStuff_/'+Path
                os.remove(NameFile)
                print ("Successfully Removed")
                return True
            except:
                print ("No Such File to Be Removed")
                return False
         
    def Pwd(self):
        return str(os.getcwd())
    
    def AddToFollowed(self,UserName):
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+'Followed.py'
        with open(NameFile , 'a+') as f:
            f.write(
                str({"UserName" : str(str(UserName)) , "Date" : DataStuff().Date()}) + " , "
            )
            f.close()
    
    def AddToDoneTargets(self,UserName):
        Pwd=DataStuff().Pwd()
        NameFile=Pwd+'/_DataStuff_/'+'DoneTargets.py'
        with open(NameFile , 'a+') as f:
            f.write(
                str('"'+str(UserName)+'"') + " , "
            )
            f.close()
    
    def ReturnFollowed(self):
        Followed_ = reload(_DataStuff_.Followed)
        Followed_ = Followed_.FollowedUserNames
        Followed_=list(Followed_)
        Followed_.remove({"UserName":"UserName" , "Date":[0000,0,0]})
        return Followed_
        
    def DeleteFromFollowed(self,UserName):
        List=DataStuff().ReturnFollowed()
        for Dict in List:
            if Dict["UserName"]==UserName:
                TargetFound=Dict
                List.remove(TargetFound)
                List.insert(0,{"UserName":"UserName" , "Date":[0000,0,0]})
                Written=str(tuple(List))
                Written=Written[1:-1]
                if not(Written[-1]=="," or Written[-2]==","):
                    Written+=" , "
                DataStuff().ReplaceFile(Written,"Followed.py",'FollowedUserNames')
                return True
        return False
    
    def ReturnRawTargets(self,AmountToReturn="All"):
        All=DataStuff().GetTargets()
        Done=DataStuff().GetDoneTargets()
        Raw=(list(set(All) - set(Done))) 
        if AmountToReturn=="All":
            return Raw
        else:
            if len(Raw)>=AmountToReturn:
                return Raw[0:int(AmountToReturn)]
            else:
                print (" >>> There Is Not That Much Raw Targets To Return , All Amount is >>> ",len(Raw) , " <<< ")
                return False
        
class Full_Programs:
    
    def UnFollow(self,UserName,CookieName=True,HeadLess=True,DelayEachSingleUnfollow=200): 
        if CookieName:
            CookieName=UserName
        Telegram().SendMessage("Init")

        DelayPackage=210
        i=0
        while True:
            i+=1
            '''try:
                Before=(Agriculture().CountFollowingAndFollowers("Urge_ir"))[1]
                print ("Before = ",Before)
            except Exception as e:
                Telegram().SendMessage("Count",str(e))
                print (e)'''

            try:
                Insta=Agriculture(SetBot=False,HeadLess=HeadLess)
                Insta.LogInInstagramByCookie(CookieName)
                Insta.GoToAccount(UserName)
                Insta.UnFollow_WhenYouAreInTargetAccount(UserName,DelayEachSingleUnfollow)
                #Insta.CloseDriver()
                sleep(DelayPackage)
            
            
            except Exception as e:
                print ("<<<>>><<<>>> There Is An ERROR <<<>>><<<>>>")
                print (e)
                Telegram().SendMessage("TryExcept",str(e))
                try:
                    Insta.CloseDriver()
                except:
                    pass
            
            
            '''try:
                Now=(Agriculture().CountFollowingAndFollowers("Urge_ir"))[1]
                if Before-Now <= CountUnfollows:
                    Telegram().SendMessage("Ban")
                    break
            except Exception as e:
                Telegram().SendMessage("Count",str(e))
                print (e)'''
            
            if i%1==0:
                Telegram().SendMessage("Fine")
            
    def AutoPost(self,UserName,PassWord,EachMinute,Amount=9**9**2,HeadLess=True,SetBot=True):
        Insta=Agriculture(UserName,PassWord,SetBot=SetBot,HeadLess=HeadLess)
        sleep(50)
        Insta.LogInInstagramByCookie("Game_Revisto")
        for _ in range (Amount):
            Bef=time()
            if True:
                while not(Insta.Repost(Insta,UserName,PassWord,DataStuff().CaptionGenerator())):
                    pass      
                Now=time()
                Taken=Now-Bef
                if not(Taken>=EachMinute*60):
                    print ("WAITING >>>  ",str(EachMinute*60-Taken),"sec" )
                    sleep(EachMinute*60-Taken)
                
            '''except Exception as e:
                print ("error >>>  ",e)
                print ("***********Couldnt Make It*******************")'''
                
        Insta.CloseDriver()
         
    def FollowerEarner(self,UserName,PassWord,CookieName=True,HeadLess=True):
        if CookieName:
            CookieName=UserName
        Insta=Agriculture(UserName,PassWord,SetBot=True,HeadLess=HeadLess)
        Insta.LogInInstagramByCookie(CookieName)
        
        def EachLoop():
        
            if not(DataStuff().IsDailyMemoryForToday()):
                DataStuff().ReplaceFile()
            
            ResponseWhatCanWeDoNow=DataStuff().ReturnWhatCanWeDoNow()
            if ResponseWhatCanWeDoNow!=False:
                if Insta.AutoAction(ResponseWhatCanWeDoNow["BestAction"],Insta):
                    print ("---___--- "+ResponseWhatCanWeDoNow["BestAction"]+" ---___---")
                    return True
                for Act in ResponseWhatCanWeDoNow['AllActionsExceptBestAction']:
                    if Insta.AutoAction(Act,Insta):
                        print ("---___--- "+Act+" ---___---")
                        return True
            
            return False
            
        while True:
            EachLoop()
            sleep(1)

